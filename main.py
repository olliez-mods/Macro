import tkinter as tk
import os

from functions import *

def run_coms(num):
    coms = open("C:\\Users\\socks\\Desktop\\Python\\Macro\\Executer\\" + str(num) + ".txt", "r").read().split("\n")
    setStop(coms[0])
    del coms[0]
    run(coms)


root = tk.Tk()
helpButton = tk.Button(text="Help Me", command=lambda : os.startfile("help.txt"), width=30)

frameONE = tk.Frame(root)
buttonONE = tk.Button(frameONE, text="Start 1", command=lambda : run_coms(1), width=15)
editButtonONE = tk.Button(frameONE, text="Edit 1", command=lambda : os.startfile("C:\\Users\\socks\\Desktop\\Python\\Macro\\Executer\\1.txt"), width=15)

frameTWO = tk.Frame(root)
buttonTWO = tk.Button(frameTWO, text="Start 2", command=lambda : run_coms(2), width=15)
editButtonTWO = tk.Button(frameTWO, text="Edit 2", command=lambda : os.startfile("C:\\Users\\socks\\Desktop\\Python\\Macro\\Executer\\2.txt"), width=15)

frameTHREE = tk.Frame(root)
buttonTHREE = tk.Button(frameTHREE, text="Start 3", command=lambda : run_coms(3), width=15)
editButtonTHREE = tk.Button(frameTHREE, text="Edit 3", command=lambda : os.startfile("C:\\Users\\socks\\Desktop\\Python\\Macro\\Executer\\3.txt"), width=15)


helpButton.pack()

frameONE.pack()
buttonONE.pack(side="left")
editButtonONE.pack(side="left")

frameTWO.pack()
buttonTWO.pack(side="left")
editButtonTWO.pack(side="left")

frameTHREE.pack()
buttonTHREE.pack(side="left")
editButtonTHREE.pack(side="left")

root.mainloop()

