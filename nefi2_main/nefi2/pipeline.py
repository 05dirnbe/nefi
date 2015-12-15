# -*- coding: utf-8 -*-
"""
This class represents a central control mechanism over a sequential
image processing pipeline. It controls all the available image processing
steps, handles processing results and works as an mediator between the
algorithms and UI.
"""

__author__ = "p.shkadzko@gmail.com"


import os
import xml.etree.ElementTree as et
from model.steps._step import Step
import sys


class Pipeline:
    def __init__(self, steps):
        """
        Pipeline constructor
        Params:
            steps -- OrderedDict of step names and their instances
        Instance vars:
            self.available_steps -- dict of {Step name: Step}
            self.executed_steps -- a list of Steps
            self.pipeline_path -- a path to a saved pipelines
            self.image_path -- a path to an image file
        """
        self.available_steps = steps
        self.executed_steps = [v for v in self.available_steps.values()]
        self.pipeline_path = 'saved_pipelines'  # default dir
        self.image_path = None

        ### debugging
        # for k,v in self.available_steps.items():
        #    print(k,v)

    def new_step(self, name, position):
        """
        Create an instance of a new Step.
        Params:
            name -- a step name
            position -- a step index in self.executed_steps
        Returns
            True
        """
        self.executed_steps.insert(position, Step(name))
        return True

    def move_step(self, origin_pos, destination_pos):
        return False

    def delete_step(self, position):
        return False

    def process(self):
        pass

    def change_algorithm(self, position, alg_name):
        """
        Set the algorithm of the step in position to modified = True
        Params:
            position -- list index of the step in the pipeline
            alg_name -- algorithm name
        Returns True
        """
        for v in self.executed_steps[position].available_algs.values()[0]:
            if alg_name == v.Body().get_name():
                v.Body().set_modified()
        return True

    def get_executed_steps(self):
        """
        Returns:
            list of strings
        """
        pass

    def get_algorithm_list(self, position):
        """
        Get names of all available algorithms for the step in position.
        Returns:
            alg_names -- a list of algorithm names
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
