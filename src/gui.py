from tkinter import *
from PIL import Image, ImageTk

from utils.constants import PAYLOAD_PIX

from controllers.qrcodegen import getQRCode
from controllers.loadconfig import configs

class Application:
    def __init__(self, master=None):
        self.configs = configs()

        self.fonte = ("Verdana", "8")
        self.master = master

        self.price=0.00

        # add menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        myMenu = Menu(menu, tearoff=0)
        myMenu.add_separator()
        myMenu.add_command(label="exit", command=self.master.destroy)

        menu.add_cascade(label="Menu", menu=myMenu)
        menu.add_cascade(label="Options")

        def on_click(event):
            value.configure(state=NORMAL)
            value.delete(0, END)

            # make the callback only work once
            value.unbind('<Button-1>', on_click_id)

        def get_value_and_gen():
            price = value.get()
            
            self.qrcode_window()

        value = Entry(master, justify=RIGHT, width=28)
        value.insert(0, '0.00')
        value.configure(state=DISABLED)

        value.pack(
            side=LEFT,
            padx=15, 
            ipady=8,
            ipadx=8
        )

        on_click_id = value.bind('<Button-1>', on_click)

        Button(master, text='Gerar', command=get_value_and_gen).pack(
            side=LEFT,
            padx=5,
            ipady=8,
            ipadx=12
        )

    def qrcode_window(self):
        cube_s = int(self.configs['DEFAULT']['qrcode_size']) * 49

        new_window = Toplevel(self.master)
        # new_window.title("QR Code - R$ " + str(self.price))
        new_window.title("QR Code - R$ 0,00")
        new_window.geometry(centralize_app(self.master, cube_s, cube_s))
        new_window.resizable(False, False)

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

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    root.title('Pixhos')
    root.resizable(False, False)
    # root.attributes('-topmost', 1)
    root.geometry('{}x{}+{}+{}'.format(window_width, window_height, center_x, center_y))

    root.mainloop()
    return 0;
