#!Python2

from SimpleCV import Camera

"""

SimpleCV modulu ile kameradan resim alan fonksiyon icerir... 

"""



def resimcek():
    cam = Camera()
    img = cam.getImage()
    img.save("deneme.jpg")

    del cam
    del img 


if __name__ == '__main__':
    resimcek()
