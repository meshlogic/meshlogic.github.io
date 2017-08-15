.. title: Eliminate Material and Node Group Duplicates in Blender
.. slug: eliminate-material-duplicates
.. date: 2017-08-13 15:00:00 UTC+02:00
.. category: blender
.. tags: blender-scripting
.. link: 
.. description:
.. type: text

.. TEASER_END


I got to the point when wishing to build and organize a decent library of smart materials for Blender (something like you can have in 3D Coat or Substance Painter if you don't mind using proprietary software). I got really tempted to start making such library when Blender 2.79 officially included the material library addon called **MatLib VX**.

But alas, even this useful addon **MatLib VX** doesn't bring any significantly new functionality to Blender. It just uses the existing **append/link** feature which enables you to include various datablocks from external Blender files. And here comes the problematic aspect of appending materials from external files. Imagine your materials use custom node groups (like shader setups, etc). **Then every time you append a material, Blender automatically creates numbered duplicates for all node groups with the same name, even when the groups are supposed to be exactly the same!** And this means huge mess in your node groups. A similar problem occurs when you are appending mesh assets containing the same materials.

So, to fix this bug/feature, I have created a simple script that eliminates all these duplicates after you append materials from your external files. It searches all existing node groups, materials, worlds and if finds any duplicates (ending with .001, .002, etc), it replaces them with the original group or material if it is found.

After running the script **the eliminated node groups and materials will have zero 0 users**, so after you save and reopen your file, they should disappear and your group list should be clean and tidy :)


.. code-block:: python
    :number-lines:

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
    eliminate_node_groups()
    eliminate_materials()



Now, I'm thinking I will include this code in my another addon **Extra Material List**, which displays materials in a more comfy way than the default short pop-up list.


