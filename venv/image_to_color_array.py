import numpy as np
import PIL
from PIL import Image

def resize_image_to_width(img, width):
    #img is PIL Image
    #returns a PIL.Image object



    widthpct = (width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(widthpct)))
    img = img.resize((width, hsize), PIL.Image.ANTIALIAS)

    return img


def resized_image_to_array(img):

    return np.asarray(img)

def dist_in_3d(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)


def assign_color_num(pixel_arr, color_selection_arr):

    assign_arr = np.zeros(shape=(pixel_arr.shape[0],pixel_arr.shape[1]))

    for x, row in enumerate(pixel_arr):
        for y, val in enumerate(row):
            color_dist = [dist_in_3d(val, i) for i in color_selection_arr]
            closest = color_dist.index(min(color_dist))

            assign_arr[x, y] = closest

    return assign_arr


def from_assigned_to_img(pixel_arr, color_selection_arr):
    image_array = np.zeros(shape=(pixel_arr.shape[0],pixel_arr.shape[1],3))

    for x, row in enumerate(pixel_arr):
        for y, val in enumerate(row):
            print(val)
            image_array[x, y] = color_selection_arr[int(val)]
    image_array = image_array.astype(np.uint8)
    #print(image_array)
    #print(image_array.shape)
    ret_img = Image.fromarray(image_array, mode='RGB')

    return ret_img


'''

img = Image.open('landscape.jpg')

img_arr = resized_image_to_array(img)

print("done with array")

color_palette = [[0,0,0], [64,64,64], [128,128,128], [192,192,192],[255,255,255]]

reassigned = assign_color_num(img_arr, color_palette)

print("done assigning")

new_img = from_assigned_to_img(reassigned, color_palette)

new_img.save("grayscalelandscape.jpg")
'''


'''

image = resize_image_to_width("wave.jpg", 100)

image.save("resized_wave_2.jpg")

imarr = resized_image_to_array(image)

print(imarr)
print(imarr.shape)
print(type(imarr[0,0,1]))

testim = Image.fromarray(imarr)
testim.save("test1.jpg")




color_palette = [[0,0,0], [128,128,128], [255,255,255]]




reassigned = assign_color_num(imarr, color_palette)

print(reassigned)



new_img = from_assigned_to_img(reassigned,color_palette)

new_img.save("reassigntest1.jpg")

print(np.asarray(new_img))

'''


