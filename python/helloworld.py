from PIL import Image, ImageFilter

before = Image.open("1.jpg")
after = before.filter(ImageFilter.BLUR)
after.save("out.jpg")