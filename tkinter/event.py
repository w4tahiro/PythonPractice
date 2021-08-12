import tkinter as tk
from PIL import Image,ImageTk

class EventUI(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master.title('event')

        self.x = 0
        self.y = 0

        self.c = tk.Canvas(self,width = 240,height = 240,highlightthickness = 0)
        self.c.bind('<Button-1>',self.on_click)
        self.c.pack()

        self.on_draw()

    def on_click(self,event):
        self.x = event.x
        self.y = event.y
        self.on_draw()

    def on_draw(self):
        self.c.delete('all')
        
        str = 'click on {},{}'.format(self.x,self.y)
        self.c.create_text(10,10,text = str,font='courier 16',anchor = tk.NW)

f = EventUI()
f.pack()
f.mainloop()