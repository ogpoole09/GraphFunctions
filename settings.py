import tkinter as tk
from tkinter import ttk
import json

with open("Data/config.json", "r") as f:
    config = json.load(f)

def save_settings():
    if selected_function.get() == "Square Root":
        config["function"] = "Square Root"
        config["vertex"] = f"({h_entry.get()}, {k_entry.get()})"
        config["domain"] = f"[{h_entry.get()}, ∞)"

        if selected_posneg.get() == "Positive":
            config["posneg"] = "Positive"
            config["start_point"] = "7, 16"
            x0, y0 = 7, 16
            config["point_1"] = f"{x0 + 1}, {y0 - 1}"
            config["point_2"] = f"{x0 + 4}, {y0 - 2}"
            config["point_3"] = f"{x0 + 9}, {y0 - 3}"
            config["point_4"] = f"{x0 + 16}, {y0 - 4}"
            config["range"] = f"[{k_entry.get()}, ∞)"
        elif selected_posneg.get() == "Negative":
            config["posneg"] = "Negative"
            config["start_point"] = "7, 16"
            x0, y0 = 7, 16
            config["point_1"] = f"{x0 + 1}, {y0 + 1}"
            config["point_2"] = f"{x0 + 4}, {y0 + 2}"
            config["point_3"] = f"{x0 + 9}, {y0 + 3}"
            config["point_4"] = f"{x0 + 16}, {y0 + 4}"
            config["range"] = f"(-∞, {k_entry.get()}]"

    elif selected_function.get() == "Cube Root":
        config["function"] = "Cube Root"
        config["point_intersect"] = f"({h_entry.get()}, {k_entry.get()})"
        config["domain"] = "(-∞, ∞)"
        config["range"] = "(-∞, ∞)"

        if selected_posneg.get() == "Negative":
            config["posneg"] = "Negative"
            config["start_point"] = "16, 16"
            x1, y1 = 16, 16
            config["point_1"] = f"{x1 + 1}, {y1 + 1}"
            config["point_2"] = f"{x1 + 8}, {y1 + 2}"
            config["point_3"] = f"{x1 - 1}, {y1 - 1}"
            config["point_4"] = f"{x1 - 8}, {y1 - 2}"
        elif selected_posneg.get() == "Positive":
            config["posneg"] = "Positive"
            config["start_point"] = "16, 16"
            x1, y1 = 16, 16
            config["point_1"] = f"{x1 + 1}, {y1 - 1}"
            config["point_2"] = f"{x1 + 8}, {y1 - 2}"
            config["point_3"] = f"{x1 - 1}, {y1 + 1}"
            config["point_4"] = f"{x1 - 8}, {y1 + 2}"

    elif selected_function.get() == "Rational":
        config["function"] = "Rational"
        config["domain"] = f"(-∞, {h_entry.get()})U({h_entry.get()}, ∞)"
        config["range"] = f"(-∞, {k_entry.get()})U({k_entry.get()}, ∞)"

        if selected_posneg.get() == "Positive":
            config["posneg"] = "Positive"
            config["start_point"] = "-1, -1"
            x2, y2 = 16, 16
            config["point_1"] = f"{x2 + 2}, {y2 - 2}"
            config["point_2"] = f"{x2 + 1}, {y2 - 4}"
            config["point_3"] = f"{x2 + 4}, {y2 - 1}"
            config["point_4"] = f"{x2 - 2}, {y2 + 2}"
            config["point_5"] = f"{x2 - 4}, {y2 + 1}"
            config["point_6"] = f"{x2 - 1}, {y2 + 4}"
        elif selected_posneg.get() == "Negative":
            config["posneg"] = "Negative"
            config["start_point"] = "-1, -1"
            x2, y2 = 16, 16
            config["point_1"] = f"{x2 - 2}, {y2 - 2}"
            config["point_2"] = f"{x2 - 1}, {y2 - 4}"
            config["point_3"] = f"{x2 - 4}, {y2 - 1}"
            config["point_4"] = f"{x2 + 2}, {y2 + 2}"
            config["point_5"] = f"{x2 + 4}, {y2 + 1}"
            config["point_6"] = f"{x2 + 1}, {y2 + 4}"

    elif selected_function.get() == "Quadratic":
        config["function"] = "Quadratic"
        config["domain"] = "(-∞, ∞)"
        config["vertex"] = f"({h_entry.get()}, {k_entry.get()})"

        if selected_posneg.get() == "Positive":
            config["posneg"] = "Positive"
            config["start_point"] = "16, 23"
            x3, y3 = 16, 23
            config["point_1"] = f"{x3 + 1}, {y3 - 1}"
            config["point_2"] = f"{x3 + 2}, {y3 - 4}"
            config["point_3"] = f"{x3 + 3}, {y3 - 9}"
            config["point_4"] = f"{x3 - 1}, {y3 - 1}"
            config["point_5"] = f"{x3 - 2}, {y3 - 4}"
            config["point_6"] = f"{x3 - 3}, {y3 - 9}"
            config["range"] = f"[{k_entry.get()}, ∞)"
        elif selected_posneg.get() == "Negative":
            config["posneg"] = "Negative"
            config["start_point"] = "16, 9"
            x3, y3 = 16, 9
            config["point_1"] = f"{x3 + 1}, {y3 + 1}"
            config["point_2"] = f"{x3 + 2}, {y3 + 4}"
            config["point_3"] = f"{x3 + 3}, {y3 + 9}"
            config["point_4"] = f"{x3 - 1}, {y3 + 1}"
            config["point_5"] = f"{x3 - 2}, {y3 + 4}"
            config["point_6"] = f"{x3 - 3}, {y3 + 9}"
            config["range"] = f"(-∞, {k_entry.get()}]"

    elif selected_function.get() == "Cubic":
        config["function"] = "Cubic"
        config["domain"] = "(-∞, ∞)"
        config["range"] = "(-∞, ∞)"
        config["point_intersect"] = f"({h_entry.get()}, {k_entry.get()})"

        if selected_posneg.get() == "Positive":
            config["posneg"] = "Positive"
            config["start_point"] = "16, 16"
            x1, y1 = 16, 16
            config["point_1"] = f"{x1 + 1}, {y1 - 1}"
            config["point_2"] = f"{x1 + 2}, {y1 - 8}"
            config["point_3"] = f"{x1 - 1}, {y1 + 1}"
            config["point_4"] = f"{x1 - 2}, {y1 + 8}"
        elif selected_posneg.get() == "Negative":
            config["posneg"] = "Negative"
            config["start_point"] = "16, 16"
            x1, y1 = 16, 16
            config["point_1"] = f"{x1 - 1}, {y1 - 1}"
            config["point_2"] = f"{x1 - 2}, {y1 - 8}"
            config["point_3"] = f"{x1 + 1}, {y1 + 1}"
            config["point_4"] = f"{x1 + 2}, {y1 + 8}"
    
    elif selected_function.get() == "Absolute Value":
        config["function"] = "Absolute Value"
        config["domain"] = "(-∞, ∞)"
        config["vertex"] = f"({h_entry.get()}, {k_entry.get()})"

        if selected_posneg.get() == "Positive":
            config["posneg"] = "Positive"
            config["start_point"] = "16, 16"
            x1, y1 = 16, 16
            config["point_1"] = f"{x1 + 1}, {y1 - 1}"
            config["point_2"] = f"{x1 + 2}, {y1 - 2}"
            config["point_3"] = f"{x1 + 3}, {y1 - 3}"
            config["point_4"] = f"{x1 - 1}, {y1 - 1}"
            config["point_5"] = f"{x1 - 2}, {y1 - 2}"
            config["point_6"] = f"{x1 - 3}, {y1 - 3}"
            config["range"] = f"[{k_entry.get()}, ∞)"
        elif selected_posneg.get() == "Negative":
            config["posneg"] = "Negative"
            config["start_point"] = "16, 16"
            x1, y1 = 16, 16
            config["point_1"] = f"{x1 + 1}, {y1 + 1}"
            config["point_2"] = f"{x1 + 2}, {y1 + 2}"
            config["point_3"] = f"{x1 + 3}, {y1 + 3}"
            config["point_4"] = f"{x1 - 1}, {y1 + 1}"
            config["point_5"] = f"{x1 - 2}, {y1 + 2}"
            config["point_6"] = f"{x1 - 3}, {y1 + 3}"
            config["range"] = f"(-∞, {k_entry.get()}]"
    
    config["h"] = h_entry.get()
    config["k"] = k_entry.get()

    with open("Data/config.json", "w") as f:
        json.dump(config, f, indent=4)
    
    saveLabel.config(text="Settings Saved")
    saveLabel.pack(pady=10)
    root.after(2000, lambda: saveLabel.config(text=""))
    saveLabel.pack(pady=10)

