


# pip install qrcode
import qrcode

link = "https://www.youtube.com/@TechnicallyRipped"

qr = qrcode.QRCode(version=1)

qr.add_data(link)

qr.make(fit=True)

qr_image = qr.make_image(fill_color=(225,70,190), back_color=(155,204,40))

qr_image.save("qrcode.png")
