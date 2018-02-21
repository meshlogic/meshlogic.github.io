.. title: Custom Exposure Node for Blender
.. slug: nodes-exposure
.. date: 2017-02-19 15:00:00 UTC+02:00
.. category: blender/materials
.. tags: mathjax, blender
.. link: 
.. type: text
.. previewimage: teaser.png
.. description:


Exposure value (EV) is indeed essential for every photographer and computer artist. In Blender there is an exposure slider in Color Management allowing us to edit the overall exposure (in EV stops) of the output viewport or render. However, what if we wanted to edit exposure of certain material map in the node editor? Such node is still missing in Blender (2.78), but we can easily create a custom group node for that purpose.

.. figure:: exposure-node.png
    :align: center
    :class: figure-radius

    Custom exposure node for Blender.

.. TEASER_END


Basically, changing exposure value in RGB color space just means multiplication of each color component by a given factor. Exposure value is defined on a 2-base logarithmic scale, so the multiplication factor should be obtained as $2^{EV}$, so

.. math::
    x_{\textrm{EV}} = x\ 2^{\textrm{EV}} \quad \textrm{for} \quad x \in \{R,G,B\}.


We can implement this simple formula for both material and compositor node editor as follows...


.. figure:: exposure-nodesetup.tn.png
    :target: exposure-nodesetup.png
    :align: center
    :class: figure-radius

    Node setup for the custom exposure node.


Download
========

- Download a `blend file <Exposure_Nodes.blend>`_ with exposure nodes for both material and compositor node editor.


