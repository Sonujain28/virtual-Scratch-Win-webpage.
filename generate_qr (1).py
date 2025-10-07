import qrcode

# Step 1: Add your website URL (Netlify URL)
url = "https://virtualscratchwinwebpage.netlify.app/shree_om_mobile.html"

# Step 2: Generate QR code
qr = qrcode.QRCode(
    version=1, 
    box_size=10, 
    border=4
)
qr.add_data(url)
qr.make(fit=True)

# Step 3: Create image of QR code
img = qr.make_image(fill_color="black", back_color="white")

# Step 4: Save QR code as PNG
img.save("scratch_and_win_qr.png")

print("QR code generated and saved as scratch_and_win_qr.png")
