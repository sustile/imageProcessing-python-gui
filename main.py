import tkinter
from turtledemo.__main__ import font_sizes

from customtkinter import CTk
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import filedialog,PhotoImage

import model
from model import *

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

# INIT VALUES
originalFile = ""
imageObject = 0
imagePath = PATH + "\pochita.png"
currentFilters = []
# INIT VALUES


# HELPER FUNCTIONS
def load_image(path, image_size):
    return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))
# HELPER FUNCTIONS

window = CTk()
# window.geometry("1920x1080")
window.resizable(False, True)
window.state("zoomed")
window.title("Image Processing")

# window.grid_rowconfigure(0, weight=1)
# window.grid_rowconfigure(1, weight=2)

mainFrame = customtkinter.CTkFrame(window)

mainFrame.grid(row=0, column=0)
mainFrame.grid_columnconfigure(0, weight=1)
mainFrame.grid_columnconfigure(1, weight=1)
# mainFrame.pack(ipadx=20,ipady=20,fill="both", expand=True)
mainFrame.pack_propagate(False)
mainFrame.pack(padx=20,pady=20,fill="both", expand=True, ipadx=40, ipady=60)

# mainFrame.configure(height=330, width=mainFrame["width"])

# FUNCTIONS


def convertImage():
    window3 = customtkinter.CTkToplevel(window)
    window3.title("Convert Image")
    window3.grid_columnconfigure(0, weight=1)
    window3.grid_columnconfigure(1, weight=1)

    convertImagesFrame = customtkinter.CTkFrame(window3)
    convertImagesFrame.pack(expand=True,anchor=customtkinter.CENTER, ipady=20, padx=40, pady=40)

    png = customtkinter.CTkButton(master=convertImagesFrame, text="PNG",
                                              width=100,
                                              compound="right", fg_color=("#ddd", "gray25"), hover_color="#f72585",
                                              text_font=("Roboto Mono", 10), corner_radius=20)
    png.pack( ipadx=40, ipady=10, side=customtkinter.LEFT, padx=20)

    jpg = customtkinter.CTkButton(master=convertImagesFrame, text="JPG",
                                              width=100,
                                              compound="right", fg_color=("#ddd", "gray25"), hover_color="#f72585",
                                              text_font=("Roboto Mono", 10), corner_radius=20,command=lambda : model.convertImage(imagePath, "jpg", originalFile))
    jpg.pack(side=customtkinter.RIGHT, ipadx=40, ipady=10, padx=20)


def ChangeImages():
    global imageObject, originalFile, imagePath
    file = filedialog.askopenfilename(title="Select an Image", filetypes=(("PNG", "*.png"), ("JPG", "*.jpg")))
    image = Image.open(file)
    originalFile = file
    imagePath = file
    image.thumbnail((500, 500), Image.BICUBIC)
    imageCon = ImageTk.PhotoImage(image)
    imageObject.configure(image=imageCon)
    imageObject.image = imageCon
    resetVals()

def edgeDetect():
    global currentFilters, imagePath
    if checkFilterIfExists("Edge Detection"):
        edgeDetection.configure(fg_color=("#ddd", "gray25"))
        if currentFilters.__contains__("Edge Detection"):
            currentFilters.remove("Edge Detection")
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()
    else:
        returnedFile = model.detectEdges(imagePath)
        if returnedFile != "ERROR":
            imagePath = returnedFile
            currentFilters.append("Edge Detection")
            currentFilters = list(set(currentFilters))
            updateImage()
            edgeDetection.configure(fg_color=("#ddd", "#8338ec"))

def emboss():
    global currentFilters, imagePath
    if checkFilterIfExists("Emboss"):
        embossBtn.configure(fg_color=("#ddd", "gray25"))
        if currentFilters.__contains__("Emboss"):
            currentFilters.remove("Emboss")
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()
    else:
        returnedFile = model.filter_emboss(imagePath)
        if returnedFile != "ERROR":
            imagePath = returnedFile
            currentFilters.append("Emboss")
            currentFilters = list(set(currentFilters))
            updateImage()
            embossBtn.configure(fg_color=("#ddd", "#8338ec"))

