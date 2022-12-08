from turtledemo.__main__ import font_sizes

from customtkinter import CTk
import customtkinter
from PIL import Image, ImageTk
import os

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# HELPER FUNCTIONS
def load_image(path, image_size):
    return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))
# HELPER FUNCTIONS

window = CTk()
window.geometry("1920x1080")
# window.resizable(False,False)
window.state("zoomed")
window.title("Image Processing")

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=2)

mainFrame = customtkinter.CTkFrame(window)


mainFrame.grid(row=0, column=0)
mainFrame.grid_columnconfigure(0, weight=1)
mainFrame.grid_columnconfigure(1, weight=1)
mainFrame.pack(padx=200,pady=20,fill="both", expand=True)
mainFrame.configure(height=330, width=mainFrame["width"])
mainFrame.grid_propagate(0)


# SET DEFAULT IMAGE

image = Image.open(PATH + "\cat.png")
image.thumbnail((600,600), Image.ANTIALIAS)
imageCon = ImageTk.PhotoImage(image)
imageObject = customtkinter.CTkLabel(master = mainFrame, image=imageCon)
imageObject.grid(row = 0, column = 0, padx = 20, pady = 20)

# SET DEFAULT IMAGE

#OPEN FOLDER BTN
open_folder_icon = load_image("/Icons/folder-open.png", 35)
open_folder_btn = customtkinter.CTkButton(master=mainFrame, image=open_folder_icon, text="Change Image ", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 20), corner_radius=20)
open_folder_btn.grid(row=0, column = 1,padx = 20, pady = 20,ipadx=20, ipady=20)

#OPEN FOLDER BTN

# FILTERS CONT INIT
filters_cont_frame = customtkinter.CTkFrame(master=window)
# filters_cont_frame.grid(row = 1, column = 0)
# filters_cont_frame.grid_columnconfigure(0, weight=2)
# filters_cont_frame.grid_columnconfigure(1, weight=1)
filters_cont_frame.pack(padx=40,pady=40,fill="both", expand=True)
# FILTERS CONT INIT

# FILTERS CONT BUTTONS
edgeDetection = customtkinter.CTkButton(master=filters_cont_frame, text="Edge Detection", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
edgeDetection.grid(row=0, column = 0,padx = 20, pady = 20,ipadx=20, ipady=20)

commonImageManipulation = customtkinter.CTkButton(master=filters_cont_frame, text="Common Image Manipulation Tools", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
commonImageManipulation.grid(row=0, column = 1,padx = 20, pady = 20,ipadx=20, ipady=20)

filtersBtn = customtkinter.CTkButton(master=filters_cont_frame, text="Filters", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
filtersBtn.grid(row=0, column = 2,padx = 20, pady = 20,ipadx=20, ipady=20)

imageEnchancements = customtkinter.CTkButton(master=filters_cont_frame, text="Image enhancements", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
imageEnchancements.grid(row=0, column = 3,padx = 20, pady = 20,ipadx=20, ipady=20)


# currFiltersAndTools = customtkinter.CTkButton(master=filters_cont_frame, text="Currently Applied Filters and Tools", width=100,
#                                         compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
# currFiltersAndTools.grid(row=1, column = 0,padx = 20, pady = 20,ipadx=20, ipady=20)

emboss = customtkinter.CTkButton(master=filters_cont_frame, text="Emboss", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
emboss.grid(row=0, column = 4,padx = 20, pady = 20,ipadx=20, ipady=20)

Grayscale = customtkinter.CTkButton(master=filters_cont_frame, text="Grayscale", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
Grayscale.grid(row=1, column = 0,padx = 20, pady = 20,ipadx=20, ipady=20)

red = customtkinter.CTkButton(master=filters_cont_frame, text="Red", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
red.grid(row=1, column = 1,padx = 20, pady = 20,ipadx=20, ipady=20)

green = customtkinter.CTkButton(master=filters_cont_frame, text="Green", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
green.grid(row=1, column = 2,padx = 20, pady = 20,ipadx=20, ipady=20)

blue = customtkinter.CTkButton(master=filters_cont_frame, text="Blue", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
blue.grid(row=1, column = 3,padx = 20, pady = 20,ipadx=20, ipady=20)

boxBlur = customtkinter.CTkButton(master=filters_cont_frame, text="Box Blur", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
boxBlur.grid(row=1, column = 4,padx = 20, pady = 20,ipadx=20, ipady=20)

gaussianBlur = customtkinter.CTkButton(master=filters_cont_frame, text="Gaussian Blur", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
gaussianBlur.grid(row=2, column = 0,padx = 20, pady = 20,ipadx=20, ipady=20)

smooth = customtkinter.CTkButton(master=filters_cont_frame, text="Smooth", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#C77C78", text_font=("Roboto Mono", 15), corner_radius=20)
smooth.grid(row=2, column = 1,padx = 20, pady = 20,ipadx=20, ipady=20)
# FILTERS CONT BUTTONS

window.mainloop()