import time

""" 

Zamanim modülü Tarih va Saati döndüren , iki fonksiyonlu basit bir modüldür

"""


def Tarih():
    Trh = str(time.localtime()[2]) + "." + str(time.localtime()[1]) + "." + str(time.localtime()[0])

    return Trh 


def Saat():
    Sat = str(time.localtime()[3]) + ":" + str(time.localtime()[4])
    return Sat



if __name__ == '__main__':
    print(Tarih())
    print(Saat())
    input()