def grayscale():
    global currentFilters, imagePath
    if checkFilterIfExists("GrayScale"):
        GrayscaleBtn.configure(fg_color=("#ddd", "gray25"))
        if currentFilters.__contains__("GrayScale"):
            currentFilters.remove("GrayScale")
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()
    else:
        returnedFile = model.filter_grayscale(imagePath)
        if returnedFile != "ERROR":
            imagePath = returnedFile
            currentFilters.append("GrayScale")
            currentFilters = list(set(currentFilters))
            updateImage()
            GrayscaleBtn.configure(fg_color=("#ddd", "#8338ec"))

def red():
    global currentFilters, imagePath
    if checkFilterIfExists("RedMix"):
        redBtn.configure(fg_color=("#ddd", "gray25"))
        if currentFilters.__contains__("RedMix"):
            currentFilters.remove("RedMix")
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()
    else:
        returnedFile = model.filter_red(imagePath)
        if returnedFile != "ERROR":
            imagePath = returnedFile
            currentFilters.append("RedMix")
            currentFilters = list(set(currentFilters))
            updateImage()
            redBtn.configure(fg_color=("#ddd", "#8338ec"))

def blue():
    global currentFilters, imagePath
    if checkFilterIfExists("Blue"):
        blueBtn.configure(fg_color=("#ddd", "gray25"))
        if currentFilters.__contains__("Blue"):
            currentFilters.remove("Blue")
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()
    else:
        returnedFile = model.filter_blue(imagePath)
        if returnedFile != "ERROR":
            imagePath = returnedFile
            currentFilters.append("Blue")
            currentFilters = list(set(currentFilters))
            updateImage()
            blueBtn.configure(fg_color=("#ddd", "#8338ec"))

def green():
    global currentFilters, imagePath
    if checkFilterIfExists("Green"):
        greenBtn.configure(fg_color=("#ddd", "gray25"))
        if currentFilters.__contains__("Green"):
            currentFilters.remove("Green")
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()
    else:
        returnedFile = model.filter_green(imagePath)
        if returnedFile != "ERROR":
            imagePath = returnedFile
            currentFilters.append("Green")
            currentFilters = list(set(currentFilters))
            updateImage()
            greenBtn.configure(fg_color=("#ddd", "#8338ec"))

def smooth():
    global currentFilters, imagePath
    if checkFilterIfExists("Smooth"):
        smoothBtn.configure(fg_color=("#ddd", "gray25"))
        if currentFilters.__contains__("Smooth"):
            currentFilters.remove("Smooth")
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()
    else:
        returnedFile = model.filter_smooth(imagePath)
        if returnedFile != "ERROR":
            imagePath = returnedFile
            currentFilters.append("Smooth")
            currentFilters = list(set(currentFilters))
            updateImage()
            smoothBtn.configure(fg_color=("#ddd", "#8338ec"))

def boxBlur():
    global currentFilters, imagePath
    val = math.floor(boxBlurSlider.get())
    if val != 0:
        returnedFile = model.filter_boxBlur(imagePath, threshold=val)
        if returnedFile != "ERROR":
            imagePath = returnedFile["image"]
            currentFilters.append(f"Box Blur {returnedFile['value']}")
            currentFilters = list(set(currentFilters))
            updateImage()
            boxBlurBtn.configure(fg_color=("#ddd", "#8338ec"))
    else:
            if checkFilterIfExists("Box Blur"):
                boxBlurBtn.configure(fg_color=("#ddd", "gray25"))
                currentFilters.remove(findIndex("Box Blur"))
                if len(currentFilters) == 0:
                        imagePath = originalFile
                        updateImage()
                else:
                        result = model.updateFilters(currentFilters, originalFile)
                        if result != "ERROR":
                            imagePath = result
                            updateImage()

def gaussianBlur():
    global currentFilters, imagePath
    val = math.floor(gaussianBlurSlider.get())
    if val != 0:
        returnedFile = model.filter_gaussianBlur(imagePath, threshold=val)
        if returnedFile != "ERROR":
            imagePath = returnedFile["image"]
            currentFilters.append(f"Gaussian Blur {returnedFile['value']}")
            currentFilters = list(set(currentFilters))
            updateImage()
            gaussianBlurBtn.configure(fg_color=("#ddd", "#8338ec"))
        else:
            gaussianBlurBtn.configure(fg_color=("#ddd", "gray25"))
    else:
        if checkFilterIfExists("Gaussian Blur"):
            gaussianBlurBtn.configure(fg_color=("#ddd", "gray25"))
            currentFilters.remove(findIndex("Gaussian Blur"))
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()

