


# pip install qrcode
import qrcode

link = "https://instagram.com/technicallyripped"

qr = qrcode.QRCode(version=1)

qr.add_data(link)

qr.make(fit=True)

qr_image = qr.make_image(fill_color="black", back_color="white")

qr_image.save("1qrcode.png")



































