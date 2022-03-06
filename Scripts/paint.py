from PIL import Image, ImageDraw

img = Image.open("../Plot/y(x).png")

draw = ImageDraw.Draw(img)
draw.ellipse((100, 100, 50, 50), fill=(255, 0, 0))
img.save("../Plot/y(x).png")
