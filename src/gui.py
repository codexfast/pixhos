from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk

from utils.constants import PAYLOAD_PIX
from utils.constants import ICONS_PATH

from controllers.qrcodegen import getQRCode
from controllers.loadconfig import db_config
from controllers.pixhos import db_pixhos
from controllers.goprint import getPrinters
from controllers.goprint import _print

class Application:
    def __init__(self, master=None):
        self.configs = db_config()
        self.pixhos = db_pixhos()

        self.fonte = ("Verdana", "8")
        self.master = master

        self.price=0.00

        # add menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        # Menu
        myMenu = Menu(menu, tearoff=0)
        myMenu.add_command(label="Configurações", command=self.config_window)
        myMenu.add_separator()
        myMenu.add_command(label="exit", command=self.master.destroy)

        # Printers
        printers = Menu(menu, tearoff=0)
        printers_list = Menu(menu, tearoff=0)

        # script prog exec
        # prog = f'printers_list.add_command(label=_[2], command=pc.copy(_[2]) )'
        my_printers = getPrinters()
        control = [BooleanVar() for x in range(len(my_printers))]

        for i, _ in enumerate(my_printers):
            print(i,_[2])
            # exec(prog)
            printers_list.add_checkbutton(
                label=_[2],
                onvalue=1, offvalue=0,
                variable=control[i],
                # command=lambda: pc.copy(_[2])
                # command=set_prt(this)
            )

        printers.add_cascade(label="padrão", menu=printers_list)
        printers.add_cascade(
            label=f'Testar {self.configs["prt_default"] if self.configs != None else "impressora"}',
            state=DISABLED if not self.configs else None,
            command=
                lambda: 
                    _print(
                        self.configs['prt_default'],
                        b'test'
                    )
        )
        #------

        menu.add_cascade(label="Menu", menu=myMenu)
        menu.add_cascade(label="Impressoras", menu=printers)
        menu.add_cascade(label="Sobre", command=self.about_window)

        def on_click(event):
            value.configure(state=NORMAL)
            value.delete(0, END)

            # make the callback only work once
            # value.unbind('<Button-1>', on_click_id)

        def generate():
            price = value.get()

            if not self.configs or not self.pixhos:
                messagebox.showwarning("showwarning", "Configurações/Qrcode não configurado!")
            else:
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

        Button(master, text='Gerar', command=generate).pack(
            side=LEFT,
            padx=5,
            ipady=8,
            ipadx=12,
        )

    def qrcode_window(self):  
        img= getQRCode(PAYLOAD_PIX).get_image()

        default_print = self.configs['prt_default']      
        # cube_s = int(self.configs['DEFAULT']['qrcode_size']) * int(img.size[0]/10)

        w,h = img.size;

        new_window = Toplevel(self.master)
        # new_window.title("QR Code - R$ " + str(self.price))
        new_window.title("QR Code - R$ 0,00")
        new_window.geometry(centralize_app(self.master, w,h))
        new_window.resizable(False, False)
        new_window.iconbitmap(ICONS_PATH["qr16Xico"])
        new_window.focus_force()
        new_window.grab_set()


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

        img = ImageTk.PhotoImage(img) # Transform to PhotoImage

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
        new_window.grab_set()


        message="""App para geração/impressão de pix\r\n dinânimo\r\n\r\nDesenvolvido por codexfast"""

        Label(new_window, text=message, width=120).place(relx=.5, rely=.5, anchor= CENTER)

    def config_window(self):
        new_window = Toplevel(self.master)
        new_window.title("Configurações")
        new_window.geometry(centralize_app(self.master, 250, 390))
        new_window.resizable(False, False)
        new_window.iconbitmap(ICONS_PATH["qr16Xico"])
        new_window.grab_set()

        notebook = ttk.Notebook(new_window)
        notebook.pack(expand=True)

        
        # create frames
        frame1 =Frame(notebook, width=400, height=280)
        frame2 =Frame(notebook, width=400, height=280)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        # add frames to notebook

        notebook.add(frame1, text='Pixhos')
        notebook.add(frame2, text='Impressora')

        Label(frame1, text="ALAAL", width=120).place(relx=.5, rely=.5, anchor= CENTER)


        

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