def reduceImages():
    global currentFilters, imagePath
    val = math.floor(reduceResSlider.get())
    if val != 0:
        returnedFile = model.reduceImages(imagePath, threshold=val)
        if returnedFile != "ERROR":
            imagePath = returnedFile["image"]
            currentFilters.append(f"Reduce Resolution {returnedFile['value']}")
            currentFilters = list(set(currentFilters))
            updateImage()
            reduceResolution.configure(fg_color=("#ddd", "#8338ec"))
    else:
        if checkFilterIfExists("Reduce Resolution"):
            reduceResolution.configure(fg_color=("#ddd", "gray25"))
            currentFilters.remove(findIndex("Reduce Resolution"))
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()

def brightness():
    global currentFilters, imagePath
    val = math.floor(brightnessBtnSlider.get())
    if val != 1:
        returnedFile = model.enhancement_brightness(imagePath, value=val)
        if returnedFile != "ERROR":
            imagePath = returnedFile["image"]
            currentFilters.append(f"Brightness {returnedFile['value']}")
            currentFilters = list(set(currentFilters))
            updateImage()
            brightnessBtn.configure(fg_color=("#ddd", "#8338ec"))
    else:
        if checkFilterIfExists("Brightness"):
            brightnessBtn.configure(fg_color=("#ddd", "gray25"))
            currentFilters.remove(findIndex("Brightness"))
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()

def contrast():
    global currentFilters, imagePath
    val = math.floor(contrastBtnSlider.get())
    if val != 1:
        returnedFile = model.enhancement_contrast(imagePath, value=val)
        if returnedFile != "ERROR":
            imagePath = returnedFile["image"]
            currentFilters.append(f"Contrast {returnedFile['value']}")
            currentFilters = list(set(currentFilters))
            updateImage()
            contrastBtn.configure(fg_color=("#ddd", "#8338ec"))
    else:
        if checkFilterIfExists("Contrast"):
            contrastBtn.configure(fg_color=("#ddd", "gray25"))
            currentFilters.remove(findIndex("Contrast"))
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()


def sharpness():
    global currentFilters, imagePath
    val = math.floor(sharpnessBtnSlider.get())
    if val != 1:
        returnedFile = model.enhancement_sharpness(imagePath, value=val)
        if returnedFile != "ERROR":
            imagePath = returnedFile["image"]
            currentFilters.append(f"Sharpness {returnedFile['value']}")
            currentFilters = list(set(currentFilters))
            updateImage()
            sharpnessBtn.configure(fg_color=("#ddd", "#8338ec"))
    else:
        if checkFilterIfExists("Sharpness"):
            sharpnessBtn.configure(fg_color=("#ddd", "gray25"))
            currentFilters.remove(findIndex("Sharpness"))
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()

def color():
    global currentFilters, imagePath
    val = math.floor(colorBtnSlider.get())
    if val != 1:
        returnedFile = model.enhancement_color(imagePath, value=val)
        if returnedFile != "ERROR":
            imagePath = returnedFile["image"]
            currentFilters.append(f"Color {returnedFile['value']}")
            currentFilters = list(set(currentFilters))
            updateImage()
            colorBtn.configure(fg_color=("#ddd", "#8338ec"))
    else:
        if checkFilterIfExists("Color"):
            colorBtn.configure(fg_color=("#ddd", "gray25"))
            currentFilters.remove(findIndex("Color"))
            if len(currentFilters) == 0:
                imagePath = originalFile
                updateImage()
            else:
                result = model.updateFilters(currentFilters, originalFile)
                if result != "ERROR":
                    imagePath = result
                    updateImage()



def saveFile():
    global  imagePath
    with Image.open(imagePath) as fileObj:
        savePath = tkinter.filedialog.askdirectory(title="Save Location")
        outPath = savePath + "/" + imagePath.split("/")[-1]
        fileObj.save(outPath)
        print("----------------------------------------------------------------------")
        print("File Saved")
        print("----------------------------------------------------------------------")
#FUNCTIONS

# HELPER FUNCTIONS
def updateImage():
    global imageObject, originalFile, imagePath
    image = Image.open(imagePath)
    image.thumbnail((500, 500), Image.BICUBIC)
    imageCon = ImageTk.PhotoImage(image)
    imageObject.configure(image=imageCon)
    imageObject.image = imageCon

