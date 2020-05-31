# -*- coding: utf-8 -*-
"""
Use this script to build an updatable version of the presentation, to be used
during the composition process.

For a live update run:

.. shell::

    watch -n1 make preview

"""
import logging
import logging.config


def main():
    logging.config.fileConfig("logging.conf")

    logger = logging.getLogger("make.preview")


if __name__ == "__main__":
    main()
