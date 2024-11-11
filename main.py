import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

window=Tk()
window.config(width=900, height=900, bg=BACKGROUND_COLOR,padx=50,pady=50)

canv=Canvas(width=800, height=526)
front_img=PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")

card=canv.create_image(400,263,image=front_img)
canv.config(bg=BACKGROUND_COLOR, highlightthickness=0)
spanish=canv.create_text(400,263,text="Click any button", font=("Arial", 50, "bold"))
canv.grid(row=0, column=0, columnspan=2)

right_img=PhotoImage(file="images/right.png")
wrong_img=PhotoImage(file="images/wrong.png")

global num

wordlist=[[0,0] for _ in range(1000)]
data=pd.read_csv("words.csv")
df=data.to_dict(orient="records")
print(df)

for i in range(0,999):
    wordlist[i][0]=df[i]['sp']
    wordlist[i][1]=df[i]['en']

print(wordlist)

def right_ans():
    wordlist.remove(num)
    spanish_update()
def spanish_update():
    num = random.randint(0, 999)
    canv.itemconfig(card, image=front_img)
    canv.itemconfig(spanish, text=wordlist[num][0])
    window.after(3000, english_update,num)

def english_update(num):
    canv.itemconfig(card, image=back_img)
    canv.itemconfig(spanish, text=wordlist[num][1])


wrong=Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=spanish_update)
right=Button(image=right_img, highlightthickness=0, borderwidth=0, command=spanish_update)

wrong.grid(row=1, column=0)
right.grid(row=1, column=1)



window.mainloop()