def resetVals():
    global currentFilters
    currentFilters = []
    reduceResSlider.set(0)
    boxBlurSlider.set(0)
    gaussianBlurSlider.set(0)
    brightnessBtnSlider.set(1)
    contrastBtnSlider.set(1)
    sharpnessBtnSlider.set(1)
    colorBtnSlider.set(1)

def checkFilterIfExists(x):
    found = False
    for i in currentFilters:
        if x in i:
            found = True
    return found

def findIndex(x):
    for i in range(0, len(currentFilters)):
        if x in currentFilters[i]:
            return currentFilters[i]

def flipImages():
    def mirror():
        global currentFilters, imagePath
        if checkFilterIfExists("Mirror"):
            mirrorBtn.configure(fg_color=("#ddd", "gray25"))
            if currentFilters.__contains__("Mirror"):
                currentFilters.remove("Mirror")
                if len(currentFilters) == 0:
                    imagePath = originalFile
                    updateImage()
                else:
                    result = model.updateFilters(currentFilters, originalFile)
                    if result != "ERROR":
                        imagePath = result
                        updateImage()
        else:
            returnedFile = model.flipImages(imagePath, value="Mirror")
            if returnedFile != "DONT-UPDATE":
                imagePath = returnedFile["image"]
                currentFilters.append(returnedFile["value"])
                currentFilters = list(set(currentFilters))
                updateImage()
                mirrorBtn.configure(fg_color=("#ddd", "#8338ec"))

    def topToBottom():
        global currentFilters, imagePath
        if checkFilterIfExists("Top to Bottom"):
            topToBottomBtn.configure(fg_color=("#ddd", "gray25"))
            if currentFilters.__contains__("Top to Bottom"):
                currentFilters.remove("Top to Bottom")
                if len(currentFilters) == 0:
                    imagePath = originalFile
                    updateImage()
                else:
                    result = model.updateFilters(currentFilters, originalFile)
                    if result != "ERROR":
                        imagePath = result
                        updateImage()
        else:
            returnedFile = model.flipImages(imagePath, value="Top to Bottom")
            if returnedFile != "DONT-UPDATE":
                imagePath = returnedFile["image"]
                currentFilters.append(returnedFile["value"])
                currentFilters = list(set(currentFilters))
                updateImage()
                topToBottomBtn.configure(fg_color=("#ddd", "#8338ec"))

    def rotate90deg():
        global currentFilters, imagePath
        if checkFilterIfExists("Rotate 90 degrees"):
            rotate90.configure(fg_color=("#ddd", "gray25"))
            if currentFilters.__contains__("Rotate 90 degrees"):
                currentFilters.remove("Rotate 90 degrees")
                if len(currentFilters) == 0:
                    imagePath = originalFile
                    updateImage()
                else:
                    result = model.updateFilters(currentFilters, originalFile)
                    if result != "ERROR":
                        imagePath = result
                        updateImage()
        else:
            returnedFile = model.flipImages(imagePath, value="Rotate 90 degrees")
            if returnedFile != "DONT-UPDATE":
                imagePath = returnedFile["image"]
                currentFilters.append(returnedFile["value"])
                currentFilters = list(set(currentFilters))
                updateImage()
                rotate90.configure(fg_color=("#ddd", "#8338ec"))

    def rotate180deg():
        global currentFilters, imagePath
        if checkFilterIfExists("Rotate 180 degrees"):
            rotate180.configure(fg_color=("#ddd", "gray25"))
            if currentFilters.__contains__("Rotate 180 degrees"):
                currentFilters.remove("Rotate 180 degrees")
                if len(currentFilters) == 0:
                    imagePath = originalFile
                    updateImage()
                else:
                    result = model.updateFilters(currentFilters, originalFile)
                    if result != "ERROR":
                        imagePath = result
                        updateImage()
        else:
            returnedFile = model.flipImages(imagePath, value="Rotate 180 degrees")
            if returnedFile != "DONT-UPDATE":
                imagePath = returnedFile["image"]
                currentFilters.append(returnedFile["value"])
                currentFilters = list(set(currentFilters))
                updateImage()
                rotate180.configure(fg_color=("#ddd", "#8338ec"))

    def rotate270deg():
        global currentFilters, imagePath
        if checkFilterIfExists("Rotate 270 degrees"):
            rotate270.configure(fg_color=("#ddd", "gray25"))
            if currentFilters.__contains__("Rotate 270 degrees"):
                currentFilters.remove("Rotate 270 degrees")
                if len(currentFilters) == 0:
                    imagePath = originalFile
                    updateImage()
                else:
                    result = model.updateFilters(currentFilters, originalFile)
                    if result != "ERROR":
                        imagePath = result
                        updateImage()
        else:
            returnedFile = model.flipImages(imagePath, value="Rotate 270 degrees")
            if returnedFile != "DONT-UPDATE":
                imagePath = returnedFile["image"]
                currentFilters.append(returnedFile["value"])
                currentFilters = list(set(currentFilters))
                updateImage()
                rotate270.configure(fg_color=("#ddd", "#8338ec"))

    def transposeFlip():
        global currentFilters, imagePath
        if checkFilterIfExists("Transpose"):
            transpose.configure(fg_color=("#ddd", "gray25"))
            if currentFilters.__contains__("Transpose"):
                currentFilters.remove("Transpose")
                if len(currentFilters) == 0:
                    imagePath = originalFile
                    updateImage()
                else:
                    result = model.updateFilters(currentFilters, originalFile)
                    if result != "ERROR":
                        imagePath = result
                        updateImage()
        else:
            returnedFile = model.flipImages(imagePath, value="Transpose")
            if returnedFile != "DONT-UPDATE":
                imagePath = returnedFile["image"]
                currentFilters.append(returnedFile["value"])
                currentFilters = list(set(currentFilters))
                updateImage()
                transpose.configure(fg_color=("#ddd", "#8338ec"))

    def transverseFlip():
        global currentFilters, imagePath
        if checkFilterIfExists("Transverse"):
            transverse.configure(fg_color=("#ddd", "gray25"))
            if currentFilters.__contains__("Transverse"):
                currentFilters.remove("Transverse")
                if len(currentFilters) == 0:
                    imagePath = originalFile
                    updateImage()
                else:
                    result = model.updateFilters(currentFilters, originalFile)
                    if result != "ERROR":
                        imagePath = result
                        updateImage()
        else:
            returnedFile = model.flipImages(imagePath, value="Transverse")
            if returnedFile != "DONT-UPDATE":
                imagePath = returnedFile["image"]
                currentFilters.append(returnedFile["value"])
                currentFilters = list(set(currentFilters))
                updateImage()
                transverse.configure(fg_color=("#ddd", "#8338ec"))

    window2 = customtkinter.CTkToplevel(window)
    window2.title("Flip Images")
    window2.grid_rowconfigure(0, weight=1)

    flipImagesFrame = customtkinter.CTkFrame(window2)
    flipImagesFrame.grid_rowconfigure(0 ,weight=1)
    flipImagesFrame.grid_rowconfigure(1 ,weight=1)

    flipImagesFrame.grid_columnconfigure(0, weight=1)
    flipImagesFrame.grid_columnconfigure(1, weight=1)
    flipImagesFrame.grid_columnconfigure(2, weight=1)
    flipImagesFrame.grid_columnconfigure(3, weight=1)
    flipImagesFrame.pack(expand=True,anchor=customtkinter.CENTER, ipadx=40, ipady=40, padx=40, pady=40)

    mirrorColor = "gray25"
    if checkFilterIfExists("Mirror") : mirrorColor = "#8338ec"
    mirrorBtn = customtkinter.CTkButton(master=flipImagesFrame, text="Mirror",
                                              width=100,
                                              compound="right", fg_color=("#ddd", mirrorColor), hover_color="#f72585",
                                              text_font=("Roboto Mono", 10), corner_radius=20,command=mirror)
    mirrorBtn.grid(row=0, column=0, ipadx=40, ipady=10)

    topBtmColor = "gray25"
    if checkFilterIfExists("Top to Bottom") : topBtmColor = "#8338ec"
    topToBottomBtn = customtkinter.CTkButton(master=flipImagesFrame, text="Top to Bottom",
                                              width=100,
                                              compound="right", fg_color=("#ddd", topBtmColor), hover_color="#f72585",
                                              text_font=("Roboto Mono", 10), corner_radius=20,command=topToBottom)
    topToBottomBtn.grid(row=0, column=1, ipadx=40, ipady=10)

    rot90color = "gray25"
    if checkFilterIfExists("Rotate 90") : rot90color = "#8338ec"
    rotate90 = customtkinter.CTkButton(master=flipImagesFrame, text="Rotate 90",
                                              width=100,
                                              compound="right", fg_color=("#ddd",rot90color), hover_color="#f72585",
                                              text_font=("Roboto Mono", 10), corner_radius=20, command=rotate90deg)
    rotate90.grid(row=0, column=2, ipadx=40, ipady=10)

    rot180color = "gray25"
    if checkFilterIfExists("Rotate 180") : rot180color = "#8338ec"
    rotate180 = customtkinter.CTkButton(master=flipImagesFrame, text="Rotate 180",
                                              width=100,
                                              compound="right", fg_color=("#ddd", rot180color), hover_color="#f72585",
                                              text_font=("Roboto Mono", 10), corner_radius=20, command=rotate180deg)
    rotate180.grid(row=0, column=3, ipadx=40, ipady=10)

    rot270color = "gray25"
    if checkFilterIfExists("Rotate 270") : rot270color = "#8338ec"
    rotate270 = customtkinter.CTkButton(master=flipImagesFrame, text="Rotate 270",
                                              width=100,
                                              compound="right", fg_color=("#ddd", rot270color), hover_color="#f72585",
                                              text_font=("Roboto Mono", 10), corner_radius=20, command=rotate270deg)
    rotate270.grid(row=1, column=0, ipadx=40, ipady=10)

    transposecolor = "gray25"
    if checkFilterIfExists("Transpose") : transposecolor = "#8338ec"
    transpose = customtkinter.CTkButton(master=flipImagesFrame, text="Transpose",
                                              width=100,
                                              compound="right", fg_color=("#ddd", transposecolor), hover_color="#f72585",
                                              text_font=("Roboto Mono", 10), corner_radius=20, command=transposeFlip)
    transpose.grid(row=1, column=1, ipadx=40, ipady=10)

    transverseColor = "gray25"
    if checkFilterIfExists("Transverse") : transverseColor = "#8338ec"
    transverse = customtkinter.CTkButton(master=flipImagesFrame, text="Transverse",
                                              width=100,
                                              compound="right", fg_color=("#ddd", transverseColor), hover_color="#f72585",
                                              text_font=("Roboto Mono", 10), corner_radius=20, command=transverseFlip)
    transverse.grid(row=1, column=2, ipadx=40, ipady=10)

