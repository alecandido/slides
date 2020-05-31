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
import logging
import logging.config

import toml


def main(here, root):
    logging.config.fileConfig(here / "logging.conf")

    logger = logging.getLogger("make")

    misc = root / "misc"
    my_reveal = root / "my-reveal"

    # make a copy
    # -----------

    shutil.rmtree(my_reveal, ignore_errors=True)
    shutil.copytree(
        root / "reveal.js",
        my_reveal,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".git", ".github"),
    )

    # update package.json
    # -------------------

    package_json = my_reveal / "package.json"
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

    __import__("pprint").pprint(configs)

    shutil.copy2(presentation_toml, my_reveal)

    # add structures
    # --------------

    # MISSING

    # add themes
    # ----------

    # MISSING

    # add src folder
    # --------------

    (my_reveal / "src").mkdir(exist_ok=True)


if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent
    root = here / ".."

    main(here, root)
