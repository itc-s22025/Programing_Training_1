import random
import math
from tkinter import *

point = 0


class Ball:
    
    
    def __init__(self, canvas, color, paddle):
       
        self.canvas = canvas
        self.paddle = paddle
  
        self.id = self.canvas.create_oval(10, 10, 30, 30, fill=color, outline='')
    
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    
        self.init_x = self.canvas_width / 2 - 7.5
        self.init_y = self.canvas_height / 2 - 7.5
     
        self.speed = 0
     
        self.x = 0
        self.y = 0
        

    def start(self, evt):
      
        if self.speed != 0:
            return
    
        self.canvas.moveto(self.id, self.init_x, self.init_y)
        self.speed = 3    
   
        angle = math.radians(random.choice(list(range(20, 65, 5))))
        direction = random.choice([1, -1]) 
     
        self.x = math.cos(angle) * self.speed * direction
        self.y = math.sin(angle) * self.speed
    
    def draw(self):
        global point

        self.canvas.create_text(250, 100, text=point, tag='tex',font=('Times New Roman', 100))
    
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.fix(pos[0] - 0, 0)
        
        if pos[1] <= 0:
            self.fix(0, pos[1])

        if pos[2] >= self.canvas_width:
            self.fix(pos[2] - self.canvas_width, 0)

        if pos[3] >= self.canvas_height:
            self.fix(0, pos[3] - self.canvas_height)

            self.failed() 

        paddle_pos = self.canvas.coords(self.paddle.id)
   
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] \
           and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
            self.fix(0, pos[3] - paddle_pos[1])
            self.canvas.delete('tex')
            point = point + 1


        
    def fix(self, diff_x, diff_y):
     
        self.canvas.move(self.id, -(diff_x * 2), -(diff_y * 2))
 
        if diff_x != 0:
            self.x = -self.x
            
        if diff_y != 0:
            self.y = -self.y

    def resta(self, evt):
        #self.canvas.delete(self.ide)
        self.draw()

    def from_forget(self, evt):
        self.canvas2.place_forget()
        self.canvas.pack()
        self.draw()
        
    def trans(self):
        self.canvas.place_forget()
        self.canvas2 = Canvas(width='500',height='400', bg='white')
        self.canvas2.place(x=0, y=0)
        self.label2 = Label(self.canvas2, text='''Failed... :(
Press r then space-key to resume!''', font=(25))
        self.label2.place(x=100, y=150)
        self.canvas.bind_all("<KeyPress-r>",self.from_forget)


    def failed(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        self.canvas.after(500, self.trans)

#        self.ide = self.canvas.create_text(250,250,anchor='center',text='Failed:(',font=("Times New Roman",24))
#        self.canvas.bind_all("<KeyPress-r>",self.resta)
