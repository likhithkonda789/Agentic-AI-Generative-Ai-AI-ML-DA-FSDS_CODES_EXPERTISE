from tkinter import *
import tkinter.messagebox as mb
import requests

# Function
def extract_lyrics():
    artist_name = artist.get().strip()
    song_name = song.get().strip()

    if not artist_name or not song_name:
        mb.showwarning("Input Error", "Please enter both song name and artist name.")
        return

    # Correct API URL (no manual %20)
    url = f"https://api.lyrics.ovh/v1/{artist_name}/{song_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        lyrics = data.get("lyrics")

        if lyrics:
            print("\n" + lyrics + "\n")
            mb.showinfo(
                "Lyrics Found",
                "Lyrics extracted successfully.\nCheck your terminal window."
            )
        else:
            mb.showerror("Not Found", "Lyrics not available.")

    except requests.exceptions.HTTPError:
        mb.showerror(
            "Song Not Found",
            "This song is not available in lyrics.ovh database.\nTry an English song."
        )
    except requests.exceptions.RequestException as e:
        mb.showerror("Network Error", str(e))


# Tkinter Window
root = Tk()
root.title("Likhith's Song Lyrics Extractor")
root.geometry("600x200")
root.resizable(0, 0)
root.config(bg='CadetBlue')

Label(
    root,
    text="Likhith's Song Lyrics Extractor",
    font=("Comic Sans MS", 16, "bold"),
    bg="CadetBlue"
).pack(side=TOP, fill=X)

Label(root, text="Enter the song name:", font=("Times New Roman", 14), bg="CadetBlue").place(x=20, y=50)
song = StringVar()
Entry(root, width=40, textvariable=song, font=("Times New Roman", 14)).place(x=200, y=50)

Label(root, text="Enter the artist's name:", font=("Times New Roman", 14), bg="CadetBlue").place(x=20, y=100)
artist = StringVar()
Entry(root, width=40, textvariable=artist, font=("Times New Roman", 14)).place(x=200, y=100)

Button(
    root,
    text="Extract lyrics",
    font=("Georgia", 10),
    width=15,
    command=extract_lyrics
).place(x=220, y=150)

root.mainloop()
