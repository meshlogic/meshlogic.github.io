.. title: Outliner Tweaks - Blender Addon
.. slug: outliner-tweaks
.. date: 2018-01-02 15:00:00 UTC+02:00
.. category: blender/addons
.. tags: blender, blender-addon, python
.. type: text
.. link: 
.. previewimage: teaser.png
.. description: Make organizing objects and groups in Outliner easier.

.. default-role:: code
.. TEASER_END

.. figure:: outliner02.png
	:align: right
	:class: figure

	Outliner itself can display all objects, but they can't be sorted into folders.



I think many Blender users would agree that organizing objects into layers is not a strong side of Blender. The concept of **20 unnamed layers** is very unfortunate and easily tends to chaos in your files. Even when opening my own file, I always have to go through all the unnamed layers to see what objects are on which layer.

Moreover, there is the **Outliner** panel, which rather brings more confusion than help with organizing your objects. Well, you can see there a list of all objects, but you are unable to organize them into folders to bring some order into your scene. Besides, when you select some objects in the outliner, you don't see them in the viewport, because it collides with the layer visibility.

Later, I discovered there is the **Groups** options to display grouped objects, but again, it's implemented in a very unintuitive way. When you switch to Groups, you see only the existing groups and cannot create new groups. To make it even more confusing, it doesn't show objects that has no group assigned yet, so you can't select them and assign them to the new group.

So, my conclusion always was that the **Outliner** is just a confusing part of Blender and I never used it. But recently, I got really annoyed with the chaos in my Blender files, and tried to script some tweaks that would make Outliner more useful.


How it works?
================

.. figure:: outliner-tweaks-01.png
	:align: right
	:class: figure

	Outliner and menu of the Outliner Tweaks.


The idea behind the addon is to introduce two **auxiliary groups** and commands that work on them. It adds a little icon in the corner of the Outliner menu and introduces some commands with hotkeys.


Auxiliary Groups
	.. class:: li-medskip

		- **#DEFAULT_GROUP** - This group collects all objects that are not grouped yet. So, you can finally see all ungrouped objects in the Outliner, even when the Outliner is set to display groups only. To update the #DEFAULT_GROUP group press **U** when your mouse is in the Outliner.

		- **#NEW_GROUP** - This group enables to add selected objects into a new group from Outliner. Press **N** and the #NEW_GROUP is created. Then, you can rename this group as you wish.



Update Default Group (U)
	- Group all unsorted objects (add them to the #DEFAULT_GROUP).
	- Clean the #DEFAULT_GROUP from the objects that already belong to other groups.

Add to New Group (N)
    - Add selected objects to the #NEW_GROUP.
    - Remove them from all other groups.

Remove from Groups (R)
    - Remove selected objects from all groups.
    - Add them to the DEFAULT_GROUP.

Expand/Collapse One Level (E)
	- Toggle Expand/Collapse one level for all items.

Isolate Selection (Q)
	- Isolate (display) the selected objects in the 3D viewport and make sure the right layers are enabled.
	- Enable visibility and render for the selected objects.
	- Restrict visibility and render for all other objects.


Conclusion
============

I think this addon finally makes Outliner usable. You can manage all objects and groups directly from the Outliner without the need to switch between panels. Also, you can finally display all the selected objects in the 3D viewport and don't need to bother with the 20 unnamed layers anymore.

I know there are plans to improve the layer management system in the milestone Blender 2.8. But I didn't want to wait, because I guess it will take lots of time yet, before we have a stable and bug-free version of Blender 2.8.


ChangeLog
==========

Version 0.1 (02.01.2018)
    - Initial release


Download
================

.. listing:: blender-addons/outliner-tweaks/0.1/OutlinerTweaks.py python
    :number-lines:

