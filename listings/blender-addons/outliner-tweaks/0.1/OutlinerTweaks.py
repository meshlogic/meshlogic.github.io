#-------------------------------------------------------------------------------
#                      Outliner Tweaks - Addon for Blender
#
# Auxiliary Groups
# - #DEFAULT_GROUP - to collect ungrouped objects
# - #NEW_GROUP
#
# Commands:
# - Update Default Group (U)
# - Add to New Group (N)
# - Remove from Groups (R)
# - Expand/Collapse One Level (E)
# - Isolate Selection (Q)
#
#-------------------------------------------------------------------------------
# Version: 0.1
# Revised: 2.1.2018
# Author: Miki (meshlogic)
#-------------------------------------------------------------------------------
bl_info = {
    "name": "Outliner Tweaks",
    "author": "Miki (meshlogic)",
    "category": "3D View",
    "description": "Make organizing objects and groups in Outliner easier.",
    "location": "Outliner > Header",
    "version": (0, 1),
    "blender": (2, 79, 0)
}

import bpy
from bpy.props import *
from bpy.types import Menu, Operator, Panel, UIList


#--- Set default groups names
DEFAULT_GROUP = "#DEFAULT_GROUP"
NEW_GROUP = "#NEW_GROUP"

#--- Print debug msg into console
DEBUG = False
def dprint(*msg):
    if DEBUG: print(*msg)
    

#-------------------------------------------------------------------------------
# MISC FUNC
#-------------------------------------------------------------------------------
def activate_all_layers():
    for i in range(20):
        bpy.context.scene.layers[i] = True
    return

def cache_layers():
    layer_cache = [False]*20
    for i in range(20):
        layer_cache[i] = bpy.context.scene.layers[i]   
    return layer_cache

def restore_layers(layer_cache):
    for (i, state) in enumerate(layer_cache):
        bpy.context.scene.layers[i] = state
    return


#-------------------------------------------------------------------------------
# IsolateSelection_OT
#-------------------------------------------------------------------------------
class IsolateSelection_OT(Operator):
    """Isolate the selected objects in the 3D viewport
    - 1. Enable visibility and render for the selected objects
    - 2. Restrict visibility and render for all other objects
    - 3. Make visible only the layers of the selected objects"""
    
    bl_idname = "outliner.isolate_selection"
    bl_label = "Isolate Selection"

    #--- Available only in object mode
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'

    def execute(self, context):
        dprint("\n*** outliner.isolate_selection ***")

        #--- All layers must be active (you cannot get selected_objects on inactive layers)
        activate_all_layers()
        layer_mask = [False]*20
        
        #--- Loop all objects
        for obj in bpy.data.objects:
            
            # 1. Make selected objects visible
            if obj in bpy.context.selected_objects:
                
                # Add object's layer to the mask
                layer_mask = [a or b for a,b in zip(obj.layers, layer_mask)]
            
                obj.hide = False
                obj.hide_render = False
                
            # 2. Hide all other objects
            else:
                obj.hide = True
                obj.hide_render = True
        
        #--- 3. Make visible only the layers of the selected objects
        restore_layers(layer_mask)
        
        return{'FINISHED'}


#-------------------------------------------------------------------------------
# ExpandCollapse_OT
#-------------------------------------------------------------------------------
class ExpandCollapse_OT(Operator):
    """Toggle Expand/Collapse one level for all items"""

    bl_idname = "outliner.expand_collapse_one_level"
    bl_label = "Expand/Collapse One Level"
    
    toggle_expand = BoolProperty(default = False)
    
    #--- Available only in object mode
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'

    def execute(self, context):
              
        # Collapse all items
        for i in range(5):
            bpy.ops.outliner.show_one_level(open=False)
        
        # Toggle expand
        if not self.toggle_expand:
            bpy.ops.outliner.show_one_level(open=True)
        
        self.toggle_expand = not self.toggle_expand 
        
        return{'FINISHED'}
        
        
#-------------------------------------------------------------------------------
# UpdateDefaultGroup_OT
#-------------------------------------------------------------------------------
class UpdateDefaultGroup_OT(Operator):
    """Update Default Group
    - 1. Group all unsorted objects (add them to the DEFAULT_GROUP)
    - 2. Clean the DEFAULT_GROUP from the objects that already belong to other groups"""

    bl_idname = "outliner.update_default_group"
    bl_label = "Update Default Group"

    #--- Available only in object mode
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'

    def execute(self, context):
        dprint("\n*** outliner.update_default_group ***")
        
        #--- Create DEFAULT_GROUP if it doesn't exist yet
        if DEFAULT_GROUP not in bpy.data.groups:
            bpy.ops.group.create(name = DEFAULT_GROUP)
        
        #--- Loop all objects
        for obj in bpy.data.objects:
            
            # Get names of all groups the obj belongs to
            obj_groups = [g.name for g in obj.users_group]
            
            # 1. Add ungrouped object to DEFAULT_GROUP
            if len(obj_groups) == 0:
                bpy.data.groups.get(DEFAULT_GROUP).objects.link(obj)
                dprint(" ", obj.name, "added to", DEFAULT_GROUP)
            
            # 2. Remove grouped obj from DEFAULT_GROUP
            elif len(obj.users_group) > 1 and DEFAULT_GROUP in obj_groups:
                bpy.data.groups.get(DEFAULT_GROUP).objects.unlink(obj)
                dprint(" ", obj.name, "removed from", DEFAULT_GROUP)
        
        return{'FINISHED'}
        

