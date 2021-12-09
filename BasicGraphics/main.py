import tkinter as tk

class BasicGraphics(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.master.title("Hello World GUI")
        self.pack(fill=tk.BOTH, expand=1)
        canvas = tk.Canvas(self)

        # x and y are how many pixels from 0,0 at the top left
        canvas.create_text(100, 100, text="Hello World GUI!")
        canvas.create_oval(200, 100, 300, 200, outline='black')
        canvas.create_line(250, 200, 250, 500)
        canvas.create_line(150, 300, 350, 300)
        canvas.create_line(150, 600, 250, 500)
        canvas.create_line(350, 600, 250, 500)


        canvas.pack(fill=tk.BOTH, expand=1)
        self.pack()

app_frame = tk.Tk()

app_frame.geometry('800x600')

app = BasicGraphics(app_frame)
app.mainloop()