import os

"clean old rst files"
os.system("del /q CodeContent\GeneratedModel\*")
os.system("del /q CodeContent\GeneratedView\*")
os.system("del /q CodeContent\GeneratedController\*")

"create rst files for selected folders"
os.system("sphinx-apidoc -o ./CodeContent/GeneratedModel ../../model/")
os.system("sphinx-apidoc -o ./CodeContent/GeneratedView ../../view/")
os.system("sphinx-apidoc -o ./CodeContent/GeneratedController ../../controller/")

os.system("make clean")
os.system("make html")

