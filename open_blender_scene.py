# this code generates a blender scene from scratch, puts a monkey
# inside and a lamp, and saves it as a .blend file
# works


import bpy
import os

# set the output folder and file name
folder_path = "/Users/Nacho/Desktop/VentureClub/scene"
file_name = "my_scene"

# check how many files are already in the folder
num_existing_files = sum([1 for f in os.listdir(folder_path) if f.startswith(file_name)])

# if there are existing files, append a number to the file name
if num_existing_files > 0:
    file_name = f"{file_name}{num_existing_files+1}"

# set the output file path
output_path = os.path.join(folder_path, f"{file_name}.blend")

# create a new scene
new_scene = bpy.ops.scene.new(type='NEW')
scene = bpy.context.scene

# create a camera and set it as active
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 10), rotation=(0, 0, 0))
camera = bpy.context.object
scene.camera = camera

# position the camera
camera.location = (0, 0, 5)
camera.rotation_euler = (0, 0, 0)

#### place object HERE


# create a lamp
lamp_data = bpy.data.lights.new(name="lamp", type='POINT')
lamp_object = bpy.data.objects.new(name="lamp", object_data=lamp_data)
bpy.context.scene.collection.objects.link(lamp_object)

# position the lamp
lamp_object.location = (5, 5, 5)

# set the lamp energy
lamp_data.energy = 1000


# set up the render settings
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = os.path.join(folder_path, f"{file_name}.png")

# render the image
bpy.ops.render.render(write_still=True)

# save the scene
bpy.ops.wm.save_as_mainfile(filepath=output_path)

# close Blender
bpy.ops.wm.quit_blender()
