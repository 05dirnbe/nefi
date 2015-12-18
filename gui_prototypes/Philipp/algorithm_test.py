from PyQt5.QtCore import QObject, pyqtSlot


class Algorithm(QObject):
    def __init__(self):
        """
        Algorithm class
        Instance vars:
            self.modified -- True if Algorithm settings were modified
            self.belongs -- A step name to which current algorithm belongs

        Returns:
            object:
        """
        QObject.__init__(self)
        self.modified = True
        self.integer_sliders = []
        self.float_sliders = []
        self.checkboxes = []

    def belongs(self):
        """Return a step name to which current algorithm belongs."""
        raise NotImplementedError

    def process(self, image):
        """
        A user must override this method in order to comply with the interface.

        Args:
            image:
        """
        raise NotImplementedError

    def get_name(self):
        return "Example Algorithm"

    def report_pip(self):
        raise NotImplementedError


class IntegerSlider:
    def __init__(self, algorithm_instance, name, default, lower, upper):
        self.default = default
        self.value = default
        self.lower = lower
        self.upper = upper
        self.name = name
        algorithm_instance.integer_sliders.append(self)

    @pyqtSlot(int)
    def set_value(self, arg1):
        self.value = arg1


class FloatSlider:
    def __init__(self, algorithm_instance, name, default, lower, upper):
        self.default = default
        self.value = default
        self.lower = lower
        self.upper = upper
        self.name = name
        algorithm_instance.float_sliders.append(self)

    @pyqtSlot(float)
    def set_value(self, arg1):
        self.value = arg1


class CheckBox:
    def __init__(self, algorithm_instance, name, default):
        self.default = default
        self.value = default
        self.name = name
        algorithm_instance.checkboxes.append(self)

    @pyqtSlot(bool)
    def set_value(self, arg1):
        self.value = arg1


MyAlgorithm = Algorithm()
Slider1 = IntegerSlider(MyAlgorithm, "Setting 1", 10, -10, 20)
Slider2 = IntegerSlider(MyAlgorithm, "Setting 2", 1, -10, 20)
Slider3 = IntegerSlider(MyAlgorithm, "Setting 3", 100, -1, 200)
Slider4 = IntegerSlider(MyAlgorithm, "Setting 4", 1.2, -2.1, 4.0)
