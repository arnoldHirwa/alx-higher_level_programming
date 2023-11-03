#!/usr/bin/python3
import importlib.util as utils

if __name__ == "__main__":
    path = "hidden_4.pyc"
    spec = utils.spec_from_file_location("hidden_4", path)
    myMod = utils.module_from_spec(spec)
    spec.loader.exec_module(myMod)
    # Get names from module
    for name in (dir(myMod)):
        if not name.startswith('__'):
            print(name)
