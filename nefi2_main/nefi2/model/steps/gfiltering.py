# -*- coding: utf-8 -*-
from _step import Step


class StepBody(Step):
    def __init__(self):
        self.name = 'Graph filtering'
        # we need Step to load its algorithms after self.name assignment
        Step.__init__(self)


if __name__ == '__main__':
    pass
