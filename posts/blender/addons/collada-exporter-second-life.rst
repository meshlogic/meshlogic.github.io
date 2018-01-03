.. title: Collada Exporter for Second Life - Blender Addon
.. slug: collada-exporter-second-life
.. date: 2017-05-17 15:00:00 UTC+02:00
.. category: blender
.. tags: blender-addons
.. link: 
.. description:
.. type: text

.. TEASER_END


This python script is a replacement for the Blender's native Collada exporter made in C++. The main goal was to fix issues related to exporting static mesh objects including textures to the Second Life grid. Also, thanks to the python, this exporter can be easily modified/maintained without the need to go into Blender's source code and recompiling Blender.


.. figure:: ui-panel.png
    :align: right
    :class: figure-round


Motivation
================

Recently, I've noticed that the default Collada exporter in Blender (2.78) has some problems to export textured objects for usage in Second Life. Particularly, I've reported these two issues:


.. class:: li-smallskip

    - `Collada exporter assigns the same texture to all objects when they share the same material <https://developer.blender.org/T51259>`_

    - `Collada exporter does not assign any texture when object has multiple UV maps <https://developer.blender.org/T51288>`_

These issues prevent to quickly upload larger scenes (like a whole house) including all baked textures to SL and you need to apply textures by hand after upload, which is time wasting especially when you do many uploads to test your builds.

I wanted to try to fix these issues. But alas the default Collada exporter is made in C++ and I didn't want to recompile whole Blender. So, I decided to write my own Python based exporter that would work as an addon.


Features
===========

.. class:: li-smallskip

    - Export static mesh objects to Collada (.dae), including images assigned to the active UV layer.

    - Export normals according the Auto-Smooth mesh option. Works also with face weighted normals.

    - Tested with Firestorm Viewer for Second Life.

    - Requires python collada module https://github.com/pycollada/pycollada. Pycollada is not a part of official Blender, so must be installed into Blender's folder (eg. Blender/2.78/scripts/modules)



ChangeLog
===========

Version 0.3 (30.11.2017)
    - Remove model tags (PHY, LOD1, LOD2, etc) from material id names
    - Export normals according the Auto-Smooth mesh option
    - Added more shading options

Version 0.2 (17.05.2017)
    - Objects (geometry nodes) are sorted by name now

Version 0.1 (12.05.2017)
    - Initial release



Download
========


.. - `From my GitHub <https://github.com/meshlogic/blender-addons/tree/master/collada-exporter-sl>`_


.. listing:: blender-addons/collada-exporter-sl/0.3/ColladaExporterSL.py python
    :number-lines:


