# -*- coding: utf-8 -*-
"""
This class represents a central control mechanism over a sequential
image processing pipeline. It controls all the available image processing
steps, handles processing results and works as an mediator between the
algorithms and UI.
"""

__author__ = "p.shkadzko@gmail.com"


import xml.etree.ElementTree as et


class Pipeline:
    def __init__(self, steps):
        """
        Pipeline constructor
        Params:
            steps --

        Instance vars:
            self.available_steps -- dict of {Step name: Step}
            self.executed_steps -- a list of Steps
            pipeline_path -- a path to a saved pipeline
            image_path -- a path to an image file
        """
        pass

    def new_step(self, position):
        return False

    def change_step(self, position, step_type):
        return False

    def move_step(self, origin_pos, destiantion_pos):
        return False

    def delete_step(self, position):
        return False

    def process(self):
        pass

    def change_algorithm(self, position, alg_type):
        return False

    def get_executed_steps(self):
        """
        Returns:
            list of strings
        """
        pass

    def get_algorithm_list(self, position):
        """
        Returns:
            list of strings
        """
        pass


    def read_pipeline_xml(self, xml_file):
        """
        Parse the xml file of a saved pipeline.
        Create and return a dictionary representation of the xml file.
        Params:
            xml_file -- a path to an xml file of a saved pipeline
        Returns:
            settings dictionary {Step: {Algorithm: {Param: val}}}
        """
        tree = et.parse(xml_file)
        root = tree.getroot()
        for elem in root:
            if elem.tag == 'pipeline':
                # create settings dictionary
                settings = {}
                for step in elem.iter('step'):
                    step_name = step.attrib['name']
                    settings[step_name] = {}
                    for alg in step.iter('alg'):
                        alg_name = alg.attrib['name']
                        settings[step_name].update({alg_name: {}})
                        for param in alg.iter('param'):
                            params = {param.attrib['name']: param.text}
                            settings[step_name][alg_name].update(params)
        return settings

    def read_image(self, img_path):
        pass

    def save_pipeline_xml(self, save_path):
        pass


if __name__ == '__main__':
    pass
