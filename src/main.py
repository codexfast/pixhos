# Pixhos
# App para geração de QR Code de Pix com valor dinâmico

from utils.constants import PAYLOAD_PIX

from controllers.qrcodegen import getQRCode
from controllers.loadconfig import configs

def main():
	# qrcode = getQRCode(PAYLOAD_PIX)
    # return getQRCode(PAYLOAD_PIX).save('./qrcode/qrcode.png')

    print(configs().sections())

    return 0;

if (__name__ == "__main__"):
    main()