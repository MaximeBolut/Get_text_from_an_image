import tkinter
from tkinter import *

import pytesseract
import PIL
from PIL import Image, ImageGrab
import os
import keyboard

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


root=Tk()
root.title("Image 2 Text (by Maxime B)")
#root.iconbitmap('logo2crop.ico')
root.config(background='#2E4053')
masterframe=Frame(root,background='#2E4053', bd=2) 
masterframe.grid(row=1, columnspan=3)


def get_text():
    
    ok=0
    #this is to get the image that you've screenshot. Note that window+shit+s is awesome to select better what you want to screenshot
    im = ImageGrab.grabclipboard()
    
    if isinstance(im, Image.Image):
        ok= 1
    
    elif im:
       for filename in im:
           try:
               im = Image.open(filename)
           except IOError:
               pass # ignore this file
           else:
               ok=1
    
    else:
      T.insert(END,'clipboard empty, take a screenshot of something \n')
      ok=0
       
    #im.show()
    
    if ok==1:
      path= os.getcwd()
      path=path+str("\\image_saved.png")
      image_saved=im.save(path)
      
      text=pytesseract.image_to_string(path)
      T.insert(END, text)
    
      os.remove(path)



def clearing():
    T.delete('1.0', END)


def snapshot():
	keyboard.press_and_release('cmd + shift + s')


snap=Button(root, text= 'Make a snapshot', font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C', width=20, command= snapshot)
snap.grid(row=0, column=0)

go=Button(root, text= 'Get TEXT from snapshot!', font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C', width=20, command= get_text)
go.grid(row=0, column=1)

#go.pack()

clr=Button(root, text= 'Clear all', font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C', width=20, command= clearing)
clr.grid(row=0, column=2)

#clr.pack()

s = Scrollbar(masterframe)
T = Text(masterframe)

T.focus_set()
s.pack(side=RIGHT, fill=Y)
T.pack()
s.config(command=T.yview)
T.config(yscrollcommand=s.set)


root.mainloop()

'''
s = Scrollbar(root)
T = Text(root)

T.focus_set()
s.pack(side=RIGHT, fill=Y)
T.pack()
s.config(command=T.yview)
T.config(yscrollcommand=s.set)
'''