# HELPER FUNCTIONS


# ---------------------------
# GUI
#----------------------------

# SET DEFAULT IMAGE


image = Image.open(imagePath)
image.thumbnail((500,500), Image.BICUBIC)
imageCon = ImageTk.PhotoImage(image)
imageObject = customtkinter.CTkLabel(master = mainFrame, image=imageCon)
# imageObject.grid(row = 0, column = 0, padx = 20, pady = 20)
imageObject.pack(side=customtkinter.LEFT, anchor=customtkinter.CENTER,fill=customtkinter.BOTH,expand=True)

originalFile = imagePath


# SET DEFAULT IMAGE

#OPEN FOLDER BTN
folderFrame = customtkinter.CTkFrame(mainFrame)
folderFrame.pack(side=customtkinter.RIGHT,anchor=customtkinter.CENTER,expand=True,ipadx=20)
folderFrame.rowconfigure(0, weight=1)
folderFrame.rowconfigure(1, weight=1)
open_folder_icon = load_image("/Icons/folder-open.png", 35)
open_folder_btn = customtkinter.CTkButton(master=folderFrame, image=open_folder_icon, text="Change Image ", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20, command=ChangeImages)


open_folder_btn.pack( ipadx=20, ipady=5,side=customtkinter.TOP,pady=30, padx=20)

