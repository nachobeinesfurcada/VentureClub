import datetime
from PIL import Image, ImageDraw, ImageFont
import os

# Set up the image
width = 800
height = 600
img = Image.new('RGB', (width, height), color='black')
draw = ImageDraw.Draw(img)

# Set up the font
font_path = "/System/Library/Fonts/Helvetica.ttc"
font = ImageFont.truetype(font_path, size=60)
font_small = ImageFont.truetype(font_path, size=40)

# Set up the team logo
logo_path = "/Users/Nacho/Desktop/VentureClub/logoboca.png"
logo = Image.open(logo_path).resize((200, 200), resample=Image.BICUBIC)

# Set up the player photo
photo_path = "/Users/Nacho/Desktop/VentureClub/schiavi.jpg"
photo = Image.open(photo_path).resize((200, 200), resample=Image.BICUBIC)

# Set up the text
team_name = "Boca Juniors"
player_name = "Flaco Schiavi"
stats = "Goals: 10  Assists: 5"

# Draw the top stripe
top_stripe_height = height // 4
draw.rectangle((0, 0, width, top_stripe_height), fill='white')
img.paste(logo, (50, 50))

# Draw the bottom stripe
bottom_stripe_height = height // 4
draw.rectangle((0, height - bottom_stripe_height, width, height), fill='green')
img.paste(photo, (width - 250, height - 250))

# Draw the team name
team_name_bbox = draw.textbbox((0, 0), team_name, font=font)
team_name_x = (width - team_name_bbox[2]) // 2
team_name_y = (top_stripe_height - team_name_bbox[3]) // 2
draw.text((team_name_x, team_name_y), team_name, font=font, fill='black')

# Draw the player name and stats
player_name_bbox = draw.textbbox((0, 0), player_name, font=font)
stats_bbox = draw.textbbox((0, 0), stats, font=font_small)
player_info_padding = 20
player_info_x = width - stats_bbox[2] - player_info_padding
player_info_y = height - bottom_stripe_height + (bottom_stripe_height - player_name_bbox[3] - stats_bbox[3] - player_info_padding) // 2
draw.text((player_info_x, player_info_y), player_name, font=font, fill='white')
draw.text((player_info_x, player_info_y + player_name_bbox[3] + player_info_padding), stats, font=font_small, fill='white')

# Create the output directory if it doesn't exist
output_dir = "/Users/Nacho/Desktop/VentureClub/input"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the image
now = datetime.datetime.now()
filename = f"{team_name}_{player_name}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.png"
output_path = os.path.join(output_dir, filename)
img.save(output_path)

print(f"Image saved to {output_path}")

