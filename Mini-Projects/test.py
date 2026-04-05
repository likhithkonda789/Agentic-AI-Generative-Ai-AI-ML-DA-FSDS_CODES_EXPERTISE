import tkinter as tk

root = tk.Tk()
root.title("My Tkinter App")
root.geometry("300x200")

label = tk.Label(root, text="Hello Tkinter!")
label.pack()

root.mainloop()