saveImage_icon = load_image("/Icons/floppy-disk.png", 35)
saveImage = customtkinter.CTkButton(master=folderFrame, text="Save Image ", image=saveImage_icon, width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=saveFile)

saveImage.pack( ipadx=20, ipady=5, pady=20)

convertImage_icon = load_image("/Icons/arrows-clockwise.png", 35)
convertImage = customtkinter.CTkButton(master=folderFrame, text="Convert Image ", width=100, image=convertImage_icon,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20, command=convertImage)

convertImage.pack( ipadx=20, ipady=5,side=customtkinter.BOTTOM, pady=30)


#OPEN FOLDER BTN

# FILTERS CONT INIT
filters_cont_frame = customtkinter.CTkFrame(master=window)
filters_cont_frame.grid_columnconfigure(0, weight=1)
filters_cont_frame.grid_columnconfigure(1, weight=1)
filters_cont_frame.grid_columnconfigure(2, weight=1)
filters_cont_frame.grid_columnconfigure(3, weight=1)
filters_cont_frame.grid_columnconfigure(4, weight=1)

filters_cont_frame.grid_rowconfigure(0, weight=1)
filters_cont_frame.grid_rowconfigure(1, weight=1)
filters_cont_frame.grid_rowconfigure(2, weight=1)
filters_cont_frame.pack(padx=40,pady=40,fill="both", expand=True)

