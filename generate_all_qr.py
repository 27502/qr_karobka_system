import qrcode
import json

with open("karobkalar.json", "r") as f:
    karobkalar = json.load(f)

for karobka_id in karobkalar:
    url = f"http://localhost:5000/karobka/{karobka_id}"
    img = qrcode.make(url)
    img.save(f"karobka_{karobka_id}_qr.png")
    print(f"QR code yaratildi: karobka_{karobka_id}_qr.png")
