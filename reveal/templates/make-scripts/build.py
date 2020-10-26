# -*- coding: utf-8 -*-
"""
Use this script to build the presentation release:

- source into `_sandbox/src`
- release into `_sandbox/build`
"""
import sys
import pathlib
import shutil
import subprocess
import logging
import logging.config

import toml


def main(here, root):
    # start logging
    # =============
    logging.config.fileConfig(here / "logging.conf")

    logger = logging.getLogger("make.build")

    # load configs
    # ============
    sandbox = root / "_sandbox"
    presentation_toml = sandbox / "presentation.toml"

    with open(presentation_toml) as f:
        configs = toml.load(f)

    # init build folder
    # =================
    build = root / configs["title"]
    print(build)
    shutil.rmtree(build, ignore_errors=True)
    build.mkdir()

    shutil.copy2(presentation_toml, build)

    # run the build
    # =============

    subprocess.check_call([sys.executable, (sandbox / "build_template.py").resolve()])

    # collect all relevant files
    # ==========================
    dist = build / "dist"
    dist.mkdir()

    # css
    for css in ["reveal", "reset", "theme"]:
        shutil.copy2(sandbox / "dist" / f"{css}.css", dist / f"{css}.css")

    # assets
    shutil.copytree(sandbox / "dist" / "fonts", dist / "fonts")

    # js
    shutil.copy2(sandbox / "dist" / "reveal.js", dist / "reveal.js")
    shutil.copytree(sandbox / "plugin", build / "plugin")

    # html
    shutil.copy2(sandbox / "index.html", build / "index.html")

    # assets
    shutil.copytree(sandbox / "assets", build / "assets")

    # make a compressed copy of the full dir
    # ======================================
    subprocess.check_call(
        ["tar", "cvzf", build / "_sandbox.tar.gz", sandbox.relative_to(root)],
        cwd=root,
    )


if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent
    root = here / ".."

    main(here, root)
