#　タイマー機能をつけました

count = 60

class Timer:

    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas['font'] = ('Times New Roman', 20)

#        self.canvas.create_text(200, 10, text=count)
#　↑はcanvas上でcreate_textでどうにかカウントしようとしていたときの名残　ラベルのほうが楽だったのでラベルを作成しました

    def start(self):
#　タイマー開始
        global count
        self.canvas['text'] = count
        count = count - 1
        self.canvas.after(1000, self.start)
        if count == 0:
            count = 'Finished!'
#　カウントが0になったら無理やりcountの文字を'Finishd!'にする
