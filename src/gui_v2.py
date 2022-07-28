# coding: utf-8
# gui v2 pixhos

from utils.constants import ICONS_PATH

from tkinter import E, RIGHT, EW, W, Tk, Menu
from tkinter import ttk

class Main():
    def __init__(self, master=None):
        self.master = master

        # init menu
        self.__menu()

        # init main
        self.__main()

    def __menu(self):
        # add menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create sub menu <menu>
        myMenu = Menu(menu, tearoff=0)
        myMenu.add_command(label="Configurações", command=lambda: print("Abrindo config"))
        myMenu.add_separator()
        myMenu.add_command(label="Sair", command=self.master.destroy)

        # add to cascade
        menu.add_cascade(label="Menu", menu=myMenu)

    def __main(self):
        self.master.columnconfigure(0, weight=3)
        self.master.columnconfigure(1, weight=1)

        price_entry = ttk.Entry(self.master, justify=RIGHT)
        price_entry.insert(0, 'R$ 0,00')
        price_entry.grid(column=0, row=0, padx=5, pady=5, ipady=5, ipadx=2, sticky=EW)

        gen_button = ttk.Button(self.master, text="Gerar", command=lambda: print("Gerando pix"))
        gen_button.grid(column=1, row=0, padx=5,pady=5, sticky=E, ipady=5)


def centralize_app(root, wHeigth, wWidth):

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - wWidth / 2)
    center_y = int(screen_height/2 - wHeigth / 2)

    return f'{wWidth}x{wHeigth}+{center_x}+{center_y}'

def initialize():
    root = Tk()
    
    Main(root)

    # set dimension
    window_height = 100
    window_width = 300

    root.title('Pixhos')
    root.resizable(False, False)
    root.iconbitmap(ICONS_PATH["qr16Xico"])
    # root.attributes('-topmost', 1)
    root.geometry(centralize_app(root, window_height, window_width))

    root.mainloop()

if __name__ == "__main__":
    initialize()