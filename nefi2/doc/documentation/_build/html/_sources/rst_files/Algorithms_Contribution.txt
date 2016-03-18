Algorithms Creation
===================

As previously mentioned, NEFI2 is not just a pipeline of hardcoded **Categories** and **Algorithms** which execute one single task.
It can be customized and extended such that it is no longer a Graph extraction but an image reduction and enchancement pipeline.
This all means that you can add new **Algorithms** or new **Categories** (see :ref:`add_cats`) with ease.

Say, you want to move (redefine) some **Algorithm** to any other **Category**.
You only need to change one line in, for example "Blur" algorithm ``__init__(self)`` constructor, from ``self.parent = "Preprocessing"`` to ``self.parent = "Segmentation"``.
Then next time you start NEFI2, "Blur" will appear in *Segmentation* category.

If you want to rename the **Algorithm**, change ``self.name == "Blur"`` to something you prefer more (don't forget to adjust your saved json pipelines as well, see :ref:`create_pip`).

Here is a small tutorial that describes the process of adding a new **Algorithm**.

Tutorial
--------

Imagine you decided to add an algorithm that reduces an image.
You've looked up in `OpenCV <http://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#resize>`_ how to do it and wrote a small test function.
::

    def resize(img, ratio):
        """
        Args
            |*img* (ndarray): image array
            |*ratio* (float): % amount to reduce
        """
        ratio = 1 - (ratio / 100)
        small = cv2.resize(img, (0,0), fx=ratio, fy=ratio, interpolation=cv2.INTER_AREA)
        return small

What's next?

**1.** Goto ``model/algorithms`` directory and create a new file, for example **reduce_img.py**.

**2.** Copy-paste the default **Algorithm** header code below.

::

    #!/usr/bin/env python3
    import cv2
    from _alg import *


    class AlgBody(Algorithm):
        def __init__(self):
            Algorithm.__init__(self)
            self.name = ""
            self.parent = ""

        def process(self, args):
            pass


    if __name__ == '__main__':
        pass

Here you basically created and empty dummy **Algorithm** which won't be included in NEFI2 until it gets a ``self.name`` and a ``self.parent`` -- this variable tells NEFI2 which **Category** does the **Algorithm** belong to.

**3.** Define the **Algorithm** name and the parent **Category**.
::

    self.name = "Image Reduce"
    self.parent = "Preprocessing"

Now, you need to decide whether your custom **Algorithm** has any settings that you want to adjust.
We want to define a value of how much the image can be reduced %-wise.
This will be a float number between 1 (1%) and 100 (100%).
In order to display this type of setting in the UI we use a small collection of QT widgets:

	* :class:`_alg.IntegerSlider`.
	* :class:`_alg.FloatSlider`.
	* :class:`_alg.CheckBox`.
	* :class:`_alg.DropDown`.

We also use a list of containers for these widgets:

    * :class:`self.integer_sliders`
    * :class:`self.float_sliders`
    * :class:`self.checkboxes`
    * :class:`self.drop_downs`

**4.** Import :class:`_alg.IntegerSlider` and add it to your **Algorithm** constructor.
Add the necessary default values.
Each QT widget has a list of fixed number of default settings ``(name, lower, upper, step_size, default)`` that
NEFI2 uses when you first select the **Algorithm** in the UI.
Specify them: ``self.ratio = IntegerSlider("Reduction ratio", 1, 100, 1, 50)``.
And finally add your QT widget to predefined ``self.integer_sliders`` container: ``self.integer_sliders.append(self.ratio)``

**5.** Rename your ``resize()`` function to ``process(self)``.
You can leave your function as it is, of course, but ``process(self)`` must be present and handle the results of your ``resize()`` function accrodingly.
Function ``process()`` is called by NEFI2 on your image data and saves the results of the **Algorithm** in a special variable ``self.result = {"img": None, "graph": None}``.
Make sure you have the results of your algorithm correctly assigned to this variable otherwise your algorithm won't work::

    def process(self, args):
        """
        Args
            |*img* (ndarray): image array
            |*ratio* (float): % amount to reduce [0-1]

        """
        smaller = cv2.resize(args[0], (0, 0), fx=ratio, fy=ratio,
                             interpolation=cv2.INTER_AREA)
        self.result['img'] = smaller

You might have noticed another small difference.
We replaced initial ``resize(img, ratio)`` params with ``process(args)``.
Basically **args** represents our ``self.result`` variable only it is a list here, **args** first element is an image array and second is a graph (may not be present).
In this function we are working with image arrays so we access it as **args[0]**.
Imagine that the **Pipeline** processes one array with various algorithms.
These algorithms all must know exactly where the results of the previous algorithm are kept.
That is why we need to adhere to this small *interface* requirement.

Here is the final code for your custom **Algorithm**.
::

    #!/usr/bin/env python3
    """
    Tutorial Algorithm
    Reduce image size using predefined ratio value.
    """

    import cv2
    from _alg import Algorithm, IntegerSlider


    class AlgBody(Algorithm):
        """OpenCV image size reduction implementation"""
        def __init__(self):
            Algorithm.__init__(self)
            self.name = "Image Reduce"
            self.parent = "Preprocessing"
            self.ratio = IntegerSlider("Reduction %", 1, 100, 1, 50)
            self.integer_sliders.append(self.ratio)

        def process(self, args):
            """
            Args
                |*img* (ndarray): image array

            """
            ratio = 1 - (self.ratio.value / 100)
            smaller = cv2.resize(args[0], (0, 0), fx=ratio, fy=ratio,
                                 interpolation=cv2.INTER_AREA)
            self.result['img'] = smaller


    if __name__ == '__main__':
        pass

Now, time to test it!

.. figure::  images/tutorial1.png
   :align:   center
   :scale: 85%

As you can see, it worked nicely.
This was a rather simple example and probably your algorithms will be far more advanced.
If you get stuck, you can always check with the code of the existing algorithms.
