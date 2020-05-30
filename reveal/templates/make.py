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


def main():
    logger = logging.getLogger("make")

    here = pathlib.Path(__file__).resolve().parent
    misc = here / "misc"
    my_reveal = here / "my-reveal"

    # make a copy
    # -----------

    shutil.copytree(here / "reveal.js", my_reveal, dirs_exist_ok=True)

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
    main()
