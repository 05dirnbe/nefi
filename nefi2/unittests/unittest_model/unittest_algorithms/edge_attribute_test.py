# -*- coding: utf-8 -*-
import unittest
import networkx as nx
import cv2
from edge_Attribute_filter import AlgBody as Edge_Body
from guo_hall import AlgBody as guo_body
from invert_color import AlgBody as invert_body
from adaptive import AlgBody as adaptive_body
import operator as op


__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}

class Test_Edge_attribute (unittest.TestCase):

    def test_init(self):
        alg = Edge_Body()
        self.assertEqual(alg.name,"Edge attribute filter")
        self.assertEqual(alg.parent, "Graph filtering")

        self.assertEqual(alg.drop_downs[0].name, "Attribute")
        self.assertEqual(alg.drop_downs[0].options,{"width","length"})


        self.assertEqual(alg.drop_downs[1].name, "Operator")
        self.assertEqual(alg.drop_downs[1].options,{"Strictly smaller",
                                                    "Smaller or equal",
                                                    "Equal",
                                                    "Greater or equal",
                                                    "Strictly greater"})

        self.assertEqual(alg.float_sliders[0].name, "Attribute treshold")
        self.assertEqual(alg.float_sliders[0].lower, 0.0)
        self.assertEqual(alg.float_sliders[0].upper, 20.0)
        self.assertEqual(alg.float_sliders[0].step_size, 0.1)
        self.assertEqual(alg.float_sliders[0].value, 10.0)

    def test_set_uiElement(self):
        alg=Edge_Body()

        alg.attribute.set_value("width")
        self.assertEqual(alg.attribute.value,"width")
        alg.attribute.set_value("length")
        self.assertEqual(alg.attribute.value,"length")

        alg.operator.set_value("Strictly smaller")
        self.assertEqual(alg.operator.value,"Strictly smaller")
        alg.operator.set_value("Smaller or equal")
        self.assertEqual(alg.operator.value,"Smaller or equal")
        alg.operator.set_value("Equal")
        self.assertEqual(alg.operator.value,"Equal")
        alg.operator.set_value( "Greater or equal")
        self.assertEqual(alg.operator.value, "Greater or equal")
        alg.operator.set_value("Strictly greater")
        self.assertEqual(alg.operator.value, "Strictly greater")

        alg.attribute_threshold_value.set_value(0.0)
        self.assertEqual(alg.attribute_threshold_value.value,0.0)
        alg.attribute_threshold_value.set_value(5.0)
        self.assertEqual(alg.attribute_threshold_value.value,5.0)
        alg.attribute_threshold_value.set_value(20.0)
        self.assertEqual(alg.attribute_threshold_value.value,20.0)

    def test_process(self):
        alg=Edge_Body()
        alg.attribute.set_value("width")
        alg.operator.set_value("Strictly smaller")

        pp_alg = invert_body()
        sg_alg = adaptive_body()
        gd_alg = guo_body()

        img_array = cv2.imread("p_polycephalum.jpg")
        graph = ""

        pp_alg.process([img_array,graph])
        sg_alg.process([pp_alg.result['img'],pp_alg.result['graph']])
        gd_alg.process([sg_alg.result['img'],sg_alg.result['graph']])

        alg.process([gd_alg.result['img'],gd_alg.result['graph']])

        #should be
        should_graph=gd_alg.result['graph']
        to_be_removed = [(u, v) for u, v, data in
                             should_graph.edges_iter(data=True)
                if op.lt(data["width"],10.0)]
        should_graph.remove_edges_from(to_be_removed)

        self.assertEqual(alg.result['graph'],should_graph)

if __name__ == '__main__':
    unittest.main()
