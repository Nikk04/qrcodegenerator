import qrcode


class QRCodeGenerator:
    def generate_qr(self, url):
        if not url:
            raise ValueError("Il testo non è stato inserito. Inserisci un testo valido.")

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("imgqrcode.png")
        img.show()
