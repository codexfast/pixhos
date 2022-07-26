## Vamos imprimir??

from escpos.printer import Network

import win32.win32print as win32print
import abc

class PrintTemplate(metaclass=abc.ABCMeta):
    def hello_world(self):
        self.text("Hello World")
        self.ln(10)
        self.cut()

    def pixhos(self, payload, amount, name, key):
        self.textln(GoPrint.spaceBetween("PIX", f"R${amount}"))
        self.qr(payload, size=6)
        self.textln(GoPrint.spaceBetween("", key))
        self.textln(GoPrint.spaceBetween("", name))
        self.cut()


class GoPrint(Network, PrintTemplate):
    def __init__(self, host, port=9100, timeout=5, *args, **kwargs):
        try:
            super().__init__(host, port, timeout, *args, **kwargs)
        except OSError:
            print(f'Conection Error [{host}]')

    @staticmethod
    def spaceBetween(text1:str, text2:str, width:int =25) -> str:

        if (len(text1) + len(text2)) > width: raise Exception(f'Text is long, max width: {width}')

        text = text1.ljust(width - len(text2), ' ')
        text += text2

        return text

    def test(self):
        self.text("Irure proident eiusmod enim nostrud laborum sit.")
        self.qr("http://www.google.com",)
        self.barcode("123123123")
        self.textln("With new line")
        self.text("More a text")
        self.ln(10)
        self.block_text("Cillum laboris veniam consectetur veniam in culpa tempor et Lorem elit quis.", columns=3)
        self.set(align='right')
        self.textln('Right text')
        self.set(align='left')
        self.textln('Left text')
        self.textln(self.spaceBetween("Left", "Right"))
        self.cut()

    def __del__(self): pass

def _print(printer, _raw):
    prt = win32print.OpenPrinter(printer)

    win32print.StartDocPrinter(prt, 1, ("undefined", None, 'raw'))
    win32print.WritePrinter(prt, bytes(_raw, 'utf-8'))
    win32print.EndDocPrinter(prt)
    win32print.ClosePrinter(prt)


def getPrinters () -> win32print:
    return win32print.EnumPrinters(2)

if __name__ == "__main__": 
    # for p in win32print.EnumPrinters(2):
    #     print(p[2])

    bar = GoPrint('192.168.0.1', timeout=5)
    # bar.hello_world()
    # bar.test()