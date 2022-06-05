import qrcode
from PIL import Image

print("\n")
text_input = input('Input your text: ')
print("\n")
print("converting . . . . .")

#simple way
#img = qrcode.make(text)

#advance way
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)
qr.add_data(text_input)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

#put logo
print("\n")
logo_aggreement = input('Do you want to put logo in the middle of your QR Code? (y/n): ')
if logo_aggreement == "y":
    logo_filename = input('Input your logo filename with extension: ')
    print("\n")
    print("adding logo . . . . .")
    logo_display = Image.open(logo_filename)
    logo_size = 450 * 0.25
    logo_display.thumbnail((logo_size, logo_size))
    logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
    img.paste(logo_display, logo_pos)

#saving
print("\n")
save_name = input('Input your output QR Code filename without extension: ')
print("\n")
print("saving . . . . .")
save_name = save_name + ".png"

img.save(save_name)

print("\n")
print("Process is finished . . . . .")
print("\n")
input("Press any button to close. . . . .")