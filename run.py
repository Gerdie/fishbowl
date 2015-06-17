from Tkinter import *
from PIL import Image, ImageTk
from threading import Timer

root = Tk()
    
bowlpic = ImageTk.PhotoImage(Image.open("Programming/fish_bowl.gif"))
fishpic = ImageTk.PhotoImage(Image.open("Programming/fish.gif"))
foodpic = ImageTk.PhotoImage(Image.open("Programming/cheerio.png"))

class App:

    def __init__(self, master):

        """Class container for app"""
        
        self.master = master
        
        self.frame = Frame(master)
        self.frame.pack()

        self.header = Label(self.frame, text="Gerdie the Goldfish")
        self.header.pack()
        
        self.button = Button(self.frame, text="Feed")
        self.button.pack()
        
        self.frame_inner = Frame(self.frame)
        self.frame_inner.pack()
        
        self.canvas = Canvas(self.frame_inner, width=700, height=500)
        self.bowl = self.canvas.create_image(350, 250, image=bowlpic)
        self.fish = self.canvas.create_image(350,270, image=fishpic)
        self.food = self.canvas.create_image(350,100, image=foodpic, state=HIDDEN)
        self.canvas.pack()
        
        def food_drop(self):
        	self.canvas.move(self.food, 0, 50)
        
        def feed(self):
        	#self.canvas.lift(self.food)
        	self.button.config(state=NORMAL)
        	Timer(2, food_drop).start()
        	Timer(4, food_drop).start()
        	Timer(6, food_drop).start()
        	#Timer(8, self.canvas.delete(self.food)).start()
        	
        self.button.config(command=feed(self))

app = App(root)

#app.button.config(command=app.feed)

root.mainloop()
root.destroy()
