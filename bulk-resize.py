import PIL
import os
import os.path
import pyfiglet
from PIL import Image

title = pyfiglet.figlet_format("Image Resize")

print(title)

print("This program will take a directory and loop through the images\n and resize them to specified dimensions.\n")
print("Disclaimer: This script will resize based on the width and height\n dimensions provided and will not keep images in aspect ratio.\n")

directory = input("Paste the directory here:\n")

width = input("Input the width:")
height = input("Input the height:\n")

ext = ('png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG') 

for file in os.listdir(directory):
    if file.endswith(ext):
        f_img = directory+"/"+file
        print(f"Resizing {file}")
        img = Image.open(f_img)
        img = img.resize((int(width),int(height)))
        img.save(f_img)
        print(f"Succesfull resize of {file}\n")
    