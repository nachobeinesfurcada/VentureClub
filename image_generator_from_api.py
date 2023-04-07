# script that generates a card from an API request
# works



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
    font_path = "/Users/Nacho/Downloads/Helvetica-Font 2/Helvetica.ttf"  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, size=40)
    draw.text((50, 50), f"{company_name} {image_date}", fill='white', font=font)

    #save image locally
    os.system(f"")
    # Save the generated image temporarily
    card_path = os.path.join(os.getcwd(), '/Users/Nacho/Desktop/VentureClub/input/'+company_name+'.png')
    image.save(card_path)


    return "Success!"

if __name__ == '__main__':
    app.run()
