# -*- coding: utf-8 -*-
"""
Use this script to update the submodule `reveal.js` with the proper
customization.

- update package.json
- add custom themes
"""
import pathlib
import shutil
import json
import sys
import subprocess
import logging
import logging.config

import toml
import click


def main(here, root):
    logging.config.fileConfig(here / "logging.conf")

    logger = logging.getLogger("make")

    misc = root / "misc"
    sandbox = root / "_sandbox"

    # make a copy
    # -----------

    shutil.rmtree(sandbox, ignore_errors=True)
    shutil.copytree(
        root / "reveal.js",
        sandbox,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".git", ".github"),
    )

    # update package.json
    # -------------------

    package_json = sandbox / "package.json"
    with open(package_json) as f:
        package_json_content = json.load(f)

    with open(misc / "rm-package.json") as f:
        rm = json.load(f)
    with open(misc / "add-package.json") as f:
        add = json.load(f)

    for d in rm:
        del package_json_content[d]
    package_json_content.update(add)

    with open(package_json, "w") as f:
        json.dump(package_json_content, f, indent=2)

    # load and add configs
    # --------------------

    presentation_toml = "presentation.toml"

    with open(presentation_toml) as f:
        configs = toml.load(f)

    shutil.copy2(presentation_toml, sandbox)

    # add structures
    # --------------

    structure = root / "structures" / configs["structure"]["name"]
    requirements = structure / "requirements.txt"
    structure_configs = structure / "structure.yaml"
    template = structure / "template.html"
    build_script = structure / "build_template.py"

    if click.confirm(
        "Do you want to install the required dependencies?", default=False
    ):
        print("Installing required packages:")
        with open(requirements) as f:
            for line in f.readlines():
                if not line or line[0] == "#":
                    continue
                print(f"  - {line}")

        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements.resolve())]
        )
        # TODO add logs

    # TODO manage configs

    shutil.copy2(build_script, sandbox)
    shutil.copy2(template, sandbox)

    # TODO hardcoded files tree, this should depend on the structure chosen
    slides = sandbox / "src" / "slides"
    slides.mkdir(parents=True, exist_ok=True)
    (slides / "0.html").touch(exist_ok=True)

    # Add room for assets

    (sandbox / "assets").mkdir(parents=True, exist_ok=True)

    # add themes
    # ----------

    themes = root / "themes"
    reveal_themes = sandbox / "dist/theme"

    # TODO replaceable_themes should not be hardcoded
    replaceable_themes = []
    not_replaceable_themes = [
        "beige",
        "black",
        "blood",
        "league",
        "moon",
        "night",
        "serif",
        "simple",
        "sky",
        "solarized",
        "white",
    ]

    for theme in reveal_themes.glob("*.css"):
        dst = themes / theme.name
        if not dst.is_file() or (
            theme.stem in replaceable_themes
            or (
                theme.stem not in not_replaceable_themes
                and click.confirm(
                    f"Do you want to replace theme '{theme.name}'?", default=False
                )
            )
        ):
            shutil.move(theme, dst)

    shutil.copytree(reveal_themes / "fonts", reveal_themes / ".." / "fonts")
    shutil.rmtree(reveal_themes, ignore_errors=True)

    shutil.copy2(themes / configs["theme"]["name"], sandbox / "dist" / "theme.css")
    shutil.copy2(themes / "reveal.css", sandbox / "dist" / "reveal.css")

    # clean up
    # --------
    # remove unneeded files from original repo

    # TODO unneeded_dirs and unneeded_files should not be hardcoded
    unneeded_dirs = ["css", "examples", "js", "test"]
    unneeded_files = [
        "CONTRIBUTING.md",
        "demo.html",
        "index.html",
        "LICENSE",
        "package-lock.json",
        "README.md",
    ]

    for d in unneeded_dirs:
        shutil.rmtree(sandbox / d, ignore_errors=True)
    for f in unneeded_files:
        (sandbox / f).unlink(missing_ok=True)


if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent
    root = here / ".."

    print()
    main(here, root)
