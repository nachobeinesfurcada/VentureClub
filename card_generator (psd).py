"""from flask import Flask, request
import json
from datetime import datetime
import os
import requests
import urllib.request
import shutil
import subprocess
import time
from PIL import Image, ImageDraw, ImageFont




# Initialize Flask app
app = Flask(__name__)

# Define endpoint for receiving data from Venture Club
@app.route('/venture_club', methods=['POST'])
def venture_club():
    # Get data from the JSON request
    data = request.get_json()

    # Get company name and current date
    company_name = data['company_name']
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Generate image using existing template
    with open('/Users/Nacho/Desktop/VentureClub/emptycard.png', 'rb') as f:
        template_data = f.read()

    # Replace placeholder text with company name and current date
    template_data = template_data.replace(b'COMPANY_NAME', company_name.encode('utf-8'))
    template_data = template_data.replace(b'CURRENT_DATE', current_date.encode('utf-8'))

    # Save the generated image
    with open('path/to/generated_image.png', 'wb') as f:
        f.write(template_data)

    # Open Blender scene and add texture to 3D card model
    blender_script = '''
import bpy

# Load the 3D card model
bpy.ops.import_scene.obj(filepath="path/to/3d_card.obj")

# Get the material of the card
card_material = bpy.data.materials["Card Material"]

# Load the generated image and add it as a texture
image_texture = bpy.data.textures.new('Card Texture', type='IMAGE')
image = bpy.data.images.load('path/to/generated_image.png')
image_texture.image = image
card_material.texture_slots.add().texture = image_texture

# Export the first frame
bpy.context.scene.frame_set(0)
bpy.ops.render.render(write_still=True, filepath='path/to/first_frame.png')

# Export the rotating animation
bpy.context.scene.frame_set(0)
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.filepath = 'path/to/card_animation.mp4'
bpy.context.scene.render.fps = 30
bpy.ops.render.render(animation=True)
'''

    # Save Blender script to file
    with open('path/to/blender_script.py', 'w') as f:
        f.write(blender_script)

    # Export the 3D card animation
    subprocess.call(['blender', '-b', '-P', 'path/to/blender_script.py'])

    # Upload the generated files to a remote server
    upload_files('path/to/generated_image.png')
    upload_files('path/to/first_frame.png')
    upload_files('path/to/card_animation.mp4')

    # Delete temporary files
    os.remove('path/to/generated_image.png')
    os.remove('path/to/first_frame.png')
    os.remove('path/to/card_animation.mp4')

    return 'Success'

def upload_files(file_path):
    # Upload file to remote server using requests module
    with open(file_path, 'rb') as f:
        r = requests.post('http://remote_server/upload', files={'file': f})
    if r.status_code == 200:
        print(f'Successfully uploaded {file_path} to remote server.')
    else:
        print(f'Failed to upload {file_path} to remote server. Status code: {r.status_code}')

if __name__ == '__main__':
    app.run()
"""