import qrcode

data = input("Enter text or URL to gen QR code: ")
img = qrcode.make(data)
img.save("qrcode.png")
print("QR code saved.")
