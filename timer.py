count = 60

class Timer:

    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas['font'] = ('Times New Roman', 20)

#        self.canvas.create_text(200, 10, text=count)

    def start(self):
        global count
        self.canvas['text'] = count
        count = count - 1
        self.canvas.after(1000, self.start)
