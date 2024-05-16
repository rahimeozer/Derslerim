import os
dosyaKonumu = "C:\\Users\\Rahos\\Documents\\Derslerim\\Python-Denemeleri\\DosyaIslemleri\\Sifre.txt"


def tumunuGoruntule(DosyaYolu):
    if os.path.exists(dosyaKonumu):
       with open(dosyaYolu,"r")as dosya:
        icerik = dosya.readlines()
        
        for satir in icerik :
            kullanıcıAdı,Sifre = satir.split(":")
            print("Kullanıcı Adı : {},Sifre :{}".format(kullanıcıAdı,Sifre.replace("\n",""))) 

    else : 
        print("Dosya mevcut değil...")

def kullanıcıEkle(DosyaYolu):
    if os.path.exists(DosyaYolu):
        yeniKullanıcıAdı = input("Kullanıcı Adı Giriniz :")
        yeniSifre = input("Şifre Giriniz :""\n")
        with open(DosyaYolu,"a")as dosya:
            dosya.write(yeniKullanıcıAdı+":"+yeniSifre)

    else:
        print("Dosya mevcut değil...")
        exit()    

def kullanıcıSil(DosyaYolu):
    if os.path.exists(DosyaYolu):
        kullanıcıAdı = input("Silinecek kullanıcı adı giriniz :")
        with open (DosyaYolu,"r") as dosya:
           icerik = dosya.readlines()

        for i,satir in enumerate (icerik) :
           if kullanıcıAdı in satir:
               icerik.pop(i)
       
        with open (DosyaYolu,"w")as dosya:
             dosya.writelines(icerik)



    else :
        print("Dosya mevcut değil..")                 
    
print("Secenekleriniz :\n"
      "1.Kullanıcı ve Sifre Görüntüle\n"
      "2.Kullanıcı Ekle\n"
      "3.Kullanıcı Silme\n"
      "4.Sifre Değistirme\n"
      "5.Cıkıs\n"
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
    None
    #SifreDegistirme
elif cevap ==  "5":
    None
    exit()
else:
    print("DALGA MI GEÇİYON ADAM MI SEÇİYON KARDEŞİMM...")          