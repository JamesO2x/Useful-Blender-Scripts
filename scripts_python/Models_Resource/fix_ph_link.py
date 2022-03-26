# This script will loop through all the materials in an object, and assign them an ALPHA blending mode,
# as well as set "backface culling" and other useful performance options for making game models.
# 
# Just select some objects and click RUN SCRIPT.
# 
# This script was specifically designed to fix this FBX model:
# [Zelda: Phantom Hourglass Link - The Models Resource](https://www.models-resource.com/ds_dsi/legendofzeldaphantomhourglass/sheet/7794/)
# 
# But this script could be used for similar models
# 
# Other Resources used:
# - Conver the FBX into FBX that Blender can read: [Rich Whitehouse](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91)
# - Import FBX Settings:
#   - Scale = 100
#   - Primary Bone Axis = X Axis
#   - Secondary Bone Axis = Z Axis

import bpy

# Get a list of all the currently selected objects.
list = [i for i in bpy.context.selected_objects if i.type == 'MESH']

# Loop through all the objects in the list.
for i in list:
    
    # Loop through each material in each individual object
    for material_slot in i.material_slots:
        material_slot.material.use_backface_culling = 1
        # Blend Mode & Shadow Node options are -> NONE, OPAQUE, CLIP, HASHED, BLEND
        material_slot.material.blend_method = 'CLIP'
        material_slot.material.shadow_method = 'CLIP'
        material_slot.material.alpha_threshold = 0.5
        
        # Run through all nodes
        for node in material_slot.material.node_tree.nodes:
            # If the node type is texture 
            if node.type == 'TEX_IMAGE':
                # Set the interpolation -> Linear, Closest, Cubic, Smart
                node.interpolation = 'Closest'

# Source for effecting multiple image texture nodes: 
# https://blender.stackexchange.com/questions/202371/how-to-change-texture-interpolation-of-many-images-all-at-once
