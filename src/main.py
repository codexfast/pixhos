## Pixhos
## App para geração de QR Code de Pix com valor dinâmico

# from utils.constants import PAYLOAD_PIX

# from controllers.qrcodegen import getQRCode
# from controllers.loadconfig import configs

from gui import initialize as init

def main():
    # cfg = configs()
    # print(cfg['DEFAULT']['printer'])

    init()
    return 0;

if (__name__ == "__main__"):
    main()
    # try:
    #     main()
    # except:
    #     print("Erro desconhecido")