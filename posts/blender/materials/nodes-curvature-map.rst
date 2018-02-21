.. title: A More Comfortable Node Setup For Curvature Map
.. slug: nodes-curvature-map
.. date: 2018-08-24 16:00:00 UTC+02:00
.. category: blender/materials
.. tags: mathjax, blender-materials
.. link: 
.. type: text
.. previewimage: teaser.png
.. description: Lighting your scene with a HDRI (HDR) environment map is a great method how to improve quality of your renders.


.. default-role:: code


.. figure:: curvature-map_convexity.tn.png
    :target: curvature-map_convexity.png
    :align: right
    :figclass: thumbnail

    Convexity map detecting edges in the mesh geometry.


When creating **smart materials**, information about the mesh curvature is necessary. It's well known that Blender already has a node with the **Pointiness** attribute, but I've found the output of this node rather difficult to use as it is. There are many published tutorials using this pointiness node with a color ramp or few math nodes to increase contrast, but still I've been trying to find a more comfortable approach how to remap the pointiness value.

.. TEASER_END

I wanted to have a node with easy to use controls, allowing to adjust sharpness and thickness of edges and cavities in the curvature map while keeping its mean (grey) value constant. For that purpose, I've created a node for remapping the pointiness value and a custom color ramp node. Because it woks quite well for me, I thought I could share it with you :)


.. Note::

    * **Pointiness** attribute in Blender gives an approximation of the mesh curvature on the **per-vertex** basis. It means it works well only for dense meshes, so you might need to increase polygon density by some SubSurf modifiers. Any **per-pixel** attribute is not implemented in Blender yet.

    * Cavity Map





.. admonition:: Moot Support

   Moot doesn't support comment counts on index pages, and it requires adding
   this to your ``conf.py``:

..


    Note that the **Pointiness** attribute in Blender gives an approximation of the mesh curvature on the **per-vertex** basis. It means it works well only for dense meshes, so you might need to increase polygon density by some SubSurf modifiers. Any **per-pixel** attribute is not implemented in Blender yet.




Curvature Map - Remapping the Pointiness Value
==============================================

To adjust the sharpness of edges in the curvature map, we can try to rise the pointiness value to the power of $n$ as follows

.. math::
    x_{out} = c (x_{in}) ^ n,

where $x_{in}$, the pointiness value produced by Blender varies around its mean value 0.5. To ensure that the output value $x_{out}$ will also vary around a constant mean value, we need to find the corresponding multiplication factor $c$. By applying logarithm function to the equation we get

.. math::
    c = 10^{ \log x_{out} - n \log x_{in} }.


Implemented with nodes it looks like this:

.. figure:: curvature-map_nodesetup.tn.png
    :target: curvature-map_nodesetup.png
    :align: center
    :class: figure-radius

    Node setup for the Curvature Map node with the Convexity and Concavity output.

And finally, the Curvature group node. Note that to get 0.5 grey color in the viewport, we need to set the $x_{out}$ mean value to 0.214 because of the sRGB conversion in Blender, but you can set whatever mean value suits you.

.. figure:: curvature-map_node.png
    :align: center
    :class: figure-radius

    Curvature Map group node. 


Edge Mask - Combine Convexity Map and a Grunge Texture
======================================================





