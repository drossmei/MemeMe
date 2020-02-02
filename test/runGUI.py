import tkinter as tk
from tkinter import Tk, BOTTOM, messagebox
from tkinter.ttk import Label, Combobox, Button
from openCV import main, data

# initialize tkinter
root = Tk()
root.title("MemeMe")
root.geometry('350x450')

emotions = list(data.keys())
emotions.append('random')

#Intialize Title Label
titleLabel = Label(root, text="MemeMe", font=("Courier", 44))
titleLabel.pack()


#Initialize Weather Label
emotionLabel = Label(root, text="Enter Custom: ", font=("Courier", 20))
emotionLabel.pack(pady=10)


#Initialize Drop Down Menu
memeCombo = Combobox(root, state="readonly")
memeCombo['values'] = sorted(c for c in emotions)
memeCombo.current(0)
memeCombo.pack(pady=10)

def clicked():
    emot = memeCombo.get()
    main(emot)

#Initialize Meme Button 
memeBtn = Button(root, text="Memeify", width=20, command=clicked)
memeBtn.pack(pady=10)


#Initialize Exit Button
exitBtn = Button(root, text='Exit', width=20, command=root.destroy)
exitBtn.pack(side=BOTTOM, pady=50)


root.mainloop()