import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Credits")
root.geometry("300x200")
root.resizable(False, False)

title = tk.Label(root, text="Credits", font=("Arial", 24, "bold"))
title.pack(pady=10)

separator1 = ttk.Separator(root, orient='horizontal')
separator1.pack(fill='x', padx=20, pady=10)

text = tk.Label(root, text="Oliver Poole - Everything", font=("Arial", 10))
text.pack(pady=10)

separator2 = ttk.Separator(root, orient='horizontal')
separator2.pack(fill='x', padx=20, pady=10)

contact = tk.Label(root, text="Contact: oliver.poole27@calhoun.org", font=("Arial", 10))
contact.pack(pady=10)

root.mainloop()
