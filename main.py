import tkinter as esige
from tkinter import *
import requests
from tkinter import filedialog
from tkinter import font
from types import LambdaType
from tkinter.filedialog import askopenfile
import os
import argparse
from fileinput import filename
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import urllib.request
from urllib.request import Request, urlopen
import os
import re
from pytube import YouTube
from bs4 import BeautifulSoup
import nltk
import pandas as pd
from mutagen.mp4 import MP4, MP4Cover
from mutagen.flac import Picture, FLAC
from mutagen import File
import os
import argparse
from fileinput import filename
import re
import eyed3
from eyed3.id3.frames import ImageFrame
#novelty
import mutagen
from PIL import Image
from io import BytesIO

root = esige.Tk()

canvas = esige.Canvas(root, width = 300, height = 400)
canvas.grid(columnspan=3, rowspan=7)

random_text3 = esige.Label(root, text='No folder selected.', foreground=[('black')], font=('calibri',10,'bold'))
random_text3.grid(columnspan=3, column=0, row=5)
tittle = ""
artist = ""
def open_file():    
    file = filedialog.askdirectory()
    global txt
    global txtnoma
    
    txt=  str(file)
    txtnoma = txt.rsplit('/',1)[-1]
    #txtnomazaidi = txtnoma.rsplit('.',1)[-2]
    print(txtnoma)
    random_text3.config(text = txtnoma)

 
def open_files():    
        file = filedialog.askopenfile(title="Select Media file")
        global txt
        global txtnoma
        txt=  str(file.name)
        txtnoma = txt.rsplit('/',1)[-1]
        #txtnomazaidi = txtnoma.rsplit('.',1)[-2]
        print(txtnoma)
        random_text3.config(text = txtnoma)
        #esige.messagebox.showinfo("File Rename","Feature coming soon.")


def awesome():
    print(txt)
    
    for foldername, dirs, filenames in os.walk(txt):
          for filename in filenames:
               #if os.path.isfile(filename):
                      # continue

              #Video_File = os.path.join(txt, filename)
              Video_File = str(txt)+"/" +str(filename)
                
              print(filename)
              print("-------------------")
              print(Video_File)
              try:
                    download_cover(filename)
                    insert_cover2(Video_File, filename) 
                    # try:
                    #      insert_cover(Video_File)   
                    # except EXCEPTION as kbc:
                    #      insert_cover2(Video_File)  
              except Exception as e:
                  print("err for"+ filename)   
                  print("err being :"+str(e))      

                  #begining
     
     #end
     #esige.messagebox.showinfo("Hurray!","Renaming Completed.")

    
browse_text = esige.StringVar()

browse_btn = esige.Button(
             
             root,
             textvariable=browse_text,
             command=lambda:open_files(),
             height=2,
             width=15,background=[('grey')],font=('calibri',10,'bold'),foreground=[('brown')],
             
             )
browse_text.set("File Select")
browse_btn.grid(column=1, row=1)

browse_texty = esige.StringVar()
browse_btny = esige.Button(
             
             root,
             textvariable=browse_texty,
             command=lambda:open_file(),
             height=2,
             width=15,background=[('grey')],font=('calibri',10,'bold'),foreground=[('brown')],
             
             
             )
browse_texty.set("Folder Select")
browse_btny.grid(column=1, row=2)


random_text2 = esige.Label(root, text="Proceed",foreground=[('navyblue')])
random_text2.grid(columnspan=3, column=0, row=3)



watermark_text = esige.StringVar()
watermark_text.set("Set Covers")
watermark_btn = esige.Button(root, textvariable=watermark_text,bg='darkgrey',
                          
   command=lambda:  awesome()                                  
                                 , height=2, width=15,font=('calibri',13,'bold'),foreground=[('white')],background=[('green')],
                                    activebackground=[('white')], activeforeground=[('green')],
                                    
   
   )

watermark_btn.grid(column=1, row=4)

#clear button


