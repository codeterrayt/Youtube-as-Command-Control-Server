from tkinter import *
from main import startCloud

root = Tk()

root.minsize(400, 200)
root.maxsize(400, 200)
root.title("Cloud Gaming")

stream_link = StringVar()


def initCloud():
    root.destroy()
    video_id = stream_link.get().replace("https://www.youtube.com/watch?v=","")
    print(video_id)
    startCloud(video_id)



Label(text="Live Stream Link").pack()
Entry(textvariable=stream_link).pack()
Button(text="Start Cloud", command=initCloud).pack()

root.mainloop()
