from controllers.loadconfig import db_config
import qrcode

def getQRCode(payload: str) -> qrcode:
    cfg = db_config()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=int(cfg['qrcode_size']),
        border=int(cfg['qrcode_border']),
    )

    qr.add_data(payload)
    qr.make(fit=True)

    return qr.make_image(fill_color="black", back_color="white")