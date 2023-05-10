import tkinter as tk
import random


class Janela:
    def __init__(self, master):
        self.master = master
        master.title("Vamos casar?")
        master.configure(bg="red")

        self.label = tk.Label(master, text="Você aceita casar comigo?", font=(
            "Arial", 18), bg="red", fg="white")
        self.label.pack(pady=20)

        self.botao1 = tk.Button(master, text="Sim", command=self.sim, bg="black", fg="white", font=(
            "Arial", 14), padx=20, pady=10, relief="raised", borderwidth=2)
        self.botao1.pack(side="left", padx=20)

        self.botao2 = tk.Button(master, text="Não", command=self.nao, bg="black", fg="white", font=(
            "Arial", 14), padx=20, pady=10, relief="raised", borderwidth=2)
        self.botao2.pack(side="right", padx=20)

        self.botao1.bind("<Enter>", self.move_botao1)

        self.center_window()

    def sim(self):
        self.label.configure(
            text="Parabéns! Você aceitou casar comigo!", font=("Arial", 18))

    def nao(self):
        self.label.configure(
            text="Que pena! :( Quem sabe na próxima vez...", font=("Arial", 18))

    def move_botao1(self, event):
        x = random.randint(0, self.master.winfo_width() -
                           self.botao1.winfo_width())
        y = random.randint(0, self.master.winfo_height() -
                           self.botao1.winfo_height())
        self.botao1.place(x=x, y=y)

    def center_window(self):
        largura = 400
        altura = 200
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        x = (largura_tela - largura) / 2
        y = (altura_tela - altura) / 2
        self.master.geometry("%dx%d+%d+%d" % (largura, altura, x, y))


root = tk.Tk()
janela = Janela(root)
root.mainloop()
