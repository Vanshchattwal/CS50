# import matplotlib.font_manager as fm
# from PIL import ImageFont
# font_name = "Arial"
# font_file = fm.findfont(fm.FontProperties(family=font_name))
# font = ImageFont.truetype(font_file, size=18)

# Import the Pillow modules
from PIL import Image, ImageDraw, ImageFont

# Import pandas to read and process the data file
import pandas as pd

# Open the template image file
template = Image.open("template.png")

# Read the data file
data = pd.read_csv("data.csv")

# Loop through each row of the data file
for index, row in data.iterrows():
    # Extract the name, registration number, and image of each participant
    name = row["name"]
    reg_no = row["registration number"]
    image = row["image"]

    # Create an ImageDraw object to draw on the template image
    draw = ImageDraw.Draw(template)

    # Add text to the template image using Arial font and black color
    font = ImageFont.truetype("arial.ttf", 32)
    draw.text((10, 10), f"{name} ({reg_no})", fill="black", font=font)

    # Add image to the template image and resize it to fit within a 200x200 pixel box
    participant_image = Image.open(image)
    participant_image.thumbnail((200, 200))
    width, height = participant_image.size
    x = (template.width - width) // 2
    y = (template.height - height) // 2
    template.paste(participant_image, (x, y))

    # Save the edited image as a new file with the registration number as the name
    filename = f"{reg_no}.png"
    template.save(filename)

# Print a message when the loop is done
print("All images have been edited and saved.")