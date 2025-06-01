import tkinter as tk
import subprocess
from tkinter import ttk
import json
import numpy as np

with open("Data/config.json", "r") as f:
        config = json.load(f)

config["vertex"] = "(0, 0)"
config["point_intersect"] = "(0, 0)"
config["h"] = "0"
config["k"] = "0"
config["domain"] = "[0, 0]"
config["range"] = "[0, 0]"
config["start_point"] = "0, 0"
config["point_1"] = "0, 0"
config["point_2"] = "0, 0"
config["point_3"] = "0, 0"
config["point_4"] = "0, 0"
config["point_5"] = "0, 0"
config["point_6"] = "0, 0"
config["function"] = "Quadratic"
config["posneg"] = "Positive"


with open("Data/config.json", "w") as f:
        json.dump(config, f, indent=4)

def open_settings():
    subprocess.Popen(["python", "settings.py"])

def load_settings():
    with open("Data/config.json", "r") as f:
        config = json.load(f)
    
    clear_points()
    clear_dashline()
    graph_nums(0, 0)

    if config["function"] == "Rational" or config["function"] == "Absolute Value":
        points_to_draw = [
            config["start_point"],
            config["point_1"],
            config["point_2"],
            config["point_3"],
            config["point_4"],
            config["point_5"],
            config["point_6"],
        ]
    else:
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
    
    Label1.config(text=f"POI/Vertex: {config["vertex"]}")
    answerCanvas.create_window(90, 15, window=Label1, anchor="w")
    Label2.config(text=f"Horizontal Shift: {config["h"]}")
    answerCanvas.create_window(90, 55, window=Label2, anchor="w")
    Label3.config(text=f"Vertical Shift: {config["k"]}")
    answerCanvas.create_window(90, 95, window=Label3, anchor="w")
    Label4.config(text=f"Domain: {config["domain"]}")
    answerCanvas.create_window(300, 15, window=Label4, anchor="w")
    Label5.config(text=f"Range: {config["range"]}")
    answerCanvas.create_window(300, 55, window=Label5, anchor="w")

    if config["function"] == "Cube Root":
        x_offset = int(config["h"])
        y_offset = -int(config["k"])
        Label1.config(text=f"P.O.I.: {config["point_intersect"]}")
        answerCanvas.create_window(90, 15, window=Label1, anchor="w")
        Label2.config(text=f"Horizontal Shift: {config["h"]}")
        answerCanvas.create_window(90, 55, window=Label2, anchor="w")
        Label3.config(text=f"Vertical Shift: {config["k"]}")
        answerCanvas.create_window(90, 95, window=Label3, anchor="w")
        Label4.config(text=f"Domain: {config["domain"]}")
        answerCanvas.create_window(300, 15, window=Label4, anchor="w")
        Label5.config(text=f"Range: {config["range"]}")
        answerCanvas.create_window(300, 55, window=Label5, anchor="w")
        Label6.config(text=f"")
        answerCanvas.create_window(300, 95, window=Label6, anchor="w")
    elif config["function"] == "Square Root":
        x_offset = int(config["h"]) + 9
        y_offset = -int(config["k"])
        Label1.config(text=f"Vertex: {config["vertex"]}")
        answerCanvas.create_window(90, 15, window=Label1, anchor="w")
        Label2.config(text=f"Horizontal Shift: {config["h"]}")
        answerCanvas.create_window(90, 55, window=Label2, anchor="w")
        Label3.config(text=f"Vertical Shift: {config["k"]}")
        answerCanvas.create_window(90, 95, window=Label3, anchor="w")
        Label4.config(text=f"Domain: {config["domain"]}")
        answerCanvas.create_window(300, 15, window=Label4, anchor="w")
        Label5.config(text=f"Range: {config["range"]}")
        answerCanvas.create_window(300, 55, window=Label5, anchor="w")
        Label6.config(text=f"")
        answerCanvas.create_window(300, 95, window=Label6, anchor="w")
    elif config["function"] == "Rational":
        x_offset = int(config["h"])
        y_offset = -int(config["k"])
        Label1.config(text=f"Horizontal Shift: {config["h"]}")
        answerCanvas.create_window(90, 15, window=Label1, anchor="w")
        Label2.config(text=f"Vertical Shift: {config["k"]}")
        answerCanvas.create_window(90, 55, window=Label2, anchor="w")
        Label3.config(text=f"Domain: {config["domain"]}")
        answerCanvas.create_window(90, 95, window=Label3, anchor="w")
        Label4.config(text=f"Range: {config["range"]}")
        answerCanvas.create_window(300, 15, window=Label4, anchor="w")
        Label5.config(text=f"H. Asymptote: y = {config["k"]}")
        answerCanvas.create_window(300, 55, window=Label5, anchor="w")
        Label6.config(text=f"V. Asymptote: x = {config["h"]}")
        answerCanvas.create_window(300, 95, window=Label6, anchor="w")
    elif config["function"] == "Quadratic":
        x_offset = int(config["h"])
        if config["posneg"] == "Positive":
            y_offset = -int(config["k"]) - 7
        if config["posneg"] == "Negative":
            y_offset = -int(config["k"]) + 7
        Label1.config(text=f"Vertex: {config["vertex"]}")
        answerCanvas.create_window(90, 15, window=Label1, anchor="w")
        Label2.config(text=f"Horizontal Shift: {config["h"]}")
        answerCanvas.create_window(90, 55, window=Label2, anchor="w")
        Label3.config(text=f"Vertical Shift: {config["k"]}")
        answerCanvas.create_window(90, 95, window=Label3, anchor="w")
        Label4.config(text=f"Domain: {config["domain"]}")
        answerCanvas.create_window(300, 15, window=Label4, anchor="w")
        Label5.config(text=f"Range: {config["range"]}")
        answerCanvas.create_window(300, 55, window=Label5, anchor="w")
        Label6.config(text=f"A.o.S.: x = {config["h"]}")
        answerCanvas.create_window(300, 95, window=Label6, anchor="w")
    elif config["function"] == "Cubic":
        x_offset = int(config["h"])
        y_offset = -int(config["k"])
        Label1.config(text=f"P.O.I.: {config["point_intersect"]}")
        answerCanvas.create_window(90, 15, window=Label1, anchor="w")
        Label2.config(text=f"Horizontal Shift: {config["h"]}")
        answerCanvas.create_window(90, 55, window=Label2, anchor="w")
        Label3.config(text=f"Vertical Shift: {config["k"]}")
        answerCanvas.create_window(90, 95, window=Label3, anchor="w")
        Label4.config(text=f"Domain: {config["domain"]}")
        answerCanvas.create_window(300, 15, window=Label4, anchor="w")
        Label5.config(text=f"Range: {config["range"]}")
        answerCanvas.create_window(300, 55, window=Label5, anchor="w")
        Label6.config(text=f"")
        answerCanvas.create_window(300, 95, window=Label6, anchor="w")
    elif config["function"] == "Absolute Value":
        x_offset = int(config["h"])
        y_offset = -int(config["k"])
        Label1.config(text=f"Vertex: {config["vertex"]}")
        answerCanvas.create_window(90, 15, window=Label1, anchor="w")
        Label2.config(text=f"Horizontal Shift: {config["h"]}")
        answerCanvas.create_window(90, 55, window=Label2, anchor="w")
        Label3.config(text=f"Vertical Shift: {config["k"]}")
        answerCanvas.create_window(90, 95, window=Label3, anchor="w")
        Label4.config(text=f"Domain: {config["domain"]}")
        answerCanvas.create_window(300, 15, window=Label4, anchor="w")
        Label5.config(text=f"Range: {config["range"]}")
        answerCanvas.create_window(300, 55, window=Label5, anchor="w")
        Label6.config(text=f"")
        answerCanvas.create_window(300, 95, window=Label6, anchor="w")

    if config["function"] == "Rational":
        graph_nums(x_offset, y_offset)
        draw_origin_axes(-x_offset * 2, -y_offset * 2)
    else:
        graph_nums(x_offset, y_offset)
        draw_origin_axes(-x_offset, -y_offset)

