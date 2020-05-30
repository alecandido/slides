# -*- coding: utf-8 -*-
"""
Use this script to restore a presentation environment from a tarball, it will
destroy the current `my-reveal` environment
"""
import os
import pathlib
import shutil
import logging
import logging.config

import click

import make


def main():
    logging.config.fileConfig("logging.conf")

    logger = logging.getLogger("make.inflate")
    # logger.setLevel(100)
    # print(logger.getEffectiveLevel())

    # ask for authorization
    # ---------------------

    if not click.confirm(
        "Are you sure to delete the current 'my-reveal' environment?", default=False
    ):
        print("Nothing done.")
        quit()

    logger.info("Authorized to replace 'my-reveal' environment.")

    # checkout a brand new instance of my-reveal
    # ------------------------------------------

    here = pathlib.Path(__file__).resolve().parent
    shutil.rmtree(here / "my-reveal", ignore_errors=True)

    os.system("git submodule update")
    make.main()

    # inflate the tarball
    # -------------------

    # MISSING


if __name__ == "__main__":
    main()
