from tkinter import *
from typing import Container

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        self.master = master


        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        
        self.lblidusuario = Label(self.containers([{'padx':20, 'padx': 5}]),
        text="VALOR", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        # self.lblidusuario = Label(self.container2,
        # text="VALOR", font=self.fonte, width=10)
        # self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Gerar",
        font=self.fonte, width=10)
        self.btnBuscar.pack(side=RIGHT)

    def containers (self, containerConf):

        print(containerConf)
        container = Frame(self.master)
        # container.update(containerConf) 
        # container

        return container.pack()


root = Tk()
Application(root)
root.mainloop()