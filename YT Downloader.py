from pytubefix import YouTube
import tkinter as tk
from tkinter import ttk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('550x400+300+300')
        self.root.title('YT Downloader')
        self.mainframe = tk.Frame(self.root, background='grey')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe, text='Video Link', background='white', font=('Brass Mono', 50))
        self.text.grid(row=0, column=0)

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky='NWES')

        self.format = tk.StringVar(value='mp4')
        self.radio_mp4 = ttk.Radiobutton(self.mainframe, text='mp4', value='mp4', variable=self.format)
        self.radio_mp4.grid(row=2, column=0, sticky='NWES', pady=10)
        self.radio_mp3 = ttk.Radiobutton(self.mainframe, text='mp3', value='mp3', variable=self.format)
        self.radio_mp3.grid(row=2, column=1, sticky='NWES', pady=10)

        self.set_text_button = ttk.Button(self.mainframe, text='Confirm', command=self.get_video)
        self.set_text_button.grid(row=3, column=0, pady=10)

        self.root.mainloop()
        return
    def get_video(self):
        link = self.set_text_field.get()
        format = self.format.get()
        video = YouTube(link).streams

        if format == "mp4":
            video.filter(adaptive=True).filter(mime_type='video/mp4').first().download()
        elif format == "mp3":
            video.get_audio_only().download()

    
if __name__ == '__main__':
    App()
