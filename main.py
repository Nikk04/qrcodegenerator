from qrcodegenerator import QRCodeGenerator

if __name__ == "__main__":
    generatore = QRCodeGenerator()
    url_sito = input("Inserisci l'URL del tuo sito: ")

    try:
        generatore.generate_qr(url_sito)
    except ValueError as e:
        print(f"Errore: {e}")
