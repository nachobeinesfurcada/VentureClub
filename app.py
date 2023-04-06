from flask import Flask, request
import json
from datetime import datetime
import os
import requests
import urllib.request
import shutil
import subprocess
import time
from PIL import Image, ImageDraw, ImageFont
import bpy
import blender


#define blender path
bpy.app.binary_path = "/Applications/Blender.app"


# Initialize Flask app
app = Flask(__name__)

# Define endpoint for receiving data from Venture Club
@app.route('/card', methods=['POST'])
def card():
    # Get data from the JSON request
    data = request.get_json()

    # Get company name and current date
    company_name = data['company_name']
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Load template image
    template = Image.open('/Users/Nacho/Desktop/VentureClub/input/emptycard.png')

    # set fontpath 
    font_path = "/System/Library/Fonts/Helvetica.ttc"

    # Create font object
    font = ImageFont.truetype(font_path, size=50)

    # Create drawing object
    draw = ImageDraw.Draw(template)

    # Replace placeholder text with company name and current date
    draw.text((100, 50), company_name, fill=(0, 0, 0), font=font)
    draw.text((100, 200), current_date, fill=(0, 0, 0), font=font)

    # Save the modified image
    template.save('card.png')

    # Open Blender scene and add texture to 3D card model
    blender_script = '''
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
'''

    # Save Blender script to file
    with open('/Users/Nacho/Desktop/VentureClub/blender_script.py', 'w') as f:
        f.write(blender_script)

    # Export the 3D card animation
    subprocess.call(['blender', '-b', '-P', '/Users/Nacho/Desktop/VentureClub/blender_script.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Upload the generated files to a remote server
    upload_files('/Users/Nacho/Desktop/VentureClub/output/generated_image.png')
    upload_files('/Users/Nacho/Desktop/VentureClub/output/first_frame.png')
    upload_files('/Users/Nacho/Desktop/VentureClub/output/card_animation.mp4')

    
    # Delete temporary files
    """
    os.remove('path/to/generated_image.png')
    os.remove('path/to/first_frame.png')
    os.remove('path/to/card_animation.mp4')
    """

    return 'Success'

@app.route('/upload', methods=['POST'])
def upload_files(file_path):
    # Upload file to remote server using requests module
    with open(file_path, 'rb') as f:
        r = requests.post('http://localhost:5000/upload', files={'file': f})
    if r.status_code == 200:
        print(f'Successfully uploaded {file_path} to remote server.')
        return 'Success'
    else:
        print(f'Failed to upload {file_path} to remote server. Status code: {r.status_code}')
        return 'Fail'

if __name__ == '__main__':
    app.run()
