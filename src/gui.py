from email.policy import default
from hashlib import new
from turtle import title
import pyperclip as pc
import subprocess as sp

from tkinter import *
from PIL import Image, ImageTk

from utils.constants import PAYLOAD_PIX
from utils.constants import ICONS_PATH

from controllers.qrcodegen import getQRCode
from controllers.loadconfig import configs
from controllers.goprint import getPrinters
from controllers.goprint import _print

class Application:
    def __init__(self, master=None):
        self.configs = configs()

        self.fonte = ("Verdana", "8")
        self.master = master

        self.price=0.00

        # add menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        # Menu
        myMenu = Menu(menu, tearoff=0)
        myMenu.add_command(label="Configurações", command=openConfigFile)
        myMenu.add_separator()
        myMenu.add_command(label="exit", command=self.master.destroy)

        # Printers
        printers = Menu(menu, tearoff=0)
        printers_list = Menu(menu, tearoff=0)

        # script prog exec
        # prog = f'printers_list.add_command(label=_[2], command=pc.copy(_[2]) )'
        for _ in getPrinters():
            # exec(prog)
            printers_list.add_command(
                label=_[2], 
                command=lambda: pc.copy(_[0])
            )

        printers.add_cascade(label="lista", menu=printers_list)
        #------

        menu.add_cascade(label="Menu", menu=myMenu)
        menu.add_cascade(label="Impressoras", menu=printers)
        menu.add_cascade(label="Sobre", command=self.about_window)

        def on_click(event):
            value.configure(state=NORMAL)
            value.delete(0, END)

            # make the callback only work once
            value.unbind('<Button-1>', on_click_id)

        def get_value_and_gen():
            price = value.get()
            
            self.qrcode_window()

        value = Entry(master, justify=RIGHT, width=27)
        value.insert(0, '0.00')
        value.configure(state=DISABLED)

        value.pack(
            side=LEFT,
            padx=15, 
            ipady=8,
            ipadx=8
        )

        # on_click_id = value.bind('<Button-1>', on_click)

        #Icon
        qrcodeicon=PhotoImage("./assets/qrcode-16x.png")

        Button(master, text='Gerar', command=get_value_and_gen).pack(
            side=LEFT,
            padx=5,
            ipady=8,
            ipadx=12,
        )

    def qrcode_window(self):  
        default_print = self.configs['DEFAULT']['printer']      
        cube_s = int(self.configs['DEFAULT']['qrcode_size']) * 49

        new_window = Toplevel(self.master)
        # new_window.title("QR Code - R$ " + str(self.price))
        new_window.title("QR Code - R$ 0,00")
        new_window.geometry(centralize_app(self.master, cube_s, cube_s))
        new_window.resizable(False, False)
        new_window.iconbitmap(ICONS_PATH["qr16Xico"])
        new_window.focus_force()

        # event -> press return
        new_window.bind(
            '<Return>', 
            lambda *args: 
                print("Na teoria ia imprimir em", default_print)
        )

        # add menu
        menu = Menu(self.master)
        new_window.config(menu=menu)
        # _print -> byte to printers
        menu.add_cascade(
            label="Imprimir", 
            command=
                lambda: 
                    print("Na teoria ia imprimir em", default_print)
        )


        img= getQRCode(PAYLOAD_PIX).get_image()
        img = ImageTk.PhotoImage(img)


        # Há algum problema em fazer Resize
        lb = Label(
            new_window, 
            image=img,
            # width=300,
            # height=300,
            # justify=CENTER,
        )

        lb.image = img
        lb.pack()

    def about_window(self):
        new_window = Toplevel(self.master)
        new_window.title("Sobre")
        new_window.geometry(centralize_app(self.master, 125, 250))
        new_window.resizable(False, False)
        new_window.iconbitmap(ICONS_PATH["qr16Xico"])

        message="""App para geração/impressão de pix\r\n dinânimo\r\n\r\nDesenvolvido por codexfast"""

        Label(new_window, text=message, width=120).place(relx=.5, rely=.5, anchor= CENTER)

def openConfigFile():
    programName = "notepad.exe" 
    fileName = "config.ini"
    sp.Popen([programName, fileName])

def centralize_app(root, wHeigth, wWidth):

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - wWidth / 2)
    center_y = int(screen_height/2 - wHeigth / 2)

    return '{}x{}+{}+{}'.format(wWidth, wHeigth, center_x, center_y)

def initialize():
    root = Tk()
    Application(root)

    # set dimension
    window_height = 100
    window_width = 300

    root.title('Pixhos')
    root.resizable(False, False)
    root.iconbitmap(ICONS_PATH["qr16Xico"])
    # root.attributes('-topmost', 1)
    root.geometry(centralize_app(root, window_height, window_width))

    root.mainloop()
    return 0;
