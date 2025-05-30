import tkinter as tk
import subprocess
from tkinter import ttk
import json

def open_settings():
    subprocess.Popen(["python", "settings.py"])

def load_settings():
    with open("Data/config.json", "r") as f:
        config = json.load(f)
    
    clear_points()

    points_to_draw = [
        config["start_point"],
        config["point_1"],
        config["point_2"],
        config["point_3"],
        config["point_4"]
    ]

    for pt in points_to_draw:
        x_str, y_str = pt.split(",")
        x = int(x_str.strip())
        y = int(y_str.strip())
        draw_point(x, y, "red")
    
    hsLabel.config(text=f"Horizontal Shift: {config["horizontal_shift"]}")
    answerCanvas.create_window(90, 55, window=hsLabel, anchor="w")
    vsLabel.config(text=f"Vertical Shift: {config["vertical_shift"]}")
    answerCanvas.create_window(90, 95, window=vsLabel, anchor="w")
    domainLabel.config(text=f"Domain: {config["domain"]}")
    answerCanvas.create_window(300, 15, window=domainLabel, anchor="w")
    rangeLabel.config(text=f"Range: {config["range"]}")
    answerCanvas.create_window(300, 55, window=rangeLabel, anchor="w")
    vertexLabel.config(text=f"Vertex: {config["vertex"]}")
    answerCanvas.create_window(90, 15, window=vertexLabel, anchor="w")

def draw_graph():
    for i in range(0, 32):
        lineInt = (i * (407//31)) + 2
        graphCanvas.create_line(lineInt, 0, lineInt, 407, fill="black")
        graphCanvas.create_line(407, lineInt, 0, lineInt, fill="black")

def draw_point(x, y, color):
    x *= 13
    x += 6
    y *= 13
    y += 6
    graphCanvas.create_oval(x-10, y-10, x+2, y+2, fill=color, outline=color, tags="graph_point")

def clear_points():
    graphCanvas.delete("graph_point")

root = tk.Tk()
root.title("Graph Functions")
root.geometry("550x700")
root.resizable(False, False)

settingsIcon = tk.PhotoImage(file="Images/SettingsIcon.png")
loadIcon = tk.PhotoImage(file="Images/LoadIcon.png")

titleCanvas = tk.Canvas(root, width=550, height=75)
titleCanvas.pack()

title = tk.Label(titleCanvas, text="Graph Functions", font=("Arial", 24, "bold"))
title.place(relx=0.5, rely=0.5, anchor="center")

loadButton = tk.Button(titleCanvas, image=settingsIcon, cursor="hand2", command=open_settings)
loadButton.place(relx=0.98, rely=0.35, anchor="e")

settingsButton = tk.Button(titleCanvas, image=loadIcon, cursor="hand2", command=load_settings)
settingsButton.place(relx=0.085, rely=0.35, anchor="e")

separator1 = ttk.Separator(root, orient='horizontal')
separator1.pack(fill='x', padx=20, pady=5)

graphCanvas = tk.Canvas(root, width=404, height=404)
graphCanvas.pack(pady=(20, 0))

separator2 = ttk.Separator(root, orient='horizontal')
separator2.pack(fill='x', padx=20, pady=(30, 5))

answerCanvas = tk.Canvas(root, width=475, height=115)
answerCanvas.pack(pady=(10, 0))

vertexLabel = tk.Label(answerCanvas, text="Vertex: ", font=("Arial", 10))
answerCanvas.create_window(90, 15, window=vertexLabel, anchor="w")

hsLabel = tk.Label(answerCanvas, text="Horizontal Shift: ", font=("Arial", 10))
answerCanvas.create_window(90, 55, window=hsLabel, anchor="w")

vsLabel = tk.Label(answerCanvas, text="Vertical Shift: ", font=("Arial", 10))
answerCanvas.create_window(90, 95, window=vsLabel, anchor="w")

domainLabel = tk.Label(answerCanvas, text="Domain: ", font=("Arial", 10))
answerCanvas.create_window(300, 15, window=domainLabel, anchor="w")

rangeLabel = tk.Label(answerCanvas, text="Range: ", font=("Arial", 10))
answerCanvas.create_window(300, 55, window=rangeLabel, anchor="w")

draw_graph()
root.mainloop()
