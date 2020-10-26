# -*- coding: utf-8 -*-
"""
Use this script to restore a presentation environment from a tarball, it will
destroy the current `_sandbox` environment
"""
import os
import pathlib
import shutil
import logging
import logging.config

import click

import make


def main(here, root):
    logging.config.fileConfig(here / "logging.conf")

    logger = logging.getLogger("make.inflate")
    # logger.setLevel(100)
    # print(logger.getEffectiveLevel())

    # ask for authorization
    # ---------------------

    if not click.confirm(
        "Are you sure to delete the current '_sandbox' environment?", default=False
    ):
        print("Nothing done.")
        quit()

    logger.info("Authorized to replace '_sandbox' environment.")

    # checkout a brand new instance of _sandbox
    # ------------------------------------------

    shutil.rmtree(root / "_sandbox", ignore_errors=True)

    os.system("git submodule update")
    make.main()

    # inflate the tarball
    # -------------------

    # MISSING


if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent
    root = here / ".."

    main(here, root)
