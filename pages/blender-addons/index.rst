.. title: Blender Addons
.. slug: blender-addons
.. date: 2017-04-10 13:50:43 UTC+02:00
.. category: 
.. tags: 
.. link: 
.. description: 
.. type: text


.. image:: blender_logo.png
    :align: right


.. class:: addon-list

	- `Outliner Tweaks <link://slug/outliner-tweaks>`_

	- `Extra Material List <link://slug/extra-material-list>`_

	- `Extra Image List <link://slug/extra-image-list>`_

	- `Collada Exporter for Second Life <link://slug/collada-exporter-second-life>`_

	- `Toggle object Wire <link://slug/toggle-object-wire>`_

	- `Bake Helper <link://slug/bake-helper>`_


|

--------------------------------------------------------------------------------

`Blender <https://www.blender.org/>`_ is a well known **open-source package for 3D graphics**. It's a very vivid and progressing project. Every new release brings some new exciting features and improvements. By design, it can't compete with parametric non-destructive CAD packages, but compared to other commercial mesh based programs (like Maya, 3ds Max or MODO), Blender does a very good job and even exceeds them in many aspects like:


.. class:: pros-list

	- Very light and easy installation on Windows, Mac, Linux. No obstructive registration needed :)

	- Super fast program start compared to the heavy commercial programs like 3ds Max.

	- Efficient and logically chosen shortcuts.

	- Realistic GPU enabled cycles render engine (PBR live-rending comes in version 2.8).

	- Fully customizable and scriptable user interface with no lag. Even enables proportional UI scaling, which users of most commercial programs can just dream about :)

	- Very powerful Python based scripting API for creating addons.


Of course, to be fair, no program is perfect and there are important features that are still missing in Blender and some tasks are rather complicated to do, especially:

.. class:: cons-list

	- A built-in material library system (there are various addons, but I think a proper library system should be the core feature).

	- A more intuitive layer manager (outliner) that would allow to organize objects into a folder structure.

	- Workflow for baking is very inefficient by default (can be automated by addons).

	- There is no baking pass for cavity map, PBR roughness and metalness map.

	- There is no option to set face-weighted normals, which would be useful for hard-surface models (can be enabled by addons).

	- There are vertex groups only, but for tasks like beveling, edge groups would be more useful.

	- Bevel modifier doesn't work well in special cases (like profile=1.0).

	- Mesh modeling is rather destructive. There is a modifier stack, but its usage is very limited compared to non-destructive workflows like in 3D CADs, or compared to the Edit Poly modifier in 3ds Max.








