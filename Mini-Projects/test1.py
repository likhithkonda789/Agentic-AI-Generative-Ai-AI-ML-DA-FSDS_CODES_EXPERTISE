import tkinter as tk

# Create the main window (root)
root = tk.Tk()
root.title("My Tkinter App") # Set window title

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack() # Pack the label into the window

# Create a button widget
def button_click():
    label.config(text="Button clicked!")

button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

# Start the main event loop
root.mainloop()