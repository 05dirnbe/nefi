.. _create_pip:

Pipeline Creation
=================

In order to create a new **Pipeline** you're advised to use NEFI2 pipeline panel.
This will guarantee that you won't make any syntax errors.
However if you still want to do it manually here is a quick overview.

The pipeline files are stored in **default_pipelines/** directory.
You can keep your pipeline json files anywhere you want, but if you put them in **default_pipelines/** they will be loaded automatically at startup.

Pipeline Syntax Example
+++++++++++++++++++++++

::

  [
    ["Watershed DE Adaptive",{"Foreground Iteration":0,
                              "Background Iteration":0,
                              "Threshold Block Size":11,
                              "Threshold Constant":1,
                              "type":"Segmentation",
                              "store_image":false}],

    ["Median Blur",{"channel1":true,
                    "channel2":true,
                    "channel3":true,
                    "kernelsize":2,
                    "type":"Preprocessing",
                    "store_image":false}],

    ["Guo Hall",{"store_image":false,
                 "type":"Graph Detection"}],

    ["Keep only LCC",{"store_image":false,
                      "type":"Graph Filtering"}],

    ["Simple Cycle",{"store_image":false,
                     "type":"Graph Filtering"}]
  ]


The order of the **Algorithms** ``["Guo Hall", ...], ["Keep only LCC", ...]`` is important, however the order of the settings slot-value pairs ``"kernelsize":2`` is not.
If the pipeline is correct it will be loaded, otherwise nothing will be added to the **Pipeline** panel and you'll have need to revise your json file.

