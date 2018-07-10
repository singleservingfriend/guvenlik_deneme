#! python3
from data import *
from os import system
from sys import exit
from time import sleep




karsilama = """

              okkangal Kişisel Güvenlik Sistemi


            """


menu = """
        [L] Giriş Kayıtlarını Oku
        [R] Son Kullanıcının Resmi 
        [C] ...
        [X] Çıkış 

       """


print(karsilama)
print(menu)



while True :
    secim = input()
    if secim == "l" :        
        system("cls")
        print(karsilama)
        print(menu)
        Giris_Log_Ekrana_Bas()
        print(menu)
    elif secim == "r" :
        Resim_Goster()
    elif secim == "x" :
        system("cls")
        print("Hoşçakalın")
        sleep(2)
        exit()        

    else :
        print("Lütfen Geçerli Bir Seçim Yapınız...")
        
