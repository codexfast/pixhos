import qrcode

def getQRCode(payload: str) -> qrcode:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(payload)
    qr.make(fit=True)

    return qr.make_image(fill_color="black", back_color="white")