# FILTERS CONT INIT

# FILTERS CONT BUTTONS
edgeDetection = customtkinter.CTkButton(master=filters_cont_frame, text="Edge Detection", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=edgeDetect)
edgeDetection.grid(row=0, column = 0,padx = 20, pady = 20,ipadx=10, ipady=10)

reduce_resFrame = customtkinter.CTkFrame(filters_cont_frame)
reduce_resFrame.rowconfigure(0, weight=1)
reduce_resFrame.rowconfigure(1, weight=1)
reduce_resFrame.columnconfigure(0, weight=1)
reduce_resFrame.grid(row=0, column = 1, ipadx = 20, ipady = 40)
reduceResolution = customtkinter.CTkButton(master=reduce_resFrame, text="Reduce Resolution", width=100,
                                        compound="right",fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20, command=reduceImages)
reduceResolution.grid(row=0, column = 0,ipadx=10, ipady=10)
reduceResSlider = customtkinter.CTkSlider(master=reduce_resFrame, from_=0, to=10,number_of_steps=1)
reduceResSlider.set(0)
reduceResSlider.grid(row=1, column = 0)

flipImages_icon = load_image("/Icons/caret-double-right.png", 25)
flipImages = customtkinter.CTkButton(master=filters_cont_frame, image=flipImages_icon,text="Flip Images", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20, command=flipImages)
flipImages.grid(row=0, column = 2,padx = 20, pady = 20,ipadx=10, ipady=10)


embossBtn = customtkinter.CTkButton(master=filters_cont_frame, text="Emboss", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=emboss)
embossBtn.grid(row=0, column = 3,padx = 20, pady = 20,ipadx=10, ipady=10)

GrayscaleBtn = customtkinter.CTkButton(master=filters_cont_frame, text="Grayscale", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=grayscale)
GrayscaleBtn.grid(row=0, column = 4,padx = 20, pady = 20,ipadx=10, ipady=10)

redBtn = customtkinter.CTkButton(master=filters_cont_frame, text="Red", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=red)
redBtn.grid(row=1, column = 0,padx = 20, pady = 20,ipadx=10, ipady=10)

greenBtn = customtkinter.CTkButton(master=filters_cont_frame, text="Green", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=green)
greenBtn.grid(row=1, column = 1,padx = 20, pady = 20,ipadx=10, ipady=10)

blueBtn = customtkinter.CTkButton(master=filters_cont_frame, text="Blue", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20, command=blue)
blueBtn.grid(row=1, column = 2,padx = 20, pady = 20,ipadx=10, ipady=10)

# BOX BLUR
boxBlueFrame = customtkinter.CTkFrame(master=filters_cont_frame)
boxBlueFrame.rowconfigure(0, weight=1)
boxBlueFrame.rowconfigure(1, weight=1)
boxBlueFrame.columnconfigure(0, weight=1)
boxBlueFrame.grid(row=1, column = 3, ipadx = 20, ipady = 40)
boxBlurBtn = customtkinter.CTkButton(master=boxBlueFrame, text="Box Blur", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=boxBlur)
boxBlurBtn.grid(row=0, column = 0,ipadx=10, ipady=10)

boxBlurSlider = customtkinter.CTkSlider(master=boxBlueFrame, from_=0, to=100, number_of_steps=1)
boxBlurSlider.set(0)
boxBlurSlider.grid(row=1, column = 0)

# BOX BLUR

# GAUSSAIN BLUR

gaussianBlurFrame = customtkinter.CTkFrame(master=filters_cont_frame)
gaussianBlurFrame.rowconfigure(0, weight=1)
gaussianBlurFrame.rowconfigure(1, weight=1)
gaussianBlurFrame.columnconfigure(0, weight=1)
gaussianBlurFrame.grid(row=1, column = 4, ipadx = 20, ipady = 40)

