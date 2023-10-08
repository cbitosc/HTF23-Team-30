import os
from PIL import Image

# Open the image
image = Image.open("uploads/ybao.png")

# Get the width and height of the image
width, height = image.size

# Calculate the height of each part
part_height = height // 10

# Create a folder to save the parts
if not os.path.exists("output_folder"):
    os.makedirs("output_folder")

# Loop through and crop the image into 10 parts
for i in range(10):
    top = i * part_height
    bottom = (i + 1) * part_height
    part = image.crop((0, top, width, bottom))
    
    # Save each part in the output folder with a unique filename
    part.save(os.path.join("output_folder", f"part_{i + 1}.png"))

# Close the original image
image.close()