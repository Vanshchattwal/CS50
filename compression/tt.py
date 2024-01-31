# import pybase64
# import qrcode
# import zlib

# with open("test.jpg", "rb") as image:
#     my_string = pybase64.b64encode(image.read())

# my_string = zlib.compress(my_string)

# # my_string = str(my_string)
# print(len(my_string))

# s = "123"

# img = qrcode.make(s)
# img.save("saved.jpg")


##----------------------encoding----------
import qrcode
import struct
import zlib
import pybase64

with open("test.jpg", "rb") as image:
    data = pybase64.b64encode(image.read())

# A long byte string
# data = b"Some very long data that exceeds the capacity of a single QR code"

# Compress the data using zlib
data = zlib.compress(data)

# Get the length of the compressed data
length = len(data)

# Split the data into chunks of 2,000 bytes each
chunks = [data[i:i+2000] for i in range(0, length, 2000)]

# Get the number of chunks
num_chunks = len(chunks)

# Loop through the chunks and generate QR codes
for i, chunk in enumerate(chunks):
    # Pack the chunk index and number of chunks into a header
    header = struct.pack(">HH", i, num_chunks)

    # Prepend the header to the chunk
    chunk = header + chunk

    # Create a QR code object with version 40 and error correction level L
    qr = qrcode.QRCode(
        version=40,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the chunk to the QR code object
    qr.add_data(chunk)

    # Make the QR code fit the chunk
    qr.make(fit=True)

    # Create an image from the QR code object
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image as a PNG file with a unique name
    img.save(f"qrcode_{i}.png")
