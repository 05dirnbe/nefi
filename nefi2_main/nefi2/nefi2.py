#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
The main nefi2 startup script.
It loads extension loader and initializes UI.
It also enables console batch processing mode.
"""


from ext_loader import ExtensionLoader


__version__ = 0.1


def main():
    """Start the main pipeline and UI"""
    exloader = ExtensionLoader()
    # pipeline = Pipeline(_steps_container, _default_config)
    # init_UI()  # not yet implemented!


if __name__ == '__main__':
    main()
