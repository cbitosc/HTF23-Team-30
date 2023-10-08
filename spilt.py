import os
from PIL import Image

# Open the image
image = Image.open("uploads/image (2).png")

# Get the width and height of the image
width, height = image.size

# Calculate the height of each part
part_height = height // 11

# Create a folder to save the horizontal parts
if not os.path.exists("horizontal_parts"):
    os.makedirs("horizontal_parts")

# Loop through and crop the image into 10 horizontal parts
for i in range(11):
    top = i * part_height
    bottom = (i + 1) * part_height
    horizontal_part = image.crop((0, top, width, bottom))
    
    # Create a folder for each horizontal part
    horizontal_part_folder = os.path.join("horizontal_parts", f"part_{i + 1}")
    if not os.path.exists(horizontal_part_folder):
        os.makedirs(horizontal_part_folder)
    
    # Calculate the width of each vertical subpart
    subpart_width = width // 8
    
    # Split the horizontal part into 5 vertical subparts
    for j in range(8):
        left = j * subpart_width
        right = (j + 1) * subpart_width
        vertical_subpart = horizontal_part.crop((left, 0, right, part_height))
        
        # Save each vertical subpart in the corresponding folder
        vertical_subpart.save(os.path.join(horizontal_part_folder, f"subpart_{j + 1}.png"))

# Close the original image
image.close()
