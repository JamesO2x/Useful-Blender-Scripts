import bpy

# Clears the '.001' from object names that were duplicated at some point.
for obj in bpy.data.objects:
    obj.name = obj.name.replace(".001","")
    
# Thanks: [modeling - Override naming of duplicated object - Blender Stack Exchange](https://blender.stackexchange.com/questions/201985/override-naming-of-duplicated-object)
