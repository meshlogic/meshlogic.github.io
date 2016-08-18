.. title: Bake Helper - Addon for Blender
.. slug: bake-helper
.. date: 2016-07-13 18:02:42 UTC+02:00
.. tags: 
.. category: Blender-Addons
.. link: 
.. description: 
.. type: text

.. .............................................................................
.. default-role:: code
.. role:: text-info
.. role:: html(raw)
    :format: html
.. .............................................................................


.. class:: container-990px

    .. slides::
        BakeHelper_00.png
        BakeHelper_02.png
        BakeHelper_03.png
        BakeHelper_04.png


Rendering to textures, or **baking textures**, allows you to create **texture/image maps** based on the object's appearance in the rendered scene. Later, these image maps can be re-mapped onto the object using the object’s UV-coordinate system, this process is called **UV  mapping**. It enables to speed up any further rendering, since colors and details are already computed and baked into the object's textures. This approach is essential for real-time rendering engines used in computer games or virtual worlds.



Motivation
==========

By default, Blender already enables to bake textures, but the workflow is very time-consuming, requiring to manually repeat lots of tasks, especially when you need to bake large scenes containing lots of objects. Here is an example, what all you need to do when baking textures in Blender using Cycles-Render.

.. class:: li-smallskip

    - In UV Editor, for each object/material in the scene, manually create and name an image map.

    - In Node Editor, for each material, add a node with the named image map and don't forget to leave it selected!

    - Now, you can finally click the Bake button and wait for the result.

    - Although you still can't see the baked textures mapped onto the objects. You need to enter Blender-Render Textured viewport mode, and manually assign all baked textures to each object in the scene.

So, it's obvious such workflow is very slow and requires to manually repeat lots of tasks that could be automated, and that's the goal of **Bake Helper** addon.



Features of Bake Helper
=======================

.. figure:: bake_helper_cycles.png
    :align: right
    :class: thumbnail

Bake Helper is intended to automate the baking workflow and to save your time by creating, assigning and saving all desired texture/image maps. In contrast to other tools, it enables to bake a separate image map for each material. This makes it especially useful for creating content for virtual grids like Second Life.


.. class:: li-smallskip

    - Works with both Blender-Render and Cycles-Render.

    - Enables to bake all objects marked in the list or a single selected object.

    - Automatically creates and assigns image maps for each object and its materials with the default name: :html:`<br>` `ObjectName_MaterialName_BakeType.png`

    - Enables to merge all object's materials into a single image map named: :html:`<br>` `ObjectName_BakeType.png`

    - Automatically assigns image maps of various types (UV Grid, Color Grid, AO, Combined, Full Render) to all selected objects.

    - When baking is finished, Blender-Render Textured viewport is invoked to display the baked image maps.

    - Save all baked image maps into the desired folder by a single click.

    - You can use shortcut to bake (F5) and shortcut to switch viewport engine and shading (F4).



Notes for baking using Blender-Render
-------------------------------------

.. class:: instruction-list li-medskip

    - :html:`❶` Add selected objects to the bake list. :html:`<br>`:text-info:`Objects intended for baking must contain a valid UV map and material(s) for Blender-Render.`

    - :html:`❷` Select dimensions for each image map associated to each material. Or, you can set to merge all materials into a single image map. :html:`<br>`:text-info:`Note that you need to provide an UV map where polygons do not overlap.`

    - :html:`❸` Specify the bake options like Bake Type, Ray Samples or Shadows Falloff. Don't forget to enable Ambient Occlusion in World settings if you need it. Then hit BAKE button (or F5) to start the baking process. :html:`<br>`:text-info:`The addon automatically creates and assigns all needed image maps for baking.`

    - :html:`❹` When baking is finished, Blender-Render Textured viewport is invoked to display the baked image maps. :html:`<br>`:text-info:`You can also assign and display image maps of other types by clicking the dedicated buttons (UV Grid, Color Grid, AO, Combined, Full Render).`

    - :html:`❺` Save the baked image maps into the desired folder. :html:`<br>`:text-info:`The path must end with "\\".`



Notes for baking using Cycles-Render
-------------------------------------

.. class:: instruction-list li-medskip

    - :html:`❶` Add selected objects to the bake list. :html:`<br>`:text-info:`Objects intended for baking must contain a valid UV map and material(s) for Cycles-Render.`

    - :html:`❷` Select dimensions for each image map associated to each material. Or, you can set to merge all materials into a single image map. :html:`<br>`:text-info:`Note that you need to provide an UV map where polygons do not overlap.`

    - :html:`❸` Specify the bake options like Bake Type or Render Samples. Don't forget to enable Ambient Occlusion in World settings if you need it. Then hit BAKE button (or F5) to start the baking process. :html:`<br>`:text-info:`The addon automatically creates all needed image maps for baking.  Also it adds an image node with the image map for each Cycles material and removes it after baking. This way the same material can be shared by multiple objects.`

    - :html:`❹` When baking is finished, Blender-Render Textured viewport is invoked to display the baked image maps. :html:`<br>`:text-info:`You can also assign and display image maps of other types by clicking the dedicated buttons (UV Grid, Color Grid, AO, Combined, Full Render).`

    - :html:`❺` Save the baked image maps into the desired folder. :html:`<br>`:text-info:`The path must end with "\\".`




Purchase
========

- This addon is for sale at `Blender Market <https://cgcookiemarkets.com/all-products/bake-helper/>`_



ChangeLog
=========

Version 1.0 (26.04.2016):
    - Fixed compatibility with Blender 2.77
    - Added button to select a render engine used for baking
    - When baking is finished, Blender-Render Textured viewport is invoked to display the baked image maps


Version 0.1 (12.12.2014):
    - Initial release for Blender 2.72



    

