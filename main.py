import bpy
import os
import json
from datetime import date

# Set up the scene and camera
scene = bpy.context.scene
camera = scene.camera

# Set up the card object and material
card = bpy.data.objects['Card']
material = card.active_material
material.node_tree.nodes['Image Texture'].image = bpy.data.images.load('/path/to/your/image.png')

# Set up the animation
animation = bpy.data.actions.new('SpinAnimation')
rotation = animation.fcurves.new('rotation_euler', index=2)
rotation.keyframe_points.add(61)
for i in range(61):
    rotation.keyframe_points[i].co = (i, i * 6, 0, 0)

# Render the first frame
scene.frame_set(1)
bpy.ops.render.render(write_still=True)

# Export the video
def export_video(company_name, today):
    bpy.context.scene.render.fps = 30
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.image_settings.codec = 'H264'
    file_name = f"{company_name}_{today}.mp4"
    bpy.context.scene.render.filepath = os.path.join('/Users/Nacho/Desktop/ventureclub/output', file_name)
    bpy.context.scene.render.use_file_extension = False
    bpy.context.scene.render.use_overwrite = True
    bpy.context.scene.frame_end = 61
    bpy.ops.render.render(animation=True)

# Load the data from the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Generate the card and video
export_video(data['company'], str(date.today()))
print('Card and video generated successfully.')