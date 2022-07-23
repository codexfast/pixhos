## Vamos imprimir??
import win32.win32print as win32print
from escpos.printer import Network

def _print(printer, _raw):
    prt = win32print.OpenPrinter(printer)

    win32print.StartDocPrinter(prt, 1, ("undefined", None, 'raw'))
    win32print.WritePrinter(prt, bytes(_raw, 'utf-8'))
    win32print.EndDocPrinter(prt)
    win32print.ClosePrinter(prt)

def _print2(nw_ip): # On test
    kitchen = Network(nw_ip) #Printer IP Address
    kitchen.text("Hello World\n")
    kitchen.barcode('1324354657687', 'EAN13', 64, 2, '', '')
    kitchen.cut()


def getPrinters () -> win32print:
    return win32print.EnumPrinters(2)

def testPrt(prt: str):
    raw ="""Id ex Lorem sint id ad ullamco sit anim enim. Nulla commodo anim id amet qui. Esse irure exercitation officia aute laborum irure cillum. Dolor est dolore est nostrud ad sit ullamco laborum sunt nulla. Ut veniam nulla in excepteur tempor adipisicing ex ex minim nostrud proident non commodo."""


    _print(prt, raw)
if __name__ == "__main__": 
    for p in win32print.EnumPrinters(2):
        print(p[2])