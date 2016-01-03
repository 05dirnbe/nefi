# -*- coding: utf-8 -*-
"""
A module which contains all necessary information's and features to create
an additional implementation of algorithms.
To contribute an algorithm implementation the contributor is needs to create
a seperate <algorithm_name>.py in the algorithms folder. In <algorithm_name>.py
he needs to create a class "class AlgBody(Algorithm):" which inherits from Algorithm.
In order to give the ext_loader the possibility to dynamically invoke the algorithm
definition, the contributor also needs to override the methods: process(self, image),
get_name(self) and belongs_to(self).
Additional UI input for the algorithm can be specified by creating IntegerSlider, FloatSlider,
CheckBox or DropDown objects. These object instances need to be created by the constructor method
__init__(self) of the algorithm implementation. E.g. we create a IntegerSlider in __init__(self)
by calling the constructor of IntegerSlider and binding it to slider1 with
"slider1 = IntegerSlider(self, "slider1", 0, 10, 1, 0)" (see the IntegerSlider definition
for further information)
"""
__authors__ = {"Dennis Groß": "gdennis91@googlemail.com",
               "Pavel Shkadzko": "p.shkadzko@gmail.com",
               "Philipp Reichert": "prei@me.com"}

from PyQt5.QtCore import QObject, pyqtSlot


class Algorithm(QObject):
    """

    """

    def __init__(self):
        """
        Algorithm class
        Instance vars:
            self.modified -- True if Algorithm settings were modified, true by default
            self.belongs -- A step name to which current algorithm belongs
            self.float_sliders -- a list containing all FloatSlider created by the user
            self.integer_sliders -- a list containing all InterSlider created by the user
            self.checkboxes -- a list containing all Checkboxes created by the user
            self.drop_downs --  a list containing all DropDowns created by the user

        Returns:
            object: instance of the algorithm object
        """
        QObject.__init__(self)
        self.modified = True
        self.integer_sliders = []
        self.float_sliders = []
        self.checkboxes = []
        self.drop_downs = []

    def belongs(self):
        """
        Identifies the category to which this algorithm implementation is associated with.
        Therefore you the contributor returns a string yielding the name of the associated
        category. E.g. we have an algorithm "blur" which is created through implementing
        the abstract class Algorithm. In "blur" we override the belongs method to return
        "preprocessing" to associate the "blur" algorithm instance with the category
        "preprocessing".

        Returns:
            The string identifier to which category this algorithm belongs to
        """
        return "Category_1"

    def process(self, image):
        """
        Contains the logic of the implemented algorithm. While computing
        the pipeline each algorithm will be called with its process method giving the
        output image from the previous algorithm processed in the pipeline.
        The images are used to draw the result of each algorithm in the left section of
        the UI. Therefore the contributor should return an image itself at the end of this
        method.
        By default this method raises an error if the user is not overriding his own process
        method.

        Args:
            image: The input image from the previous category in the pipeline.

        Returns:
            image: The result image of the process method
        """
        raise NotImplementedError

    def get_name(self):
        """
        This method returns the name of the implemented algorithm. E.g. int case the contributor
        is implementing a "watershed" algorithm, his get_name method should return "watershed".
        By default this method raises an error if the user is not overriding his own get_name
        method.

        Returns:
             The name of the algorithm specified in this implementation.
        """
        return "Example Algorithm 1"

    def report_pip(self):
        #todo: implement method
        """
        This method creates a json representation of the implemented algorithm. Therefore it
        looks into the lists containing information of the ui objects created and reports a
        fragment for a json document.
        This method must not be implemented by the contributor to add a new algorithm implementation.

        Returns:
            A json document which contains the definitions of the implemented algorithm

        """
        raise NotImplementedError


class IntegerSlider:
    """
    A class defining a slider of type int to display in the algorithm detail section of the UI.
    After calling the IntegerSlider constructor, the program automatically creates ui widgets as well
    as qt slots and signals to connect this slider with the UI.
    """
    def __init__(self, algorithm_instance, name, lower, upper, step_size, default):
        """

        Args:
            algorithm_instance: The instance of the calling algorithm
            name: The name to be displayed in the UI - label of the slider
            lower: The lower bound of the slider in the UI
            upper: The upper bound of the slider in the UI
            step_size: The amount of a slider step in the UI
            default: The default value for the slider in the UI

        Returns:
            instance of an IntegerSlider object

        """
        self.step_size = step_size
        self.default = default
        self.value = default
        self.lower = lower
        self.upper = upper
        self.name = name
        algorithm_instance.integer_sliders.append(self)

    @pyqtSlot(int)
    def set_value(self, arg1):
        """
        The set_value method is used by the UI and the batch-mode of NEFI as an input
        source of selected values for this particular slider instance.
        The @pyqtSlot(int) decoration declares this method as as QT-Slot. To get more information
        about Slots and Signals in QT read about it in the official QT documentation.

        Args:
            arg1: the integer value selected in the ui or the pipeline in batch-mode

        Returns:

        """
        self.value = arg1


