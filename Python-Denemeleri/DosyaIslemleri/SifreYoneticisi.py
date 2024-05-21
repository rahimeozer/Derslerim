import os
from cryptography.fernet import Fernet

dosyaKonumu = "C:\\Users\\Rahos\\Documents\\Derslerim\\Python-Denemeleri\\DosyaIslemleri\\Sifre.txt"

anahtarKonumu = "C:\\Users\\Rahos\\Documents\\Derslerim\\Python-Denemeleri\\DosyaIslemleri\\key.data"
# Sadece Bir Kere 
def anahtarOlustur():
    key = Fernet.generate_key()
    with open(anahtarKonumu,"wb")as dosya:
        dosya.write(key)
def anahtarOku():
    with open(anahtarKonumu,"rb")as dosya:
        key = dosya.read()
        return key 
    


    
# print("Anahtar",key)

anahtarOlustur()
key  = anahtarOku()
anahtar = Fernet(key)


def tumunuGoruntule(dosyaYolu):
    global anahtar
    if os.path.exists(dosyaKonumu):
       with open(dosyaYolu,"r")as dosya:
        icerik = dosya.readlines()
        
        for satir in icerik :
            kullanıcıAdı,Sifre = satir.replace("\n","").split(":")
            sifre=anahtar.decrypt(Sifre.encode()).decode()
            print("Kullanıcı Adı : {},Sifre :{}".format(kullanıcıAdı,Sifre)) 

    else : 
        print("Dosya mevcut değil...")

def kullanıcıEkle(DosyaYolu):
    global anahtar
    if os.path.exists(DosyaYolu):
        yeniKullanıcıAdı = input("Kullanıcı Adı Giriniz :")
        yeniSifre = input("Şifre Giriniz :""\n")
        yeniSifre= anahtar.encrypt(yeniSifre.encode()).decode()
        with open(DosyaYolu,"a")as dosya:
            dosya.write(yeniKullanıcıAdı+":"+yeniSifre+ "\n")
    else:
        print("Dosya mevcut değil...")
        exit()    

def kullanıcıSil(DosyaYolu):
    if os.path.exists(DosyaYolu):
        kullanıcıAdı = input("Silinecek kullanıcı adı giriniz :")
        with open (DosyaYolu,"r") as dosya:
           Tümİcerik = dosya.read()
           if kullanıcıAdı not in Tümİcerik:
               print("Kullanıcı bulunamadı..")
               return
           
           dosya.seek(0)
           icerik = dosya.readlines()

        for i,satir in enumerate (icerik) :
           if kullanıcıAdı in satir:
               icerik.pop(i)
       
        with open (DosyaYolu,"w")as dosya:
             dosya.writelines(icerik)

    else :
        print("Dosya mevcut değil..")  

def SifreDegistirme(path):
    global anahtar
    if os.path.exists(path):
        kullanıcıAdı=input("Şifresi değiştirilecek kullanıcı adını giriniz :")
        with open(path,"r")as dosya:
            Tümicerik = dosya.read()
            if kullanıcıAdı not in Tümicerik:
                print("Kullanıcı bulunamadı")
                return
            
            dosya.seek(0)
            icerik = dosya.readlines()

    for idx ,satir in enumerate (icerik) :
        if kullanıcıAdı in satir:
            kullanıcıAdı, sifre = satir.replace("\n","").split(":")
            sifre = input("Yeni şifre giriniz : ")
            sifre = anahtar.encrypt (sifre.encode()).decode()
            icerik[idx] = kullanıcıAdı + ":" +sifre +"\n"
            break
        # print( "Şifre başarı ile değiştirildi")

        with open (path,"w") as dosya:
            dosya.writelines(icerik)

       
print("Secenekleriniz :\n"
      "1.Kullanıcı ve Sifre Görüntüle\n"
      "2.Kullanıcı Ekle\n"
      "3.Kullanıcı Silme\n"
      "4.Sifre Değistirme\n"
      "5.Anahtar Oluştur\n"
      "6.Cıkıs\n"
      "İslem >:")
cevap = input("Bir Secenek seciniz :")

if cevap == "1":
    tumunuGoruntule(dosyaKonumu)
    # TümünüGörüntüle 
elif cevap == "2":
    kullanıcıEkle(dosyaKonumu)
    #KullanıcıEkle
elif cevap =="3":
    kullanıcıSil(dosyaKonumu)
    #KullanıcıSilme
elif cevap =="4":
    SifreDegistirme(dosyaKonumu)
    #SifreDegistirme
elif cevap ==  "5":
    anahtarOlustur()
    key = anahtarOku()
    anahtar = Fernet(key)
elif cevap == "6":
    exit()    
else:
    print("DALGA MI GEÇİYON ADAM MI SEÇİYON KARDEŞİMM...")          