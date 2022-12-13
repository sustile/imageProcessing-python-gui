import math

from PIL import Image, ImageFilter, ImageEnhance
import os, sys
import tkinter
from tkinter import filedialog

# CONVERT IMAGES
def convertImage(path,toType,originalFileName):
    try:
        with Image.open(path) as file:
            savePath = tkinter.filedialog.askdirectory(title="Save Location")
            if "\\" in originalFileName:
                originalFileName = originalFileName.split("\\")[-1]
            elif "/" in originalFileName:
                originalFileName = originalFileName.split("/")[-1]
            print(originalFileName)
            outPath = savePath + "/" + originalFileName[:-3] + toType
            print(outPath)
            file.save(outPath)
            print("----------------------------------------------------------------------")
            print("File Saved")
            print("----------------------------------------------------------------------")
    except:
        print("----------------------------------------------------------------------")
        print("Cannot Convert File")
        print("----------------------------------------------------------------------")
        return "ERROR"


# DETECT EDGES IN AN IMAGE
def detectEdges(path, skip = False):
    try:
        with Image.open(path) as file:
            # file = file.convert("L")
            file = file.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0))
            if skip:
                file.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return saveFile(file, path)

    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong edge")
        print("----------------------------------------------------------------------")
        return "ERROR"


# CREATE LOW RES IMAGES
def reduceImages(path, skip = False, threshold = 0):
    # try:
        if threshold == 0:
            while True:
                threshold = int(input("Please Enter a Threshold to Reduce the Image to : "))
                if threshold <= 0 or threshold >10:
                    print("Please Enter a Value from 1 to 10")
                else:
                    break
        with Image.open(path) as file:
            threshold = math.floor(threshold)
            if threshold == 0:
                return
            file = file.reduce(threshold)
            if skip:
                file.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return {
                "image" : saveFile(file, path),
                "value" : threshold
            }
    # except:
    #     print("----------------------------------------------------------------------")
    #     print("Something went Wrong")
    #     print("----------------------------------------------------------------------")
    #     return "ERROR"

