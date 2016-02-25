#!/usr/bin/env python3

import os

COUNTER = 0

def automodule(module_path, module_name):
    result = module_name + "\n"

    for i in range(0, len(module_name)):
        result += "-"

    result += "\n\n.. automodule:: " + module_path + "\n"
    result += "\t:members:\n\t:undoc-members:\n\t:show-inheritance:\n\n"
    return bytes(result, "UTF-8")


def create_title(name):
    result = name + "\n"

    for i in range(0, len(name)):
        result += "="

    result += "\n\n"
    return bytes(result, "UTF-8")


def walk(file, url, rst_url):
    for f in os.listdir(url):
        if os.path.isfile(os.path.join(url, f)):
            if f.endswith(".py") and f != "__init__.py":
                name = f.split(".")[0]
                file.write(automodule(rst_url + "." + name, name))
        else:
            if not f == "__pycache__":
                walk(create_subsection(file, f), url + "/" + f, rst_url + "." + f)


def dir_autogen(file, title, url, rst_url):
    file.write(create_title(title))
    exact_url = "./../../" + url
    walk(file, exact_url, rst_url)


def create_subsection(file, title):
    file.write(bytes(".. toctree::\n\n", "UTF-8"))

    global COUNTER
    COUNTER += 1
    sub_file_name = "subsection" + str(COUNTER)
    file.write(bytes("\t" + sub_file_name + "\n\n", "UTF-8"))

    sub_file = open("rst_files/" + sub_file_name + ".rst", "wb+")

    sub_file.write(create_title(title))

    return sub_file


file = open("rst_files/Autogen.rst", "wb+")

dir_autogen(file, "model", "model", "model")
dir_autogen(file, "view", "view", "view")
dir_autogen(file, "controller", "controller", "controllers")

os.system("make clean")
os.system("make html")
