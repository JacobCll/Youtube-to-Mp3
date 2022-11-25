# converts yt video to mp3 
# file goes to clipboard

from tkinter import messagebox
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import threading
import os

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.root.title("Youtube Video To mp3")

        self.input_frame = tk.LabelFrame(self.root, bg="#D3D3D3", height=100)
        self.input_frame.pack(side=tk.TOP, fill="both", expand=True)

        self.title = tk.Label(self.input_frame, text="YouTube > MP3", font=("Arial", 20), bg="#D3D3D3")
        self.title.pack(pady=20, side=tk.TOP)

        self.url_title = tk.Label(self.input_frame, text="Paste URL here:", font=("Arial", 9)).pack(pady=0.5)
        
        self.urlvar = tk.StringVar() # URL input will be saved here as a variable.

        self.input_entry = tk.Entry(self.input_frame, textvariable=self.urlvar, width=40)
        self.input_entry.pack(pady=3)

        ###
        self.button_frame = tk.Frame(self.root, bg="#8B0000", height=20)
        self.button_frame.pack(side=tk.BOTTOM, fill="both", expand=True)

        self.convert_button = tk.Button(self.button_frame, text="Convert and Download", font=("Arial", 14), command=lambda:self.start_ymp3_thread())
        self.convert_button.pack(pady=15)

        self.root.mainloop()
        
    def ymp3(self):
        url = self.urlvar.get()
        try:
            yt_url = YouTube(str(url))
        except:
            messagebox.showinfo(title='Error', message="Not a valid URL, try again.")
            return
        filename = filedialog.asksaveasfilename(title="Save mp3 location", initialfile=yt_url.title, filetypes=[("Mp3 Files", "*.mp3")], defaultextension=".mp3", confirmoverwrite=True)
        print(filename)

        if filename:
            print(url)
            audio = yt_url.streams.filter(only_audio=True).first()
            try:
                audio.download(filename=filename.replace("/", "\\")) # full path with file name
                messagebox.showinfo(title='Message', message=f"{yt_url.title} has been downloaded!")
            
            except FileExistsError: # Not necessary because of confirmoverwrite=True in filedialog 
                os.remove(filename.replace("/", "\\") + '.mp4')
                messagebox.showinfo(title='Message', message=f"File already exists in given path.")
                return
        else:
            print("No filename given. ")

    def start_ymp3_thread(self): # starts a thread of self.ymp3 everytime this function is ran.
        thread = threading.Thread(target=self.ymp3)
        thread.start()

    

if __name__ == "__main__":
    window = GUI()