# FLIP IMAGES
def flipImages(path, skip = False, value = 0):
    try:
        filterArray = [Image.FLIP_LEFT_RIGHT, Image.FLIP_TOP_BOTTOM,Image.ROTATE_90,Image.ROTATE_180,Image.ROTATE_270,Image.TRANSPOSE,Image.TRANSVERSE]
        filterArrayNames = ["Mirror", "Top to Bottom", "Rotate 90 degrees", "Rotate 180 degrees", "Rotate 270 degrees", "Transpose", "Transverse"]

        if value == 0:
            while True:
                value = int(input("Please Specify How to Flip this Image\nMirror (1)\nTop to Bottom (2)\nRotate 90 degrees (3)\nRotate 180 degrees (4)\nRotate 270 degrees (5)\nTranspose (6)\nTransverse (7)\nEnter : "))
                if value <=0 or value >7:
                    print("Please Enter a Value from 1 to 7")
                else:
                    break
        else:
            value = filterArrayNames.index(value) + 1
        with Image.open(path) as file:
            file = file.transpose(filterArray[value - 1])
            if skip:
                file.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return {
                "image" : saveFile(file, path),
                "value" : filterArrayNames[value - 1]
            }

    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def filter_grayscale(path, skip = False):
    try:
        with Image.open(path) as file:
            file = file.convert("L")
            if skip:
                file.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return saveFile(file,path)

    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def filter_red(path, skip = False):
    try:
        with Image.open(path) as img:
            red, green, blue = img.split()
            zeroed_band = red.point(lambda _: 0)
            red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
            if skip:
                img.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return saveFile(red_merge,path)

    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def filter_blue(path, skip = False):
    try:
        with Image.open(path) as img:
            red, green, blue = img.split()
            zeroed_band = blue.point(lambda _: 0)
            red_merge = Image.merge("RGB", (zeroed_band, zeroed_band,blue))
            if skip:
                img.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return saveFile(red_merge,path)

    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def filter_green(path, skip = False):
    try:
        with Image.open(path) as img:
            red, green, blue = img.split()
            zeroed_band = green.point(lambda _: 0)
            red_merge = Image.merge("RGB", (zeroed_band, green,zeroed_band))
            if skip:
                img.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return saveFile(red_merge,path)

    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def filter_boxBlur(path, skip = False, threshold = 0):
    try:
        if threshold == 0:
            while True:
                threshold = int(input("Please Enter a Threshold to Blur The Image : "))
                if threshold <= 0 or threshold >100:
                    print("Please Enter a Value from 1 to 100")
                else:
                    break
        threshold = math.floor(threshold)
        if threshold == 0:
            return
        with Image.open(path) as img:
            img = img.filter(ImageFilter.BoxBlur(threshold))
            if skip:
                img.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return {
                "image" : saveFile(img, path),
                "value" : threshold
            }
    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def filter_gaussianBlur(path, skip = False, threshold = 0):
    try:
        if threshold == 0:
            while True:
                threshold = int(input("Please Enter a Threshold to Blur The Image : "))
                if threshold <= 0 or threshold >100:
                    print("Please Enter a Value from 1 to 100")
                else:
                    break

        threshold = math.floor(threshold)
        if threshold == 0:
            return
        with Image.open(path) as img:
            img = img.filter(ImageFilter.GaussianBlur(threshold))
            if skip:
                img.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return {
                "image" : saveFile(img, path),
                "value" : threshold
            }
    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def filter_sharpen(path, skip = False):
    try:
        with Image.open(path) as img:
            img = img.filter(ImageFilter.SHARPEN)
            if skip:
                img.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            img.show()
            return saveFile(img,path)
    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def filter_smooth(path, skip = False):
    try:
        with Image.open(path) as img:
            img = img.filter(ImageFilter.SMOOTH)
            if skip:
                img.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return saveFile(img,path)
    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def filter_emboss(path, skip = False):
    try:
        with Image.open(path) as img:
            img = img.filter(ImageFilter.EMBOSS)
            if skip:
                img.save("tempUpdateFile." + str(path.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(path.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return saveFile(img,path)
    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def saveFile(file,path):
        file.save("tempFile."+str(path.split("/")[-1]).split(".")[1])
        print("----------------------------------------------------------------------")
        print("State Saved")
        print("----------------------------------------------------------------------")
        return "tempFile."+str(path.split("/")[-1]).split(".")[1]

def enhancement_brightness(file, skip = False, value = 1):
    try:
        if value == 1:
            while True:
                value = float(input("Please Enter a Threshold to Brighten The Image : "))
                if value <= 0 or value > 10:
                    print("Please Enter a Value from 1 to 10")
                else:
                    break

        value = math.floor(value)
        if value == 1:
            return
        with Image.open(file) as img:
            x = ImageEnhance.Brightness(img)
            newImg = x.enhance(value)
            if skip:
                img.save("tempUpdateFile." + str(file.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(file.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return {
                "image" : saveFile(newImg, file),
                "value" : value
            }
    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def enhancement_contrast(file, skip = False, value = 1):
    try:
        if value == 1:
            while True:
                value = float(input("Please Enter a Threshold to Enhance the Contrast The Image : "))
                if value <= 0 or value > 10:
                    print("Please Enter a Value from 1 to 10")
                else:
                    break

        value = math.floor(value)
        if value == 1:
            return
        with Image.open(file) as img:
            x = ImageEnhance.Contrast(img)
            newImg = x.enhance(value)
            if skip:
                img.save("tempUpdateFile." + str(file.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(file.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return {
                "image" : saveFile(newImg, file),
                "value" : value
            }
    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def enhancement_color(file, skip = False, value = 1):
    try:
        if value == 1:
            while True:
                value = float(input("Please Enter a Threshold to Enhance the Color The Image : "))
                if value <= 0 or value > 10:
                    print("Please Enter a Value from 1 to 10")
                else:
                    break

        value = math.floor(value)
        if value == 1:
            return
        with Image.open(file) as img:
            x = ImageEnhance.Color(img)
            newImg = x.enhance(value)
            if skip:
                img.save("tempUpdateFile." + str(file.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(file.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return {
                "image" : saveFile(newImg, file),
                "value" : value
            }
    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def enhancement_sharpness(file, skip = False, value = 1):
    try:
        if value == 1:
            while True:
                value = float(input("Please Enter a Threshold to Sharpen The Image : "))
                if value <= 0 or value > 20:
                    print("Please Enter a Value from 1 to 20")
                else:
                    break

        value = math.floor(value)
        if value == 1:
            return
        with Image.open(file) as img:
            x = ImageEnhance.Sharpness(img)
            newImg = x.enhance(value)
            if skip:
                img.save("tempUpdateFile." + str(file.split("/")[-1]).split(".")[1])
                return "tempUpdateFile." + str(file.split("/")[-1]).split(".")[1]
            print("----------------------------------------------------------------------")
            return {
                "image" : saveFile(newImg, file),
                "value" : value
            }
    except:
        print("----------------------------------------------------------------------")
        print("Something went Wrong")
        print("----------------------------------------------------------------------")
        return "ERROR"

def erode(cycles, image):
     for _ in range(cycles):
          image = image.filter(ImageFilter.MinFilter(3))
     return image


def dilate(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.MaxFilter(3))
    return image

filterListPreset = [{"name" : "Edge Detection", "function" : detectEdges},{"name" : "Reduce Resolution", "function" : reduceImages},{"name" : "GrayScale", "function" : filter_grayscale},{"name" : "RedMix", "function" : filter_red},{"name" : "Blue", "function" : filter_blue},{"name" : "Green", "function" : filter_green},{"name" : "Box Blur", "function" : filter_boxBlur},{"name" : "Gaussian Blur", "function" : filter_gaussianBlur},{"name" : "Sharpen", "function" : filter_sharpen},{"name" : "Smooth", "function" : filter_smooth},{"name" : "Emboss", "function" : filter_emboss},{"name" : "Brightness", "function" : enhancement_brightness},{"name" : "Contrast", "function" : enhancement_contrast},{"name" : "Sharpness", "function" : enhancement_sharpness},{"name" : "Color", "function" : enhancement_color}]
filterListFlipImages = ["Mirror", "Top to Bottom", "Rotate 90 degrees", "Rotate 180 degrees", "Rotate 270 degrees", "Transpose", "Transverse"]

def updateFilters(filterList, file):
    try:
            for i in filterList:
                if i in filterListFlipImages:
                    file = flipImages(file, True, i)
                    continue
                elif i == "RedColor":
                    file = filter_red(file, True)
                    continue
                for j in filterListPreset:
                    if j["name"] == i:
                        file = j["function"](file, True)
                    elif j["name"].__contains__(i.split(" ")[0]):
                        file = j["function"](file, True, int(i.split(" ")[-1]))

            return file
    except:
        print("Something went Wrong Over here")
        return "ERROR"
