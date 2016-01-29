import unittest
import sys, os
from ext_loader import ExtensionLoader
from pipeline import Pipeline

import nefi2

__author__ = {'Dennis Groß': 'gdennis91@googlemail.com'}

sys.path.insert(0, os.path.join(os.curdir, '../nefi2'))


def get_assets_resource_path_image(name):
    return os.path.join(os.path.abspath("../../assets/images/"), name)


def get_assets_resource_path_pipelines(name):
    return os.path.join(os.path.abspath("../../assets/json/"), name)


def get_batch_mode_output_path():
    return os.path.abspath("../batch_mode_output/")


def run_batch_mode(pipeline_name, image_name):
    ext_loader = ExtensionLoader()
    pipeline = Pipeline(ext_loader.cats_container)

    pipeline_url = get_assets_resource_path_pipelines(pipeline_name)
    image_url = get_assets_resource_path_image(image_name)
    directory = os.path.join(get_batch_mode_output_path(),
                             image_name.split(".")[0] + "_" + pipeline_name.split(".")[0])

    pipeline.load_pipeline_json(pipeline_url)

    pipeline.set_input(image_url)

    if not os.path.exists(directory):
        os.makedirs(directory)

    pipeline.set_output_dir(directory)

    pipeline.process()


class ParserTests(unittest.TestCase):
    def test_batch_easy(self):
        run_batch_mode("pip1.json", "input.jpeg")


if __name__ == '__main__':
    pass
