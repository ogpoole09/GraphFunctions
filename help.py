import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Help")
root.geometry("500x310")
root.resizable(False, False)

title = tk.Label(root, text="Help", font=("Arial", 24, "bold"))
title.pack(pady=10)

separator1 = ttk.Separator(root, orient='horizontal')
separator1.pack(fill='x', padx=20, pady=10)

subtitle1 = tk.Label(root, text="How to use:", font=("Arial", 17, "bold"))
subtitle1.pack(pady=10)

text1 = tk.Label(root, text=f"1. To edit the graphs properties, click on the settings button.", font=("Arial", 10))
text1.pack(pady=2)

text2 = tk.Label(root, text=f"2. In the settings window, you will see a bunch of properties you can change.", font=("Arial", 10))
text2.pack(pady=2)

text3 = tk.Label(root, text=f"3. Once you're done editing the graph, click the 'Save Settings' button.", font=("Arial", 10))
text3.pack(pady=2)

text4 = tk.Label(root, text=f"4. Back in the main window, you can click the load button (arrow pointing up),", font=("Arial", 10))
text4.pack(pady=(2, 0))
text41 = tk.Label(root, text=f"to load your properties onto the graph.", font=("Arial", 10))
text41.pack(pady=(0, 2))

text5 = tk.Label(root, text=f"5. Enjoy!", font=("Arial", 10))
text5.pack(pady=2)

root.mainloop()
