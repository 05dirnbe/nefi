# -*- coding: utf-8 -*-
"""
This class represents a central control mechanism over a sequential
image processing pipeline. It controls all the available image processing
steps, handles processing results and works as an mediator between the
algorithms and UI.
"""

import xml.etree.ElementTree as et


__author__ = "p.shkadzko@gmail.com"


class Pipeline:
    def __init__(self, steps, default_settings):
        """
        Pipeline constructor
        Params:
        Instance vars:
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



if __name__ == '__main__':
    pass
