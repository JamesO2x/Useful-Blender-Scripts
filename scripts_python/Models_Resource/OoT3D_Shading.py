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

# Vertex Color Multiplier. 
# Thanks to Alvare and Scurest from : https://www.vg-resource.com/thread-28564-page-27.html
x = 4.6 # Normal value: 2, Corrected Blender value: 4.6.


# Get a list of all the currently selected objects.
list = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

# Loop through all the objects in the list.
for obj in list:
    
    # Loop through each material in each individual object
    for material_slot in obj.material_slots:
        
        # Get the Node Tree
        ntree = material_slot.material.node_tree
        
        # Define the Image and BSDF nodes
        bsdf = ntree.nodes["Principled BSDF"]
        imag = ntree.nodes["Image Texture"]
        
        # Add the first MixRGB node
        mix1 = ntree.nodes.get('VertTextureMixer')
        if mix1 is None:
            # Adjust the image node position
            imag.location.x = -570
            imag.location.y = 270
            # Create node if not existing
            mix1 = ntree.nodes.new('ShaderNodeMixRGB')
            mix1.name = "VertTextureMixer"
            mix1.label = "Vert + Text. Mixer"
            mix1.location.x = -280
            mix1.location.y = 160
        # Assign its layer
        mix1.blend_type = 'MULTIPLY'
        mix1.inputs[0].default_value = 1.0 # increase factor to 1.0
        
        # Add the second MixRGB node
        mix2 = ntree.nodes.get('VertColorMultiply')
        if mix2 is None:
            mix2 = ntree.nodes.new('ShaderNodeMixRGB')
            mix2.name = "VertColorMultiply"
            mix2.label = "Vert Color Multiply"
            mix2.location.x = -480
            mix2.location.y = 0
        # Set Multiply, Factor, and Multiply strength
        mix2.blend_type = 'MULTIPLY'
        mix2.inputs[0].default_value = 1.0 # increase factor to 1.0
        mix2.inputs[2].default_value = (x,x,x,1) # RGBa multiplier
        

        # Add the vertex color node
        vcol = ntree.nodes.get('VertColor')
        if vcol is None:
            vcol = ntree.nodes.new('ShaderNodeVertexColor')
            vcol.name = "VertColor"
            vcol.label = "Vertex Color"
            vcol.location.x = -680
            vcol.location.y = -20
        # This should get the name of the active Vertex Color Layer
        vcol.layer_name = obj.data.vertex_colors.active.name       
        
        
        
        # Connect the 1st MixRGB to the BSDF
        ntree.links.new(mix1.outputs["Color"], bsdf.inputs[0]) # 0 = Color slot
        
        # Connect Image and 2nd MixRGB to the 1st MixRGB
        ntree.links.new(imag.outputs["Color"], mix1.inputs[1]) # 1 = Color1 slot
        ntree.links.new(mix2.outputs["Color"], mix1.inputs[2]) # 2 = Color2 slot
        
        # Connect the Vertex color to its multiplier MixRGB
        ntree.links.new(vcol.outputs["Color"], mix2.inputs[1]) # 1 = Color1 slot


# Source for linking two nodes together: 
# https://devtalk.blender.org/t/how-to-connect-nodes-using-script-commands/11567/2
