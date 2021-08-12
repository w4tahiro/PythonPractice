import tkinter as tk
from PIL import Image, ImageTk

class ImageUI(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master.title('Image')
        image = Image.open('29310.jpg')
        self.images = []
        self.images.append(ImageTk.PhotoImage(image))

        self.c = tk.Canvas(self,width = 1920,height = 1080,highlightthickness = 0)
        self.c.pack()

        self.on_draw()

    def on_draw(self):
        self.c.delete('all')
        self.c.create_image(10,10,image=self.images[0],anchor=tk.NW)

f = ImageUI()
f.pack()
f.mainloop()
