#!/usr/bin/python3

if __name__ == "__main__":

    import importlib
    mod_import = importlib.import_module('hidden_4')

    names = dir(mod_import)

    for i, name in enumerate(names):
        if name[0] == '_':
            continue

        print(f"{name}")
