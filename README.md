# Useful Blender Scripts
 A collection of useful python scripts for certain tasks in Blender.

Currently only `5` scripts in this repository so far.

Also, checkout  [Noesis](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91) - a program for converting just about any 3D format:

---

# scripts_batchfile
## _template.bat
This BATCH script Creates a new Blender Project Folder with some template files, notes, and folders within in it.

---

# scripts_python
## clear_duplicate_names.py
Removes any `.001` from all object names in a scene. Useful if you've made a duplicate of an object, then later deleted the original, and want to "clear out" the numbers added to the name. This script can also be easily modified to add or replace any text in object names in bulk.


## set_alpha.py script
Automatically plugs the `Color` and `Alpha` nodes together, as well as sets a few other parameters to display Alpha transparency on selected objects. Useful for imported models found on [The Models Resource](https://www.models-resource.com/).

![](img/set_alpha.gif)


---

# Models_Resource scripts
## fix_mm_interiors.py
This script will loop through all the materials in selected objects, and assign them an `ALPHA` blending mode,
as well as set "backface culling" and other useful performance options for making game models.

This script was originally written to fixe some strange alpha issues on some interior models from [The Legend of Zelda: Majora's Mask 3D - The Models Resource](https://www.models-resource.com/3ds/thelegendofzeldamajorasmask3d/).


## fix_ph_link.py script
Used to fix the [Phantom Hourglass Link FBX model](https://www.models-resource.com/ds_dsi/legendofzeldaphantomhourglass/sheet/7794/) from Models Resource. This script sets the proper blend mode (CLIP) as well as "Closest" interpolation on textures to mimmic the DS's look.

![](img/fix_ph_link.png)
