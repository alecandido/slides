# -*- coding: utf-8 -*-
"""
Use this script to build the presentation release:

- source into `my-reveal/src`
- release into `my-reveal/build`
"""
import logging
import logging.config


def main():
    logging.config.fileConfig("logging.conf")

    logger = logging.getLogger("make.build")


if __name__ == "__main__":
    main()
