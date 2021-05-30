import tkinter as tk

class Application(tk.Frame):

    # spinboxに関する情報を格納する関数
    spinbox = None

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、spinbox Widgetを作成する。
        # from_ : 入力できる数字の下限を設定する。初期値とされる。
        # to : 入力できる数字の上限を設定する。
        # command : 右に設定される↑↓ボタンがクリックされた場合に、実行する関数を設定する。今回はhelloWorld
        self.spinbox = tk.Spinbox(frame, from_=100, to=200, command=self.helloWorld)

        # frame Widget(Frame)を親要素とした場合に、spinbox Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.spinbox.pack()

    # hello worldを出力する関数
    def helloWorld(self):
        print('hello world')

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()