#-------------------------------------------------------------------------------
# AddToNewGroup_OT
#-------------------------------------------------------------------------------
class AddToNew_OT(Operator):
    """Add to New Group
    - 1. Add selected objects to the NEW_GROUP
    - 2. Remove them from all other groups"""

    bl_idname = "outliner.add_to_new_group"
    bl_label = "Add to New Group"
    
    #--- Available only in object mode
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'
    
    def execute(self, context):
        dprint("\n*** outliner.add_to_new_group ***")
        
        #--- All layers must be active (you cannot get selected_objects on inactive layers)
        layer_cache = cache_layers()
        activate_all_layers()
        
        #--- Create NEW_GROUP, if it doesn't exist yet
        if NEW_GROUP not in bpy.data.groups:
            bpy.ops.group.create(name = NEW_GROUP)
        
        #--- Loop the selected objects
        for obj in bpy.context.selected_objects:
            
            # 2. Remove from all groups
            for group in obj.users_group:
                group.objects.unlink(obj)
                dprint(" ", obj.name, "removed from", group.name)
            
            # 1. Add obj to the NEW_GROUP
            bpy.data.groups.get(NEW_GROUP).objects.link(obj)
            dprint(" ", obj.name, "added to", NEW_GROUP)
            
        #--- Restore layers visibility
        restore_layers(layer_cache) 
    
        return{'FINISHED'}
   
   
#-------------------------------------------------------------------------------
# RemoveFromGroups_OT
#-------------------------------------------------------------------------------
class RemoveFromGroups_OT(Operator):
    """Remove from Groups
    - 1. Remove selected objects from all groups
    - 2. Add them to the DEFAULT_GROUP"""

    bl_idname = "outliner.remove_from_groups"
    bl_label = "Remove from Groups"
    
    #--- Available only in object mode
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'
    
    def execute(self, context):
        dprint("\n*** outliner.remove_from_groups ***") 
        
        #--- All layers must be active (you cannot get selected_objects on inactive layers)
        layer_cache = cache_layers()
        activate_all_layers()

        #--- Loop the selected objects
        for obj in bpy.context.selected_objects:
            
            # 1. Remove obj from all groups
            for group in obj.users_group:
                group.objects.unlink(obj)
                dprint(" ", obj.name, "removed from", group.name)
                
            # 2. Add obj to DEFAULT_GROUP
            bpy.data.groups.get(DEFAULT_GROUP).objects.link(obj)
            dprint(" ", obj.name, "added to", DEFAULT_GROUP)

        #--- Restore layers visibility
        restore_layers(layer_cache)
    
        return{'FINISHED'} 
    

#-------------------------------------------------------------------------------
# MENU ITEMS
#-------------------------------------------------------------------------------
def draw_menu(self, context):
    layout = self.layout
    layout.menu("OutlinerTweaksMenu", icon='COLLAPSEMENU', text="")
    
class OutlinerTweaksMenu(Menu):
    bl_idname = "OutlinerTweaksMenu"
    bl_label = ""
    
    def draw(self, context):
        layout = self.layout
        layout.operator("outliner.isolate_selection", icon='RESTRICT_VIEW_OFF')
        layout.operator("outliner.expand_collapse_one_level", icon='OOPS')
                
        layout.separator()
        layout.operator("outliner.remove_from_groups", icon='X')
        layout.operator("outliner.add_to_new_group", icon='GROUP')
        layout.operator("outliner.update_default_group", icon='FILE_REFRESH')


#-------------------------------------------------------------------------------
# REGISTER/UNREGISTER KEYMAPS
#-------------------------------------------------------------------------------
addon_keymaps = []

def register_keymaps():
    wm = bpy.context.window_manager
    
    km = wm.keyconfigs.addon.keymaps.new(name="Outliner", space_type="OUTLINER")
    kmi = km.keymap_items.new("outliner.isolate_selection", "Q", "PRESS", shift=False)
    addon_keymaps.append((km, kmi))
    
    km = wm.keyconfigs.addon.keymaps.new(name="Outliner", space_type="OUTLINER")
    kmi = km.keymap_items.new("outliner.expand_collapse_one_level", "E", "PRESS", shift=False)
    addon_keymaps.append((km, kmi))
    
    km = wm.keyconfigs.addon.keymaps.new(name="Outliner", space_type="OUTLINER")
    kmi = km.keymap_items.new("outliner.update_default_group", "U", "PRESS", shift=False)
    addon_keymaps.append((km, kmi))
    
    km = wm.keyconfigs.addon.keymaps.new(name="Outliner", space_type="OUTLINER")
    kmi = km.keymap_items.new("outliner.add_to_new_group", "N", "PRESS", shift=False)
    addon_keymaps.append((km, kmi))
    
    km = wm.keyconfigs.addon.keymaps.new(name="Outliner", space_type="OUTLINER")
    kmi = km.keymap_items.new("outliner.remove_from_groups", "R", "PRESS", shift=False)
    addon_keymaps.append((km, kmi))
    
def unregister_keymaps():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi) 


#-------------------------------------------------------------------------------
# REGISTER/UNREGISTER CLASSES
#-------------------------------------------------------------------------------
def register():
    bpy.utils.register_module(__name__)
    bpy.types.OUTLINER_HT_header.prepend(draw_menu)
    register_keymaps()

def unregister():
    unregister_keymaps()
    bpy.types.OUTLINER_HT_header.remove(draw_menu)
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()


