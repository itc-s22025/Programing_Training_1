from tkinter import *

from ball import Ball
from paddle import Paddle
from timer import Timer



class Game:

    def __init__(self):
    
        self.tk = Tk()
        self.tk.title("Game")                      
        self.tk.resizable(False, False)             
        self.tk.wm_attributes("-topmost", True)     

        self.canvas = Canvas(self.tk, width=500, height=400, bd=False, highlightthickness=False)
        self.label = Label(self.tk, width=9,height=4, bg='white')

        self.canvas.pack()
        self.label.pack()
        self.tk.update()        

        self.paddle = Paddle(self.canvas, "#5f76e7")
        self.ball = Ball(self.canvas, "#f75539", self.paddle)
        self.timer = Timer(self.label)
 
        
        #kono ki- ositara kono kansuuga jikkou sareruyo
        self.canvas.bind_all("<KeyPress-Left>", self.paddle.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.paddle.turn_right)
        self.canvas.bind_all("<KeyPress-space>", self.ball.start)
#        self.label.bind_all("<KeyPress-space>", self.timer.start)
        



    def main(self):
        self.timer.start()
        self.update()     
        self.tk.mainloop()  

        

    def update(self):
   
        self.ball.draw()
        
        self.paddle.draw()


        
        self.canvas.after(1000 // 60, self.update)
        

game = Game()
game.main()
