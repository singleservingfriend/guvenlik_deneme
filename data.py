#!python3

import sqlite3
import Zamanim #time modülü ile kendi yazdığım basit bir betik
import os
import urllib.request
from time import sleep
import NetKontrol # Sistemde internet var mı yok mu kontrol eden fonksiyonu içeren modül
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json






TARIH = Zamanim.Tarih()
SAAT  = Zamanim.Saat()

def Giris_Log_Tut():
    vt = sqlite3.connect("D:\\Databases\\girislog.db")
    im = vt.cursor()
    im.execute("CREATE TABLE IF NOT EXISTS giriszaman (tarih,saat)")
    im.execute("INSERT  INTO giriszaman (tarih,saat) VALUES ('"+TARIH+"','"+SAAT+"')")
    vt.commit()



def Giris_Log_Oku():
    vt = sqlite3.connect("D:\\Databases\\girislog.db")
    im = vt.cursor()
    im.execute("SELECT * FROM giriszaman")
    veri = im.fetchall()
    return veri


def Giris_Log_Ekrana_Bas():


    print("""

              TARİH     ZAMAN
              ---------------

              """)
    for i in Giris_Log_Oku():
        print("             ", i[0],   i[1])



def Resim_Goster():
	if os.path.exists("deneme.jpg"):
		os.startfile("deneme.jpg")
	else:
		print (" Resim Bulunamadi !!! " )

def Internet_Kontrol():
    kontrol = NetKontrol.InternetChecker()
    if kontrol.test_internet():
        return True
    else :
        return False


def Ag_Bilgi():
    ext_ip = urllib.request.urlopen('http://www.ipinfo.io/json').read()
    data = json.loads(ext_ip.decode("utf-8") )
    return data['ip']+ " " + data['city'] + " " + data['loc']




def Mail_Yolla():
    fromaddr = "mailsunucunuz" # Burasını mail atacak olan adres ile değişiniz
    toaddr = "hedefmail"       #  Burasını bilgi mailinin geleceği adres ile değişiniz 

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "self-made-man Güvenlik Maili"
    body = str(Giris_Log_Oku()[-1])+" "+"Tarihinde Bilgisayarınıza Giriş Yapıldı. " + Ag_Bilgi()
    msg.attach(MIMEText(body, 'plain'))
    filename = "deneme.jpg"
    attachment = open("D:\\PROGRAMLAMA\\Code Bank\\selfsecurity\\deneme.jpg", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "mailsifreniz")  #mail atacak adresin şifresini bu alana giriniz 
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()






if __name__ == '__main__':

    Giris_Log_Tut()

    os.system("py -2 resimal.py")

    if Internet_Kontrol():
        Mail_Yolla()
    else :
        pass