clear_text = esige.StringVar()
clear_text.set("Clear")
clear_btn = esige.Button(root, textvariable=clear_text,bg='darkgrey',
     height=1, width=6,font=('calibri',10,'bold'),foreground=[('black')],background=[('grey')],
                                    activebackground=[('white')], activeforeground=[('green')],
                                    command=lambda:clear()
   
   )

clear_btn.grid(column=1,row=6)
#clear function

def download_cover(name):
     
     s_pam = re.sub("\s","+",name)

     link = "https://www.google.com/search?q="+s_pam+"&tbm=isch"

     req = Request(
                   url=link, 
                   headers={ 
                            'User-Agent': 'Mozilla/5.0'
                           }
                )

     data = urllib.request.urlopen(req)

     decoded_kinda = data.read().decode()

     pattern = "src=\"(.*?)\"."
     links = re.findall(pattern, decoded_kinda)

     urllib.request.urlretrieve(links[1], "cover.jpg")

def insert_cover(name):
        
        audio = MP3(name, ID3=ID3)
        print(audio.getall('APIC'))
        audio.tags.add(
                        APIC(
                                encoding=3,  # 3 is for utf-8
                                mime="image/jpeg",  # can be image/jpeg or image/jpeg
                                type=3,  # 3 is for the cover image
                                desc=u'Cover',
                                data=open("cover.jpeg", mode='wb').read()
                            )
                    )
        print(audio.getall('APIC'))
        audio.save(v2_version=3)  # save the current changes
        print("Cover added to "+name)
def insert_cover2(name,song_name):
        
        video = MP4(name)

        video["\xa9nam"] = "Test1"
        video["\xa9ART"] = "Test2"
        video["\xa9alb"] = "Test3"

        with open("cover.jpg", "rb") as f:
            video["covr"] = [
                MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)
            ]

        video.save(name)
        song_namer = song_name.replace(".mp3","")
        song_name_ = song_namer.strip()
        arry = song_name_.split("-")
        thee_len = len(arry)

        if thee_len < 2 :
            global tittle
            global artist
            artist = arry[0]        
            tittle = ""
            with open(name, 'r+b') as file:
                    media_file = mutagen.File(file, easy=True)
                    media_file['title'] = tittle
                    media_file['artist'] = artist
                    media_file.save(file)
        else :
       
            artist = arry[0]
            tittle = arry[1]

            with open(name, 'r+b') as file:
                    media_file = mutagen.File(file, easy=True)
                    media_file['title'] = tittle
                    media_file['artist'] = artist
                    media_file.save(file)

        print("Cover added to "+name)
def insert_cover22(name):
            mp3_path = name
            image_path = "C:/Users/Esige Ndagona/Desktop/py Image Download/cover.jpg"

            

            audiofile = eyed3.load(mp3_path)
            audiofile.tag.images.set(3, open("cover.jpg", "rb").read(), "image/jpeg")
            audiofile.tag.save()


            print("Cover added to "+name)
def insert_cover3(name):
    albumart = "cover.png"
    audio = File(filename)
        
    image = Picture()
    image.type = 3
    if albumart.endswith('png'):
        mime = 'image/png'
    else:
        mime = 'image/jpeg'
    image.desc = 'front cover'
    with open(albumart, 'rb') as f: # better than open(albumart, 'rb').read() ?
        image.data = f.read()
    
    audio.add_picture(image)
    audio.save()
    print("Cover added to "+name)

def insert_cover4(name):


          



       print("Cover added to "+name)

def insert_cover5(name):

    albumart = "cover.png"
    audio = MP4(name)
    data = open(albumart, 'rb').read()

    covr = []
    if albumart.endswith('png'):
        covr.append(MP4Cover(data, MP4Cover.FORMAT_PNG))
    else:
        covr.append(MP4Cover(data, MP4Cover.FORMAT_JPEG))

    audio.tags['covr'] = covr
    audio.save() 



    print("Cover added to "+name)

def clear():
    random_text3.config(text = '')
   

root.mainloop()
