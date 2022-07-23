
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
                messagebox.showwarning("Atenção!", "Configurações/Qrcode não configurado!")
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

    def create_input_frame2(self, container):

        frame = ttk.Frame(container)

        # grid layout for the input frame
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(0, weight=4)

        # prt default
        ttk.Label(frame, text='Impressora:').grid(column=0, row=0, sticky=W)
        # keyword = ttk.Entry(frame, width=30)
        
        selected_prt = StringVar()
        cb_prt=ttk.Combobox(frame, textvariable=selected_prt, width=25)
        cb_prt['values'] = list(map(lambda x: x[2],getPrinters()))
        cb_prt.grid(column=1, row=0, sticky=W)


        # QRcode size:
        ttk.Label(frame, text='Tamanho (QRcode)').grid(column=0, row=1, sticky=W)
        # replacement = ttk.Entry(frame, width=30)
        qrcode_size_value = StringVar()
        qrcode_size_spin_box = ttk.Spinbox(
            frame,
            from_=2,
            to=12,
            # values=(0, 10, 20, 30, 40, 50),
            textvariable=qrcode_size_value,
            state = 'readonly',
            width=25
            )
        qrcode_size_spin_box.grid(column=1, row=1, sticky=W)

        # Qrcode Border size:
        ttk.Label(frame, text='Borda (QRcode)').grid(column=0, row=2, sticky=W)
        
        qrcode_border_value = StringVar()
        qrcode_border_value.set(2)
        qrcode_border_spin_box = ttk.Spinbox(
            frame,
            from_=2,
            to=12,
            # values=(0, 10, 20, 30, 40, 50),
            textvariable=qrcode_border_value,
            state = 'readonly',
            width=25,
            
            )
        qrcode_border_spin_box.focus()
        qrcode_border_spin_box.grid(column=1, row=2, sticky=W)

        # Match Case checkbox
        # match_case = StringVar()
        # match_case_check = ttk.Checkbutton(
        #     frame,
        #     text='Match case',
        #     variable=match_case,
        #     command=lambda: print(match_case.get()))
        # match_case_check.grid(column=0, row=2, sticky=W)

        # # Wrap Around checkbox
        # wrap_around = StringVar()
        # wrap_around_check = ttk.Checkbutton(
        #     frame,
        #     variable=wrap_around,
        #     text='Wrap around',
        #     command=lambda: print(wrap_around.get()))
        # wrap_around_check.grid(column=0, row=3, sticky=W)

        for widget in frame.winfo_children():
            widget.grid(padx=0, pady=5)

        return frame
        
    def create_button_frame2(self, container):
        frame = ttk.Frame(container)

        frame.columnconfigure(0, weight=1)

        ttk.Button(frame, text='Salvar').grid(column=0, row=0)
        ttk.Button(frame, text='Testar Imp').grid(column=0, row=1)

        for widget in frame.winfo_children():
            widget.grid(padx=0, pady=3)

        return frame


    def config_window(self):
        w = 390
        h = 250

        new_window = Toplevel(self.master)
        new_window.title("Configurações")
        new_window.geometry(centralize_app(self.master, h, w))
        new_window.resizable(False, False)
        new_window.iconbitmap(ICONS_PATH["qr16Xico"])
        new_window.grab_set()

        notebook = ttk.Notebook(new_window)
        notebook.pack(expand=True)

        
        # create frames
        frame1 =Frame(notebook, width=w, height=h)
        frame2 =Frame(notebook, width=w, height=h)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        # add frames to notebook

        notebook.add(frame1, text='Pixhos')
        notebook.add(frame2, text='Impressora')

        # layout frame 2
        frame2.columnconfigure(0, weight=4)
        frame2.columnconfigure(1, weight=1)

        input_frame = self.create_input_frame2(frame2)
        input_frame.grid(column=0, row=0)

        button_frame = self.create_button_frame2(frame2)
        button_frame.grid(column=1, row=0)

        # Printers
        # lb_select_prt = Label(frame2, text="Impressora Padrão", background="RED")
                
        # selected_prt = StringVar()
        # prt_cb = ttk.Combobox(frame2, textvariable=selected_prt)

        # # get first 3 letters of every prt name
        # prt_cb['values'] = list(map(lambda x: x[2],getPrinters()))

        # # prevent typing a value
        # prt_cb['state'] = 'readonly'

        # # bind the selected value changes
        # def prt_changed(event):
        #     print(selected_prt.get())

        # prt_cb.bind('<<ComboboxSelected>>', prt_changed)

        # # spinbox
        # lb_qrcode_size = Label(frame2, text="Tamanho (QRcode)")
        # qrcode_size_value = StringVar()
        # qrcode_size_spin_box = ttk.Spinbox(
        #     frame2,
        #     from_=0,
        #     to=12,
        #     # values=(0, 10, 20, 30, 40, 50),
        #     textvariable=qrcode_size_value,
        #     state = 'readonly'
        #     )

        # spinbox
        # lb_qrcode_border = Label(frame2, text="Tamanho Borda (QRcode)")

        # qrcode_border_value = StringVar()
        # qrcode_border_spin_box = ttk.Spinbox(
        #     frame2,
        #     from_=0,
        #     to=12,
        #     # values=(0, 10, 20, 30, 40, 50),
        #     textvariable=qrcode_border_value,
        #     state = 'readonly'
        #     )

        # GRID
        # lb_select_prt,
        # qrcode_border_spin_box,
        # qrcode_size_spin_box,
        # prt_cb

        # lb_select_prt.grid(row=0, column=0, padx=5,pady=5)
        # prt_cb.grid(row=0, column=1, padx=5,pady=5, columnspan=1)

        # lb_qrcode_border.grid(row=1, column=0, padx=5,pady=5)
        # qrcode_border_spin_box.grid(row=1, column=1, padx=5,pady=5)
        
        # lb_qrcode_size.grid(row=2, column=0, padx=5,pady=5)
        # qrcode_size_spin_box.grid(row=2, column=1, padx=5,pady=5)
        

        # ----- end printers

        


        

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
