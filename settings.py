import tkinter as tk
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
        config["vertex"] = f"({h_entry.get()}, {k_entry.get()})"
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

    
    config["horizontal_shift"] = h_entry.get()
    config["vertical_shift"] = k_entry.get()

    with open("Data/config.json", "w") as f:
        json.dump(config, f, indent=4)

root = tk.Tk()
root.title("Settings")
root.geometry("500x400")

label = tk.Label(root, text="Settings Page", font=("Arial", 24, "bold"))
label.pack(pady=20)

functionList = ["Square Root", "Cube Root"]

selected_function = tk.StringVar()
selected_function.set(config["function"]) 

functionSelector = tk.OptionMenu(root, selected_function, *functionList)
functionSelector.pack(pady=10)

posnegList = ["Positive", "Negative"]

selected_posneg = tk.StringVar()
selected_posneg.set(config["posneg"]) 

posnegSelector = tk.OptionMenu(root, selected_posneg, *posnegList)
posnegSelector.pack(pady=10)

h_label = tk.Label(root, text="H:")
h_label.pack()
h_entry = tk.Entry(root)
h_entry.insert(0, config["horizontal_shift"])
h_entry.pack(pady=5)

k_label = tk.Label(root, text="K:")
k_label.pack()
k_entry = tk.Entry(root)
k_entry.insert(0, config["vertical_shift"])
k_entry.pack(pady=5)

saveButton = tk.Button(root, text="Save Settings", command=save_settings)
saveButton.pack(pady=20)

root.mainloop()
