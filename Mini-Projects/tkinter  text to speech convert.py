import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
import threading

engine = pyttsx3.init()  # offline engine

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def on_speak():
    txt = text_box.get("1.0", "end").strip()
    if not txt:
        messagebox.showinfo("Info","Type something first.")
        return
    threading.Thread(target=speak_text, args=(txt,), daemon=True).start()

def on_save():
    txt = text_box.get("1.0", "end").strip()
    if not txt:
        messagebox.showinfo("Info","Type something first.")
        return
    path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                        filetypes=[("MP3 files","*.mp3"),("WAV files","*.wav"),("All files","*.*")])
    if not path:
        return
    # pyttsx3 can save to file:
    engine.save_to_file(txt, path)
    engine.runAndWait()
    messagebox.showinfo("Saved", f"Saved audio to:\n{path}")

# Build simple UI
root = tk.Tk()
root.title("Python TTS (pyttsx3)")
root.geometry("600x360")

text_box = tk.Text(root, wrap='word', font=("Segoe UI", 12))
text_box.pack(expand=True, fill='both', padx=10, pady=10)
text_box.insert("1.0", "Hello world.")

frame = tk.Frame(root)
frame.pack(pady=6)
tk.Button(frame, text="Speak", command=on_speak, width=12).pack(side='left', padx=6)
tk.Button(frame, text="Save to file", command=on_save, width=12).pack(side='left', padx=6)
tk.Button(frame, text="Quit", command=root.quit, width=12).pack(side='left', padx=6)

root.mainloop()