def draw_graph():
    for i in range(32):
        lineInt = (i * (407//31)) + 2
        graphCanvas.create_line(lineInt, 0, lineInt, 407, fill="black")
        graphCanvas.create_line(407, lineInt, 0, lineInt, fill="black")
    
    for i in range(32):
        lineInt = (i * (407//31)) + 32
        dashCanvas.create_line(lineInt, 25, lineInt, 20, fill="black")
        dashCanvas.create_line(25, lineInt, 20, lineInt, fill="black")

def draw_point(x, y, color):
    x *= 13
    x += 6
    y *= 13
    y += 6
    graphCanvas.create_oval(x-10, y-10, x+2, y+2, fill=color, outline=color, tags="graph_point")

def clear_points():
    graphCanvas.delete("graph_point")

def clear_dashline():
    graphCanvas.delete("dash_line")

def graph_nums(x_offset, y_offset):
    dashCanvas.delete("axis_label")

    with open("Data/config.json", "r") as f:
        config = json.load(f)

    if config["function"] == "Rational":
        for i in np.arange(-8, 8, 0.5):
            value = i + x_offset
            x = 32 + (((i)*2) + 16) * 13
            dashCanvas.create_text(x, 10, text = f"{int(value) if value.is_integer() else value}", font=("Arial", 6), anchor="n", tags="axis_label")
    
        for i in np.arange(-8, 8, 0.5):
            value = -(i + y_offset)
            y = 32 + (((i)*2) + 16) * 13
            dashCanvas.create_text(17, y, text = f"{int(value) if value.is_integer() else value}", font=("Arial", 6), anchor="e",tags="axis_label")

    else:
        for i in range(-16, 16):
            x = 32 + (i + 16) * 13
            dashCanvas.create_text(x, 10, text=str(i + x_offset), font=("Arial", 6), anchor="n", tags="axis_label")
    
        for i in range(-16, 16):
            y = 32 + (i + 16) * 13
            dashCanvas.create_text(10, y, text=str(-(i + y_offset)), font=("Arial", 6), anchor="e",tags="axis_label")

def draw_origin_axes(x_offset, y_offset):
    graphCanvas.delete("origin_axis")

    with open("Data/config.json", "r") as f:
        cfg = json.load(f)

    origin_x = ((x_offset + 16) * (407//31)) + 2
    origin_y = ((y_offset + 16) * (407//31)) + 2

    graphCanvas.create_line(origin_x, 0, origin_x, 407, width=3, fill="black", tags="origin_axis")
    graphCanvas.create_line(0, origin_y, 407, origin_y, width=3, fill="black", tags="origin_axis")

    if cfg["function"] == "Rational":
        for i in range(29):
            x1 = i * 14
            x2 = x1 + 9
            graphCanvas.create_line(210, x1, 210, x2, width=3, fill="#343434", tags="dash_line")
        for i in range(29):
            x1 = i * 14
            x2 = x1 + 9
            graphCanvas.create_line(x1, 210, x2, 210, width=3, fill="#343434", tags="dash_line")
    else:
        return

root = tk.Tk()
root.title("Graph Functions")
root.geometry("550x730")
root.resizable(False, False)
root.iconbitmap("Images/icon.ico")

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

dashCanvas = tk.Canvas(root, width=454, height=454)
dashCanvas.pack(pady=10)

graphCanvas = tk.Canvas(dashCanvas, width=404, height=404)
graphCanvas.pack(pady=30, padx=30)

separator2 = ttk.Separator(root, orient='horizontal')
separator2.pack(fill='x', padx=20, pady=5)

answerCanvas = tk.Canvas(root, width=475, height=115)
answerCanvas.pack(pady=(10, 0))

Label1 = tk.Label(answerCanvas, text="P.O.I.: ", font=("Arial", 10))
answerCanvas.create_window(90, 15, window=Label1, anchor="w")

Label2 = tk.Label(answerCanvas, text="Horizontal Shift: ", font=("Arial", 10))
answerCanvas.create_window(90, 55, window=Label2, anchor="w")

Label3 = tk.Label(answerCanvas, text="Vertical Shift: ", font=("Arial", 10))
answerCanvas.create_window(90, 95, window=Label3, anchor="w")

Label4 = tk.Label(answerCanvas, text="Domain: ", font=("Arial", 10))
answerCanvas.create_window(300, 15, window=Label4, anchor="w")

Label5 = tk.Label(answerCanvas, text="Range: ", font=("Arial", 10))
answerCanvas.create_window(300, 55, window=Label5, anchor="w")

Label6 = tk.Label(answerCanvas, text="", font=("Arial", 10))
answerCanvas.create_window(300, 95, window=Label6, anchor="w")

draw_graph()
draw_origin_axes(0, 0)
graph_nums(0, 0)
root.mainloop()