gaussianBlurBtn = customtkinter.CTkButton(master=gaussianBlurFrame, text="Gaussian Blur", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=gaussianBlur)
gaussianBlurBtn.grid(row=0, column = 0,ipadx=10, ipady=10)
gaussianBlurSlider = customtkinter.CTkSlider(master=gaussianBlurFrame, from_=0, to=100,number_of_steps=1)
gaussianBlurSlider.set(0)
gaussianBlurSlider.grid(row=1, column = 0)

# GAUSSAIN BLUR

smoothBtn = customtkinter.CTkButton(master=filters_cont_frame, text="Smooth", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=smooth)
smoothBtn.grid(row=2, column = 0,padx = 20, pady = 20,ipadx=10, ipady=10)

brightnessBtnFrame = customtkinter.CTkFrame(master=filters_cont_frame)
brightnessBtnFrame.rowconfigure(0, weight=1)
brightnessBtnFrame.rowconfigure(1, weight=1)
brightnessBtnFrame.columnconfigure(0, weight=1)
brightnessBtnFrame.grid(row=2, column = 1, ipadx = 20, ipady = 40)

brightnessBtn = customtkinter.CTkButton(master=brightnessBtnFrame, text="Brightness", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=brightness)
brightnessBtn.grid(row=0, column = 0,ipadx=10, ipady=10)

brightnessBtnSlider = customtkinter.CTkSlider(master=brightnessBtnFrame, from_=1, to=10,number_of_steps=1)
brightnessBtnSlider.set(1)
brightnessBtnSlider.grid(row=1, column = 0)

contrastBtnFrame = customtkinter.CTkFrame(master=filters_cont_frame)
contrastBtnFrame.rowconfigure(0, weight=1)
contrastBtnFrame.rowconfigure(1, weight=1)
contrastBtnFrame.columnconfigure(0, weight=1)
contrastBtnFrame.grid(row=2, column = 2, ipadx = 20, ipady = 40)

contrastBtn = customtkinter.CTkButton(master=contrastBtnFrame, text="Contrast", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20, command=contrast)
contrastBtn.grid(row=0, column = 0,ipadx=10, ipady=10)

contrastBtnSlider = customtkinter.CTkSlider(master=contrastBtnFrame, from_=1, to=10,number_of_steps=1)
contrastBtnSlider.set(1)
contrastBtnSlider.grid(row=1, column = 0)

sharpnessBtnFrame = customtkinter.CTkFrame(master=filters_cont_frame)
sharpnessBtnFrame.rowconfigure(0, weight=1)
sharpnessBtnFrame.rowconfigure(1, weight=1)
sharpnessBtnFrame.columnconfigure(0, weight=1)
sharpnessBtnFrame.grid(row=2, column = 3, ipadx = 20, ipady = 40)

sharpnessBtn = customtkinter.CTkButton(master=sharpnessBtnFrame, text="Sharpness", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20, command=sharpness)
sharpnessBtn.grid(row=0, column = 0,ipadx=10, ipady=10)

sharpnessBtnSlider = customtkinter.CTkSlider(master=sharpnessBtnFrame, from_=1, to=20,number_of_steps=1)
sharpnessBtnSlider.set(1)
sharpnessBtnSlider.grid(row=1, column = 0)

colorBtnFrame = customtkinter.CTkFrame(master=filters_cont_frame)
colorBtnFrame.rowconfigure(0, weight=1)
colorBtnFrame.rowconfigure(1, weight=1)
colorBtnFrame.columnconfigure(0, weight=1)
colorBtnFrame.grid(row=2, column = 4, ipadx = 20, ipady = 40)

colorBtn = customtkinter.CTkButton(master=colorBtnFrame, text="Color", width=100,
                                        compound="right", fg_color=("#ddd", "gray25"),hover_color="#f72585", text_font=("Roboto Mono", 15), corner_radius=20,command=color)
colorBtn.grid(row=0, column = 0,ipadx=10, ipady=10)

colorBtnSlider = customtkinter.CTkSlider(master=colorBtnFrame, from_=1, to=10,number_of_steps=1)
colorBtnSlider.set(1)
colorBtnSlider.grid(row=1, column = 0)
# FILTERS CONT BUTTONS

# functions

window.mainloop()