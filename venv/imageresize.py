import PIL
from PIL import Image

width = 300

img = Image.open("wave.jpg")

widthpct = (width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(widthpct)))
img = img.resize((width, hsize), PIL.Image.ANTIALIAS)
img.save("resized_wave.jpg")


def resize_image_to_width(imgpath, width):

    #returns a PIL.Image object


    img = Image.open(imgpath)

    widthpct = (width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(widthpct)))
    img = img.resize((width, hsize), PIL.Image.ANTIALIAS)

    return img
