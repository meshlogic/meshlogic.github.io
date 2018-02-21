.. title: Eliminate Material and Node Group Duplicates
.. slug: eliminate-material-duplicates
.. date: 2017-08-13 15:00:00 UTC+02:00
.. category: blender/scripting
.. tags: blender, python
.. link: 
.. type: text
.. previewimage: teaser.png
.. description: Get rid of the unwanted datablock duplicates.

.. TEASER_END


.. figure:: teaser.png
    :align: right
    :class: figure


I think the major shortage of Blender is a missing library system for materials (something like the library system in Substance Painter). There are addons trying to implement this, but I think such fundamental feature should be implemented in the program core.

Moreover, everything what an addon can do is to utilize the standard **append** command from an external file. And here comes the annoying fact: **Every time you append an asset, Blender automatically creates numbered duplicates for all datablocks with the same name, even when they are intended to be exactly the same!** This is the reason, why after appending objects or materials, several duplicates (ending with .001, .002, etc) of the same material or node group appear in your scene.

To clean the duplicates, I made a simple script. It searches all existing materials and node groups. Then, if any duplicates (ending with .001, .002, etc) are found, they are replaced with the original item.

After running the script, **the eliminated datablock will have 0 users**. So, when you save and reopen your file, all duplicates should disappear and your material/group list should be clean :)


Eliminate Material Duplicates
=================================

.. code-block:: python

    import bpy

    #--- Eliminate Material Duplicates
    def eliminate_materials():
        print("\nEliminate Material Duplicates:")
        
        #--- Search for mat. slots in all objects
        mats = bpy.data.materials
        
        for obj in bpy.data.objects:
            for slot in obj.material_slots:
                
                # Get the material name as 3-tuple (base, separator, extension)
                (base, sep, ext) = slot.name.rpartition('.')
                
                # Replace the numbered duplicate with the original if found
                if ext.isnumeric():
                    if base in mats:
                        print("  For object '%s' replace '%s' with '%s'" % (obj.name, slot.name, base))
                        slot.material = mats.get(base)

    #--- Execute
    eliminate_materials()


Eliminate Node Group Duplicates
=================================

.. code-block:: python

    import bpy

    #--- Eliminate Node Group Duplicates
    def eliminate_node_groups():
        print("\nEliminate Node Group Duplicates:")

        #--- Search for duplicates in the actual node groups
        node_groups = bpy.data.node_groups
        
        for group in node_groups:
            for node in group.nodes:
                if node.type == 'GROUP':
                    eliminate(node)
                    
        #--- Search for duplicates in materials
        mats = list(bpy.data.materials)
        worlds = list(bpy.data.worlds)
        
        for mat in mats + worlds:
            if mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'GROUP':
                        eliminate(node)
         
    #--- Eliminate the node group duplicate with the original group if found
    def eliminate(node):
        node_groups = bpy.data.node_groups
        
        # Get the node group name as 3-tuple (base, separator, extension)
        (base, sep, ext) = node.node_tree.name.rpartition('.')
        
        # Replace the numbered duplicate with original if found
        if ext.isnumeric():
            if base in node_groups:
                print("  Replace '%s' with '%s'" % (node.node_tree.name, base))
                node.node_tree.use_fake_user = False
                node.node_tree = node_groups.get(base)

    #--- Execute
    eliminate_node_groups()


Eliminate OSL Script Duplicates
=================================

A similar method should work also to clean duplicates of OSL scripts.

.. code-block:: python

    import bpy

    #--- Eliminate OSL Script Duplicates
    def eliminate_osl():

        print("\nEliminate OSL Scripts:")
        texts = bpy.data.texts

        for mat in bpy.data.materials:
            if mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'SCRIPT':
                        name = node.script.name
                        (base, sep, ext) = name.rpartition('.')

                        # Replace the numbered duplicate with the original if found
                        if ext.isnumeric():
                            if base in texts:
                                print("  Replace '%s' with '%s'" % (name, base))

                                # Replace the script duplicate for this node
                                node.script = texts.get(base)

                                # Remove the script duplicate from bpy.data.texts ?
                                texts.get(name).user_clear()      

    #--- Execute
    eliminate_osl()


Addon to Eliminate the Duplicates
===================================

I added this functionality as a button to eliminate material and node group duplicates to my addon `Extra Material List <link://slug/extra-material-list>`_.


|


