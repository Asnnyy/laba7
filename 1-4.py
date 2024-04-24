from PIL import Image
from PIL import Image, ImageFilter
def z1():
    image = Image.open('cat.png')
    image.show()

    print(f"размер: {image.size}")
    print(f"формат: {image.format}")
    print(f"цветовая модель: {image.mode}")
z1()

def z2():
    image = Image.open('cat.png')
    image2 = image.resize((image.width // 3, image.height // 3))
    image2 = image.rotate(180)
    image2 = image.transpose(Image.FLIP_LEFT_RIGHT)
    image2.save('cat2.png')
    image2.show()
z2()

def z3():
    image = Image.open('1.jpg')
    i1 = image.filter(ImageFilter.FIND_EDGES)
    i1.show()
    i1.save('f1.jpg')

    image = Image.open('2.jpg')
    i1 = image.filter(ImageFilter.FIND_EDGES)
    i1.show()
    i1.save('f2.jpg')

    image = Image.open('3.jpg')
    i1 = image.filter(ImageFilter.FIND_EDGES)
    i1.show()
    i1.save('f3.jpg')

    image = Image.open('4.jpg')
    i1 = image.filter(ImageFilter.FIND_EDGES)
    i1.show()
    i1.save('f4.jpg')

    image = Image.open('5.jpg')
    i1 = image.filter(ImageFilter.FIND_EDGES)
    i1.show()
    i1.save('f5.jpg')
z3()

def z4():
    image = Image.open('3.jpg')
    www = Image.open('znak.png')
    image.paste(www, (100,100), www)
    image.save('wznak.jpg')
    img = Image.open('wznak.jpg')
    img.show()
z4()