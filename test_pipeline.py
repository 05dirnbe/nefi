#!/usr/bin/env python3

import os
from nefi2.model.ext_loader import ExtensionLoader
import sys
sys.path.insert(0, os.path.join(os.curdir, 'nefi2', 'model'))
sys.path.insert(0, os.path.join(os.curdir, 'nefi2', 'model', 'categories'))
sys.path.insert(0, os.path.join(os.curdir, 'nefi2', 'model', 'algorithms'))


def main():
    ext = ExtensionLoader()
    print(ext.cats_container)

if __name__ == '__main__':
    main()
