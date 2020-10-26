# -*- coding: utf-8 -*-
"""
Use this script to build an updatable version of the presentation, to be used
during the composition process.

For a live update run:

.. shell::

    watch -n1 make preview

"""
import sys
import pathlib
import logging
import logging.config


def main(here, root):
    sandbox = root / "_sandbox"
    sys.path.append(str(sandbox))
    import build_template

    # start logging
    # =============
    logging.config.fileConfig(here / "logging.conf")

    logger = logging.getLogger("make.preview")

    # build index.html
    # ================
    build_template.main(sandbox)


if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent
    root = here / ".."

    main(here, root)
