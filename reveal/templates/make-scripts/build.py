# -*- coding: utf-8 -*-
"""
Use this script to build the presentation release:

- source into `my-reveal/src`
- release into `my-reveal/build`
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
    my_reveal = root / "my-reveal"
    presentation_toml = my_reveal / "presentation.toml"

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

    subprocess.check_call([sys.executable, (my_reveal / "build_template.py").resolve()])

    # collect all relevant files
    # ==========================
    dist = build / "dist"
    dist.mkdir()

    # css
    for css in ["reveal", "reset", "theme"]:
        shutil.copy2(my_reveal / "dist" / f"{css}.css", dist / f"{css}.css")

    # assets
    shutil.copytree(my_reveal / "dist" / "fonts", dist / "fonts")

    # js
    shutil.copy2(my_reveal / "dist" / "reveal.js", dist / "reveal.js")
    shutil.copytree(my_reveal / "plugin", build / "plugin")

    # html
    shutil.copy2(my_reveal / "index.html", build / "index.html")

    # make a compressed copy of the full dir
    # ======================================
    subprocess.check_call(
        ["tar", "cvzf", build / "my-reveal.tar.gz", my_reveal.resolve()]
    )


if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent
    root = here / ".."

    main(here, root)
