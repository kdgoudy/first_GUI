import tkinter as tk

root = tk.Tk()

root.geometry("600x600")
root.title("My first GUI")

label = tk.Label(root, text="Hello World!", font=("Arial", 18))
label.pack()

root.mainloop()

