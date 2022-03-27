# This script will loop through all the materials in an object, and assign them an ALPHA blending mode,
# as well as set "backface culling" and other useful performance options for making game models.
# 
# Just select some objects and click RUN SCRIPT.
# 
# This fixes some strange alpha issues on some interior models from Majora's Mask 3D

import bpy

# Get a list of all the currently selected objects.
list = [i for i in bpy.context.selected_objects if i.type == 'MESH']

# Loop through all the objects in the list.
for i in list:
    
    # Loop through each material in each individual object
    for material_slot in i.material_slots:
        material_slot.material.use_backface_culling = 1
        material_slot.material.blend_method = 'CLIP'
        material_slot.material.shadow_method = 'CLIP'
        material_slot.material.alpha_threshold = 0.5
        
        # Connect the Image Node (Color & Alpha) to the BSDF Node
        node_tree = material_slot.material.node_tree
        node_2 = node_tree.nodes["Principled BSDF"]
        node_2.inputs[21].default_value = 1 # 21 = Alpha slot

# Source for linking two nodes together: 
# https://devtalk.blender.org/t/how-to-connect-nodes-using-script-commands/11567/2