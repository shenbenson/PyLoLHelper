import tkinter as tk
import math


def Table(canvas1):

    for i in range(2): 
        e = tk.Entry(canvas1, width=20, fg =("blue","red")[i is 0], font=('Arial',16,'bold')) 
        e.insert(tk.END, "Team " + str(i + 1))
        e.pack()
        for j in range(5):  
            e = tk.Entry(canvas1, width=20, fg=("blue","red")[i is 0], 
            font=('Arial',16,'bold')) 
            e.insert(tk.END, "Player: " + str(i * 5+ j + 1))
            e.pack()

def getSummoner ():  
    x1 = entry1.get()
    try:
        textOutput.set("Searched for Summoner:" + " " + x1)
        t = Table(root)
    except ValueError: ## if search cannot find summoner, execute
        textOutput.set("Error summoner not found")

root = tk.Tk()
root.title("PyLoLHelper - Search Page")

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
textOutput = tk.StringVar()
label1 = tk.Label(root, textvariable = textOutput)
canvas1.create_window(200, 230, window=label1)
title = tk.Label(root, fg="blue", font=("Impact", 24, 'bold'), text="PyLoLHelper")
canvas1.create_window(200, 20, window=title)
    
button1 = tk.Button(text='Search for Summoner', command=getSummoner)
canvas1.create_window(200, 180, window=button1)


root.mainloop()