class FloatSlider:
    """
    A class defining a slider of type float to display in the algorithm detail section of the UI.
    After calling the FloatSlider constructor, the program automatically creates ui widgets as well
    as qt slots and signals to connect this slider with the UI.
    """
    def __init__(self, algorithm_instance, name, lower, upper, step_size, default):
        """

        Args:
            algorithm_instance: The instance of the calling algorithm
            name: The name to be displayed in the UI - label of the slider
            lower: The lower bound of the slider in the UI
            upper: The upper bound of the slider in the UI
            step_size: The amount of a slider step in the UI
            default: The default value for the slider in the UI

        Returns:
            instance of an IntegerSlider object

        """
        self.step_size = step_size
        self.default = default
        self.value = default
        self.lower = lower
        self.upper = upper
        self.name = name
        algorithm_instance.float_sliders.append(self)

    @pyqtSlot(float)
    def set_value(self, arg1):
        """
        The set_value method is used by the UI and the batch-mode of NEFI as an input
        source of selected values for this particular slider instance.
        The @pyqtSlot(int) decoration declares this method as as QT-Slot. To get more information
        about Slots and Signals in QT read about it in the official QT documentation.

        Args:
            arg1: the integer value selected in the ui or the pipeline in batch-mode

        Returns:

        """
        self.value = arg1


class CheckBox:
    """
    A class defining a Checkbox of type boolean to display in the algorithm detail section of the UI.
    After calling the CheckBox constructor, the program automatically creates ui widgets as well
    as qt slots and signals to connect this checkbox with the UI.
    """
    def __init__(self, algorithm_instance, name, default):
        """

        Args:
            algorithm_instance: The instance of the calling algorithm
            name: The name of the checkbox to be displayed in the ui
            default: The default value of the checkbox

        Returns:

        """
        self.default = default
        self.value = default
        self.name = name
        algorithm_instance.checkboxes.append(self)

    @pyqtSlot(bool)
    def set_value(self, arg1):
        """
        The set_value method is used by the UI and the batch-mode of NEFI as an input
        source of selected values for this particular checkbox instance.
        The @pyqtSlot(bool) decoration declares this method as as QT-Slot. To get more information
        about Slots and Signals in QT read about it in the official QT documentation.

        Args:
            arg1: the boolean value selected in the ui or the pipeline in batch-mode

        Returns:

        """
        self.value = arg1


class DropDown:
    """
    A class defining a DropDown menu of type string to display in the algorithm detail section of the UI.
    After calling the DropDown constructor, the program automatically creates ui widgets as well
    as qt slots and signals to connect this DropDown with the UI.
    """
    def __init__(self, algorithm_instance, name, options):
        """

        Args:
            algorithm_instance: The instance of the calling algorithm
            name: The name of the DropDown menu to be displayed in the UI
            options: The list of string options a user can select in the Ui for the DropDown

        Returns:

        """
        self.name = name
        self.value = name
        self.options = options
        algorithm_instance.drop_downs.append(self)

    @pyqtSlot(str)
    def set_value(self, arg1):
        """
        The set_value method is used by the UI and the batch-mode of NEFI as an input
        source of selected values for this particular DropDown instance.
        The @pyqtSlot(str) decoration declares this method as as QT-Slot. To get more information
        about Slots and Signals in QT read about it in the official QT documentation.

        Args:
            arg1: the string value selected in the ui or the pipeline in batch-mode

        Returns:

        """
        self.value = arg1


MyAlgorithm_1 = Algorithm()

# name, lower, upper, step_size, default
Slider1 = IntegerSlider(MyAlgorithm_1, "Setting 1", -10, 10, 1, 5)
Slider2 = IntegerSlider(MyAlgorithm_1, "Setting 2", 0, 10, 2, 2)
Slider4 = FloatSlider(MyAlgorithm_1, "Setting 4", -1.0, 2.0, 0.1, 1.2)
Checkbox1 = CheckBox(MyAlgorithm_1, "Checkbox1", True)
DropDown1 = DropDown(MyAlgorithm_1, "DropDown1", ["bla", "blup"])
