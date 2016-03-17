# -*- coding: utf-8 -*-
"""
A module which contains all necessary information's and features to create
an additional implementation of algorithms.
To contribute an algorithm implementation the contributor is needs to create
a seperate <algorithm_name>.py in the algorithms folder. In <algorithm_name>.py
he needs to create a class "class AlgBody(Algorithm):" which inherits from
Algorithm.
In order to give the ext_loader the possibility to dynamically invoke the
algorithm definition, the contributor also needs to override the
methods: process(self, image), get_name(self) and belongs_to(self).
Additional UI input for the algorithm can be specified by creating
IntegerSlider, FloatSlider, CheckBox or DropDown objects. These object
instances need to be created by the constructor method __init__(self) of the
algorithm implementation. E.g. we create a IntegerSlider in __init__(self)
by calling the constructor of IntegerSlider and binding it to slider1 with
"slider1 = IntegerSlider(self, "slider1", 0, 10, 1, 0)" (see the IntegerSlider
definition for further information)
"""
import collections
from PyQt5.QtCore import QObject, pyqtSlot

__authors__ = {"Dennis Groß": "gdennis91@googlemail.com",
               "Pavel Shkadzko": "p.shkadzko@gmail.com",
               "Philipp Reichert": "prei@me.com"}


class Algorithm:

    def __init__(self):
        """
        Public Attributes:
            | *modified*: True if Algorithm settings were modified,
                true by default
            | *belongs*: A step name to which current algorithm belongs
            | *float_sliders*: a list containing all FloatSlider created
                by the user
            | *integer_sliders*: a list containing all InterSlider
                created by the user
            | *checkboxes*: a list containing all Checkboxes
                created by the user
            | *drop_downs*:  a list containing all DropDowns
                created by the user
            | *result*: a tuple containing all resulting data produced or
                modified by the algorithm
            | *store_image*: this flag is per default false and indicates if the
                calculated image from this algorithm should be stores at the
                default location after processing.
            | *icon* (str): Path to custom icon to be used for this algorithm.

        Returns:
            | *object*: instance of the algorithm object

        """
        # QObject.__init__(self)
        self.modified = True
        self.integer_sliders = []
        self.float_sliders = []
        self.checkboxes = []
        self.drop_downs = []
        self.name = ""
        self.icon = "./assets/images/missing.png"
        self.parent = ""
        self.result = {"img": None, "graph": None}
        self.store_image = False

    def belongs(self):
        """
        Identifies the category to which this algorithm implementation is assoc
        iated with. Therefore you the contributor returns a string yielding the
        name of the associated category. E.g. we have an algorithm "blur" which
        is created through implementing the abstract class Algorithm. In "blur"
        we override the belongs method to return "preprocessing" to associate
        the "blur" algorithm instance with the category "preprocessing".

        Returns:
            | *self.parent*: The string identifier to which category this
            algorithm belongs to
        """
        return self.parent

    def process(self, input_data):
        """
        Contains the logic of the implemented algorithm. While computing
        the pipeline each algorithm will be called with its process method
        giving the output image from the previous algorithm processed in
        the pipeline The images are used to draw the result of each algorithm
        in the left section of the UI. Therefore the contributor should return
        an image itself at the end of this method.
        By default this method raises an error if the user is not overriding
        his own process
        method.

        Args:
            | *input_data*: a tuple which contains all relevant arguments found in
            the results of the previous processed algorithm. As common in the
            pipeline pattern, the successors always get called with the
            information the predecessor created.
            The first element in input_data should always be image array,
            the second element is reserved for graph. This is why algorithm
            process methods operate on args indeces (args[0] or args[1]).
            Please consider this in case you decide to add an algorithm which
            produces something different than an image array or networkx graph
            object.
        """
        raise NotImplementedError

    def get_name(self):
        """
        This method returns the name of the implemented algorithm. E.g. int case the contributor
        is implementing a "watershed" algorithm, his get_name method should return "watershed".
        By default this method raises an error if the user is not overriding his own get_name
        method.

        Returns:
             | *self.name*: The name of the algorithm specified in this implementation.
        """
        if self.name:
            return self.name
        else:
            raise NotImplementedError

    def set_icon(self, icon_path):
        """
        Args:
            | *icon_path*: The path to the icon to be used
        """

        self.icon = icon_path

    def get_icon(self):
        """
        Returns:
            | *icon_path*: The path to the icon to be used
        """

        return self.icon

    def report_pip(self):
        """
        This method returns a dictionary which contains all relevant algorithm
        information and returns it to the pipeline along with the algorithm
        name. The pipeline needs this information to create a json
        representation of the algorithm. It will encode the dic as following:
        E.g. blur : {"type" : "preprocessing", "kernelsize" : 2.5}
        The encoding of the dic to json will be done by the pipeline which
        collects the dictionary of each algorithm in the processing list.

        Returns:
            | *self.name, collections.OrderedDict* (list): A tuple consisting
              of the name of the algorithm and the dic containing all relevant
              information about the algorithm which need to be stored on the
              filesystem for the pipeline.json.

        """
        list = [["type", self.parent], ["store_image", self.store_image]]

        for int_slider in self.integer_sliders:
            list.append([int_slider.name, int_slider.value])

        for float_slider in self.float_sliders:
            list.append([float_slider.name, float_slider.value])

        for checkbox in self.checkboxes:
            list.append([checkbox.name, checkbox.value])

        for dropdown in self.drop_downs:
            list.append([dropdown.name, dropdown.value])

        return self.name, collections.OrderedDict(list)

    def unset_modified(self):
        """
        Set modified to False
        """
        self.modified = False

    def set_modified(self):
        """
        Set modified to True
        """
        self.modified = True

    @pyqtSlot(bool)
    def set_store_image(self, state):
        self.store_image = state

    def find_ui_element(self, name):
        """
        This method helps the json parser to find the ui elements
        with the given name

        Args:
            |name: name of the ui element we are looking for

        Returns:

        """
        for int_slider in self.integer_sliders:
            if int_slider.name == name:
                return int_slider

        for float_slider in self.float_sliders:
            if float_slider.name == name:
                return float_slider

        for checkbox in self.checkboxes:
            if checkbox.name == name:
                return checkbox

        for dropdown in self.drop_downs:
            if dropdown.name == name:
                return dropdown

        raise FileNotFoundError("could not find ui element: " + name)


