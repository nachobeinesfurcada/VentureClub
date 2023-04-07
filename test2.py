from flask import Flask, request
import os
import json
import datetime
import bpy
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# Define the endpoint for receiving data from the Venture Club API
@app.route('/receive_data', methods=['POST'])
def receive_data():
    # Get the data from the request
    data = request.json

    # Load the input image
    image_path = "/Users/Nacho/Desktop/VentureClub/input/emptycard.png"  # Replace with the path to your input image
    image = Image.open(image_path)

    # Add text to the image
    company_name = data['company_name']
    image_date = datetime.datetime.now().strftime("%d/%m/%Y")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=40)
    draw.text((50, 50), f"{company_name} {image_date}", fill='black', font=font)

    #save image locally
    os.system(f"cp card.png /Users/Nacho/Desktop/VentureClub/input")
    # Save the generated image temporarily
    card_path = os.path.join(os.getcwd(), 'card.png')

    # Open a Blender scene with bpy
    blend_file = os.path.join(os.getcwd(), 'card.blend')
    with bpy.data.libraries.load(blend_file) as (data_from, data_to):
        data_to.scenes = data_from.scenes

    # Use the generated image as a texture for the element that they indicate
    bpy.data.images.load(card_path)
    bpy.data.images['card.png'].pack()

    # Export the first frame
    bpy.context.scene.frame_set(1)
    bpy.ops.render.render(write_still=True)

    # save exported image locally
    bpy.data.images['Render Result'].save_render(filepath='/Users/Nacho/Desktop/VentureClub/output')

    # Export the scene with its camera animation
    bpy.ops.render.render(animation=True)
    #save the exported scene locally
    bpy.ops.render.render['Render Result'].save_render(filepath='/Users/Nacho/Desktop/VentureClub/output')

    # Delete all temporary files
    os.remove(card_path)

    return "Success!"

if __name__ == '__main__':
    app.run()
