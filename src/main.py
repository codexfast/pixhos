# Pixhos
# App para geração de QR Code de Pix com valor dinâmico

from utils.constants import PAYLOAD_PIX
from controllers.qrcodegen import getQRCode

def main():
    return getQRCode(PAYLOAD_PIX).save('./qrcode/qrcode.png')

if (__name__ == "__main__"):
    main()