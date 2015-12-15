from PyQt5.QtCore import QObject, pyqtSlot
import sys

class Algorithm(QObject):

    integer_slot = pyqtSlot()
    float_slot = pyqtSlot()
    boolean_slot = pyqtSlot()

    @integer_slot(int)
    def kernelsize(self, slidervalue):
        pass

    def kernelsize_upper(self):
        return 5

    def kernelsize_lower(self):
        return 0

    def kernelsize_default(self):
        return 0
