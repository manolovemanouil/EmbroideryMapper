import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk
import image_to_color_array as eb

image_width = 400

rgb_palette = []

source_img = []

img_arr = []

result_img = []

window = tk.Tk()

window.geometry('1300x600')

def_img = Image.open("default_img.png")
def_img_tk = ImageTk.PhotoImage(image=def_img)

after_img = Image.open("output_def.png")
after_img_tk = ImageTk.PhotoImage(image=after_img)



window.title("EmbroideryMapper Alpha 1.0")

frame1 = tk.Frame(master=window)

frame2 = tk.Frame(master=frame1)

frame3 = tk.Frame(master=frame1)

label = tk.Label(master=frame1, text="Enter Width Below")

pic1_label = tk.Label(master=frame3, image=def_img_tk)

pic2_label = tk.Label(master=frame3, image=after_img_tk)

color_selection = tk.Listbox(master=frame3)
color_selection.insert()

def select_image_button():
    global source_img
    filename = filedialog.askopenfilename(initialdir='./',
                                             title= "Select image",
                                             filetypes = [("Image files",
                                                           "*.jpg")])
    selected_image = Image.open(filename)

    source_img = selected_image

    print(filename)
    selected_image = eb.resize_image_to_width(selected_image, image_width)
    selected_image_tk = ImageTk.PhotoImage(image=selected_image)
    pic1_label.config(image= selected_image_tk)
    pic1_label.image = selected_image_tk


button_select_img = tk.Button(
    master=frame3,
    text="Select Image",
    width=25,
    height=5,
    command=select_image_button
)

def process_image_button():
    global source_img
    global img_arr
    global result_img
    global rgb_palette

    if not source_img:
        return
    resize_width = entry_width.get()

    print(type(resize_width))

    width, height = source_img.size

    resized_img = eb.resize_image_to_width(source_img, int(resize_width))

    img_arr = eb.resized_image_to_array(resized_img)

    assigned_arr = eb.assign_color_num(img_arr, rgb_palette)

    result_img = eb.from_assigned_to_img(assigned_arr, rgb_palette)

    upscaled = eb.resize_image_to_width(result_img, image_width)
    upscaled_tk = ImageTk.PhotoImage(image=upscaled)
    pic2_label.config(image=upscaled_tk)
    pic2_label.image = upscaled_tk






button_process_image = tk.Button(
    master=frame3,
    text= "Process Image",
    width=20,
    height=5,
    command=process_image_button
)


colors = tk.Label(master=frame2, text= "Colors Appear Here", wraplength=600)

entry_width = tk.Entry(master=frame1, width=20)
label_red = tk.Label(master=frame2, text="Red: ")
entry_red = tk.Entry(master=frame2, width=10)
label_green = tk.Label(master=frame2, text="Green: ")
entry_green = tk.Entry(master=frame2, width=10)
label_blue = tk.Label(master=frame2, text="Blue: ")
entry_blue = tk.Entry(master=frame2, width=10)

def add_rgb_data():
    color_entry = [int(entry_red.get()), int(entry_green.get()), int(entry_blue.get())]
    rgb_palette.append(color_entry)

    color_text = str(rgb_palette).replace('], [', '],\n[')

    colors.config(text=str(color_text))
    colors.text = color_text

    entry_red.delete(0,'end')
    entry_green.delete(0,'end')
    entry_blue.delete(0,'end')

button_rgb = tk.Button(
    master=frame2,
    text="Add Color RGB",
    width=20,
    height=3,
    command=add_rgb_data

)

label.grid(row=0, column=0)
button_select_img.grid(row=0, column=0)
button_process_image.grid(row=0, column=1)
entry_width.grid(row=1, column=0)
label_red.grid(row=0, column=2)
entry_red.grid(row=0, column=3)
label_green.grid(row=1, column=2)
entry_green.grid(row=1, column=3)
label_blue.grid(row=2, column=2)
entry_blue.grid(row=2, column=3)
pic1_label.grid(row=1, column=0)
pic2_label.grid(row=1, column=1)
button_rgb.grid(row=3,column=3)
colors.grid(row=4, column=3)
frame2.grid(row=1, column=3)
frame3.grid(row=1, column=1)

frame1.pack()

window.mainloop()