root = tk.Tk()
root.title("Settings")
root.geometry("500x400")
root.resizable(False, False)
root.iconbitmap("Images/SettingsIcon.ico")

label = tk.Label(root, text="Settings", font=("Arial", 24, "bold"))
label.pack(pady=10)

separator1 = ttk.Separator(root, orient='horizontal')
separator1.pack(fill='x', padx=20, pady=10)

functionList = ["Quadratic", "Cubic", "Absolute Value", "Square Root", "Cube Root", "Rational"]

selected_function = tk.StringVar()
selected_function.set(config["function"]) 

function_label = tk.Label(root, text="Function:")
function_label.pack()

functionSelector = tk.OptionMenu(root, selected_function, *functionList)
functionSelector.config(cursor="hand2")
functionSelector.pack(pady=(0, 10))

posnegList = ["Positive", "Negative"]

selected_posneg = tk.StringVar()
selected_posneg.set(config["posneg"]) 

posneg_label = tk.Label(root, text="Sign:")
posneg_label.pack()

posnegSelector = tk.OptionMenu(root, selected_posneg, *posnegList)
posnegSelector.config(cursor="hand2")
posnegSelector.pack(pady=(0, 10))

h_label = tk.Label(root, text="H:")
h_label.pack()
h_entry = tk.Entry(root)
h_entry.insert(0, config["h"])
h_entry.pack(pady=(0, 10))

k_label = tk.Label(root, text="K:")
k_label.pack()
k_entry = tk.Entry(root)
k_entry.insert(0, config["k"])
k_entry.pack(pady=(0, 10))

saveButton = tk.Button(root, text="Save Settings", cursor="hand2", command=save_settings)
saveButton.pack(pady=(20, 0))

saveLabel = tk.Label(root, text="", font=("Arial", 8), fg="#1BDE18")
saveLabel.pack(pady=10)

root.mainloop()