class IntegerSlider:
    """
    A class defining a slider of type int to display in the algorithm detail
    section of the UI. After calling the IntegerSlider constructor, the program
    automatically creates ui widgets as wellas qt slots and signals to connect
    this slider with the UI.
    """

    def __init__(self, name, lower, upper, step_size, default):
        """
        Args:
            | *name*: The name to be displayed in the UI - label of the slider
            | *lower*: The lower bound of the slider in the UI
            | *upper*: The upper bound of the slider in the UI
            | *step_size*: The amount of a slider step in the UI
            | *default*: The default value for the slider in the UI

        Returns:
            instance of an IntegerSlider object
        """
        self.step_size = step_size
        self.default = default
        self.value = default
        self.lower = lower
        self.upper = upper
        self.name = name

    @pyqtSlot(int)
    def set_value(self, arg1):
        """
        The set_value method is used by the UI and the batch-mode of NEFI as
        an input source of selected values for this particular slider instance.
        The @pyqtSlot(int) decoration declares this method as as QT-Slot.
        To get more information about Slots and Signals in QT read about it in
        the official QT documentation.

        Args:
            | *arg1*: the integer value selected in the ui or the pipeline in
            batch-mode
        """

        if arg1 > self.upper or arg1 < self.lower:
            raise AssertionError("Given parameter " + str(arg1)  +" for " + str(self.name) + " setting is outside range. [" + str(self.lower) + ", " + str(self.upper) + "]")

        self.value = arg1


class FloatSlider:
    """
    A class defining a slider of type float to display in the algorithm detail
    section of the UI. After calling the FloatSlider constructor, the program
    automatically creates ui widgets as well as qt slots and signals to connect
    this slider with the UI.
    """

    def __init__(self, name, lower, upper, step_size, default):
        """
        Args:
            | *name*: The name to be displayed in the UI - label of the slider
            | *lower*: The lower bound of the slider in the UI
            | *upper*: The upper bound of the slider in the UI
            | *step_size*: The amount of a slider step in the UI
            | *default*: The default value for the slider in the UI

        Returns:
            instance of an IntegerSlider object
        """
        self.step_size = step_size
        self.default = default
        self.value = default
        self.lower = lower
        self.upper = upper
        self.name = name

    @pyqtSlot(float)
    def set_value(self, arg1):
        """
        The set_value method is used by the UI and the batch-mode of NEFI as an
        input source of selected values for this particular slider instance.
        The @pyqtSlot(int) decoration declares this method as as QT-Slot.
        To get more information about Slots and Signals in QT read about it in
        the official QT documentation.

        Args:
            | *arg1*: the integer value selected in the ui or the pipeline in
            batch-mode
        """

        if arg1 > self.upper or arg1 < self.lower:
            raise AssertionError("Given parameter " + str(arg1)  +" for " + str(self.name) + " setting is outside range. [" + str(self.lower) + ", " + str(self.upper) + "]")

        self.value = arg1


class CheckBox:
    """
    A class defining a Checkbox of type boolean to display in the algorithm
    detail section of the UI. After calling the CheckBox constructor, the
    program automatically creates ui widgets as well as qt slots and signals to
    connect this checkbox with the UI.
    """

    def __init__(self, name, default):
        """
        Args:
            | *name*: The name of the checkbox to be displayed in the ui
            | *default*: The default value of the checkbox
        """
        self.default = default
        self.value = default
        self.name = name

    @pyqtSlot(bool)
    def set_value(self, arg1):
        """
        The set_value method is used by the UI and the batch-mode of NEFI as an
        input source of selected values for this particular checkbox instance.
        The @pyqtSlot(bool) decoration declares this method as as QT-Slot. To
        get more information about Slots and Signals in QT read about it in the
        official QT documentation.

        Args:
            | *arg1*: the boolean value selected in the ui or the pipeline in
            batch-mode
        """
        self.value = arg1


class DropDown:
    """
    A class defining a DropDown menu of type string to display in the algorithm
    detail section of the UI. After calling the DropDown constructor, the
    program automatically creates ui widgets as well as qt slots and signals to
    connect this DropDown with the UI.
    """

    def __init__(self, name, options, default=None):
        """
        Args:
            | *name*: The name of the DropDown menu to be displayed in the UI
            | *options*: The list of string options a user can select in the Ui for
            | *default*: Optional: The default value
            the DropDown
        """
        self.name = name
        self.options = options
        self.default = default
        if default is not None:
            self.value = default
        else:
            self.value = list(options)[0]

    @pyqtSlot(str)
    def set_value(self, arg1):
        """
        The set_value method is used by the UI and the batch-mode of NEFI as an
        inputsource of selected values for this particular DropDown instance.
        The @pyqtSlot(str) decoration declares this method as as QT-Slot. To
        get more information about Slots and Signals in QT read about it in the
        official QT documentation.

        Args:
            | *arg1*: the string value selected in the ui or the pipeline in
            batch-mode
        """

        if arg1 not in self.options:
            raise AssertionError("Given parameter " + str(arg1)  +" for " + str(self.name) + " setting is no valid option.")

        self.value = arg1
