import unittest
import sys, os
from ext_loader import ExtensionLoader
from pipeline import Pipeline

import nefi2

__author__ = {'Dennis Groß': 'gdennis91@googlemail.com'}

sys.path.insert(0, os.path.join(os.curdir, '../nefi2'))


def get_assets_resource_path(name):
    return os.path.join(os.path.abspath("../../assets/"), name)


def get_batch_mode_output_path():
    return os.path.abspath("../batch_mode_output/")


def run_batch_mode(pipepline_name, image_name):
    extloader = ExtensionLoader()
    pipeline = Pipeline(extloader.cats_container)

    pipeline.load_pipeline_json(get_assets_resource_path(pipepline_name))
    pipeline.set_output_dir(get_batch_mode_output_path())
    pipeline.get_image(get_assets_resource_path(image_name))
    pipeline.process()


class ParserTests(unittest.TestCase):
    def test_batch_easy(self):
        run_batch_mode("pip1.json", "input.jpeg")

if __name__ == '__main__':
    pass
