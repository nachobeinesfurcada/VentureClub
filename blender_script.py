
import bpy

# Load the 3D card model
bpy.ops.import_scene.obj(filepath="/Users/Nacho/Desktop/VentureClub/3dmodel/3d_card.obj")

# Get the material of the card
card_material = bpy.data.materials["Card Material"]

# Load the generated image and add it as a texture
image_texture = bpy.data.textures.new('Card Texture', type='IMAGE')
image = bpy.data.images.load('path/to/generated_image.png')
image_texture.image = image
card_material.texture_slots.add().texture = image_texture

# Export the first frame
bpy.context.scene.frame_set(0)
bpy.ops.render.render(write_still=True, filepath='/Users/Nacho/Desktop/VentureClub/output/first_frame.png')

# Export the rotating animation
bpy.context.scene.frame_set(0)
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.filepath = '/Users/Nacho/Desktop/VentureClub/output/card_animation.mp4'
bpy.context.scene.render.fps = 30
bpy.ops.render.render(animation=True)
