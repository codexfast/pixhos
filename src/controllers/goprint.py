## Vamos imprimir??
import win32.win32print as win32print

def _print(printer, _buffer=b'test'):
    prt = win32print.OpenPrinter(printer)

    win32print.StartDocPrinter(prt, 1, ("undefined", None, None))
    win32print.WritePrinter(prt, _buffer)
    win32print.EndDocPrinter(prt)
    win32print.ClosePrinter(prt)

def getPrinters () -> win32print:
    return win32print.EnumPrinters(2)

if __name__ == "__main__": 
    for p in win32print.EnumPrinters(2):
        print(p[2])