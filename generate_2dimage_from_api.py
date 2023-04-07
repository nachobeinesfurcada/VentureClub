from flask import Flask, request
import os
import json
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/generate_image', methods=['POST'])
def generate_image():
    # Parse the JSON data from the request
    data = request.json
    company_name = data['company_name']

    # Set up the image
    image_width = 500
    image_height = 500
    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)

    # Draw the company name on the image
    font_size = 36
    font = ImageFont.truetype('Helvetica', size=font_size)
    text_width, text_height = draw.textsize(company_name, font=font)
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2
    draw.text((x, y), company_name, fill='black', font=font)

    # place logo from json on image
    logo_path = data['logo_url']
    logo = Image.open(logo_path)
    logo_width, logo_height = logo.size
    logo = logo.resize((int(logo_width/2), int(logo_height/2)))
    image.paste(logo, (int(x), int(y+text_height)))
    
    # Save the image to disk
    filename = f"{company_name}.png"
    filepath = "/Users/Nacho/Desktop/VentureClub/output/" + filename
    image.save(filepath)

    # Return a success message
    return f"Image generated and saved as {filename}!"

if __name__ == '__main__':
    app.run()