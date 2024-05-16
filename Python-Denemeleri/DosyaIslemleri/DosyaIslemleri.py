
# Absolute Path
dosyaKonumu = "C:\\Users\\Rahos\\Documents\\Derslerim\\Python-Denemeleri\\DosyaIslemleri\\mtin.txt"


#Relative Path
dk = ".\\DosyaIslemleri\\mtin.txt"




# dosya = open(dk,"r" , encoding="utf-8")

# encoding=Türkçe karakter tanıma fonksiyonu 

# print (dosya.tell())
# icerik = dosya.read(10)

# print (dosya.tell())
# icerik2 = dosya.read(3)

# print(dosya.tell())
# print(icerik)
# print(icerik2)

# tell = İmlecin konumunu gösterir..


# satir1 = dosya.readline().replace("\n","")
# print(dosya.tell())
# satir2 =dosya.readline()
# print(dosya.tell())

# print(satir1)
# print(satir2, end="")

# satirlar = dosya.readlines()
# print(type(satirlar))

# for satir in satirlar:
#     print(satirlar)

# dosya = open(dosyaKonumu , "r+" , encoding="utf-8")

# print("Dosya açıldıktan sonra konum :",dosya.tell())

# dosya.write("Benim adım Ebruli..."+"\n")
# icerik = dosya.read()
# print(icerik)

# print("Yazdıktan sonra :",dosya.tell())



# icerik = dosya.readlines()
# icerik.insert(1, "Benim adım Batman"+"\n")
# print(icerik)
# dosya.writelines(icerik)
# dosya.seek(0)

# print("Dosya okunabilir mi :",dosya.readable())


import os
if os.path.exists(dosyaKonumu):
    print("Dosyayi buldum, İslem yapiyorum")
    with open (dosyaKonumu,"r+") as dosya :
         icerik = dosya.read()
         print(icerik)
else:
    print("Dosya bulunamadı...")











 