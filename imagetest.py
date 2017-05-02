import base64

# with open("myimagecopy.png", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
encoded = base64.b64encode(open("bigimage.jpg", "rb").read())
print(encoded)
target = open('image.txt', 'w')
target.write(str(encoded)[2:-1])
target.close()
