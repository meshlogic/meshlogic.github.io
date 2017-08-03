.. title: HSL Color Model Decomposition in Blender
.. slug: nodes-hsl-color-model
.. date: 2016-08-29 18:00:00 UTC+02:00
.. category: blender
.. tags: mathjax, blender-materials
.. link: 
.. description:
.. type: text


In the current version, Blender contains decomposition nodes only for **HSV** and **RGB** color models, but still missing nodes for **HSL** color model. Since I find the HSL model very useful for color manipulations, especially its **lightness** value, I've created both **Separate HSL** and **Combine HSL** nodes, which enables me to modify each part of the HSL model.

.. figure:: hsl_hsv_models.png
    :align: center


.. TEASER_END


Both HSL and HSV(HSB) models represent a color in cylindrical coordinates. **HSL** stands for *hue*, *saturation*, and *lightness*, while **HSV(HSB)** stands for *hue*, *saturation*, and *value(brightness)*. So, the difference is in representation of lighter/darker tones as visible from the picture.



HSL Nodes for Cycles Render
===========================

Basically we need to create two custom nodes. One for separating the input color into 3 parts of the HSL model, and another node for combining these parts into the color output.

.. figure:: hsl_nodes.png
    :align: center
    :class: figure-radius


Separate HSL Node
-----------------

Because of the fact Blender already contains HSV nodes, we can use conversion from HSV to HSL model:

.. math::
    H_\mathrm{HSL} & = H_\mathrm{HSV} \\
    S_\mathrm{HSL} & = \frac{V S_\mathrm{HSV}}{1 - |2 L - 1|} \\
    L & = V (1 - \frac{S_\mathrm{HSV}}{2} )


This is how it looks like implemented in Blender's node editor using its essential nodes.

.. figure:: separate_hsl.tn.png
    :target: separate_hsl.png
    :align: center
    :class: figure-radius


Combine HSL Node
----------------

To combine parts of the HSL color model back into the output color, we can utilize the conversion from HSL to HSV:


.. math::
    H_\mathrm{HSV} & = H_\mathrm{HSL} \\
    S_\mathrm{HSV} & = 2 \frac{V-L}{V} \\
    V & = L + \frac{S_\mathrm{HSL} (1 - |2 L - 1|)}{2} \\


.. figure:: combine_hsl.tn.png
    :target: combine_hsl.png
    :align: center
    :class: figure-radius

|

Time for some procedurally generated art :)
===========================================

Recently, I have played with procedurally generated patterns like **Voronoi diagram**. I connected them together and used that pattern to modify the saturation and lightness value of the HSL color model.

.. figure:: procedural_art_nodes.tn.png
    :target: procedural_art_nodes.png
    :align: center
    :class: figure-radius


And finally, you can see what I've received :)

.. figure:: procedural_art_01.tn.png
    :target: procedural_art_01.png
    :align: center
    :class: thumbnail


References
    - Here you can download my HSL nodes - http://www.blendswap.com/blends/view/78846
    - `HSL and HSV <https://en.wikipedia.org/wiki/HSL_and_HSV>`_
    - `Voronoi diagram <https://en.wikipedia.org/wiki/Voronoi_diagram>`_
