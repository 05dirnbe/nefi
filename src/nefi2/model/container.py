# -*- coding: utf-8 -*-
"""
This class is used to receive, keep and send the results of the algorithms
processing. The results will be kept in a simple list object and directly
accessed if required.
"""


class OutContainer:
    def __init__(self):
        self.results = []

    def receive(self, image):
        """Receive a processed image and save it in a list."""
        self.results.append(image)

    def flush(self):
        """Remove all processed image instances from the container."""
        self.results = []

    def get_result(self):
        pass

    def send_result(self):
        pass

