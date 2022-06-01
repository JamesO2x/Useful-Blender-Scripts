# This script will loop through all the materials in your selected object, 
# and assign them an ALPHA blending mode, as well as set "backface culling" 
# and other useful performance options for making game models.
# 
# Just select some objects and click RUN SCRIPT.
# 
# Blend Mode & Shadow Node options are:
#   - 'NONE'   = None (for Shadow Mode only)
#   - 'OPAQUE' = Opaque
#   - 'CLIP'   = Alpha Clip
#   - 'HASHED' = Alpha Hashed
#   - 'BLEND'  = Alpha Blend (not applicable for Shadow Mode)

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
        node_1 = node_tree.nodes["Image Texture"]
        node_2 = node_tree.nodes["Principled BSDF"]
        node_tree.links.new(node_1.outputs["Color"], node_2.inputs[0]) # 0 = Color slot
        node_tree.links.new(node_1.outputs["Alpha"], node_2.inputs[21]) # 21 = Alpha slot


# Source for linking two nodes together: 
# https://devtalk.blender.org/t/how-to-connect-nodes-using-script-commands/11567/2