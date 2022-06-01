# This script will take your selected objects, and combine its Vertex Color Layer
# and its image texture color, in a specific way that mimicks Ocarina of Time 3D.
# 
# First, make sure your objects have a Vertex Color Layer in the mesh data.
# Then, press A to select all objects in your scene
# (or only select the objects you want this effect to be added to).
# Then simply press RUN SCRIPT, and you're done.
#
# It may take a few minutes for Blender to "compile your shaders"
# so be patient if the effect isn't immediate.
#
# Warning: Only run this script ONCE on your objects.
# Running this script a second time on the same objects will create
# multiple duplicate shader nodes.


import bpy

# Get a list of all the currently selected objects.
list = [i for i in bpy.context.selected_objects if i.type == 'MESH']

# Loop through all the objects in the list.
for i in list:
    
    # Loop through each material in each individual object
    for material_slot in i.material_slots:
        
        # Get the Node Tree
        node_tree = material_slot.material.node_tree
        
        # Add the first MixRGB node
        mix1 = node_tree.nodes.new('ShaderNodeMixRGB')
        mix1.location.x = -280
        mix1.location.y = 160
        # Assign its layer
        mix1.blend_type = 'MULTIPLY'
        mix1.inputs[0].default_value = 1.0 # increase factor to 1.0
        
        # Add the second MixRGB node
        mix2 = node_tree.nodes.new('ShaderNodeMixRGB')
        mix2.location.x = -480
        mix2.location.y = 0
        # Set Multiply, Factor, and Multiply strength
        mix2.blend_type = 'MULTIPLY'
        mix2.inputs[0].default_value = 1.0 # increase factor to 1.0
        mix2.inputs[2].default_value = (2.0,2.0,2.0,1.0) # 2x color multiplier
        

        # Add the vertex color node
        vcol = node_tree.nodes.new('ShaderNodeVertexColor')
        vcol.location.x = -680
        vcol.location.y = -20
        # This should get the name of the active Vertex Color Layer
        vcol.layer_name = i.data.vertex_colors.active.name       

        # Define the Image and BSDF nodes
        imag = node_tree.nodes["Image Texture"]
        bsdf = node_tree.nodes["Principled BSDF"]
        imag.location.x = -570
        imag.location.y = 270
        
        # Connect the 1st MixRGB to the BSDF
        node_tree.links.new(mix1.outputs["Color"], bsdf.inputs[0]) # 0 = Color slot
        
        # Connect Image and 2nd MixRGB to the 1st MixRGB
        node_tree.links.new(imag.outputs["Color"], mix1.inputs[1]) # 1 = Color1 slot
        node_tree.links.new(mix2.outputs["Color"], mix1.inputs[2]) # 2 = Color2 slot
        
        # Connect the Vertex color to its multiplier MixRGB
        node_tree.links.new(vcol.outputs["Color"], mix2.inputs[1]) # 1 = Color1 slot


# Source for linking two nodes together: 
# https://devtalk.blender.org/t/how-to-connect-nodes-using-script-commands/11567/2