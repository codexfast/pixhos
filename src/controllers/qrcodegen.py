from controllers.loadconfig import configs

import qrcode

def getQRCode(payload: str) -> qrcode:

    cfg = configs()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=int(cfg['DEFAULT']['qrcode_size']) or 7,
        border=4,
    )

    qr.add_data(payload)
    qr.make(fit=True)

    return qr.make_image(fill_color="black", back_color="white")