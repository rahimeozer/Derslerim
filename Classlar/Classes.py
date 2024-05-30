# Dersin Konusu:Class'lar
# Sınıf adı yazılırken baş harfi daima büyük olur..
class SinifAdi: 
    "Sinifin tanimlama dokumantasyon metni"
    # Sınıfın elemanları ve fonksiyonları...

"""

__doc__
__name__
__module__
__bases__

"""

# print("Doc :",SinifAdi.__doc__)
# print("Name:",SinifAdi.__name__)
# print("Module:",SinifAdi.__module__)
# print("Base:",SinifAdi.__bases__)

#self : kendi , referans ,yazdığımız bütün fonksiyonların içine ilk self yazacağız..
class Calisan:
    "Fabrikamizda calisan personel bilgileri icin sinif"
    calisanSayisi = 0

    def __init__(self, adi, soyadi, yasi):
        self.adi = adi
        self.soyadi = soyadi
        self.yasi= yasi
        Calisan.calisanSayisi+=1
        print("Nesne Olusturuldu...")
    
    # def __del__(self):
    #     print("Yikici calisti..") 
    
    def bilgileriDok(self):
        print(self.adi)
        print(self.soyadi)  
        print(self.yasi)
        print("Calisan Sayisi :" , Calisan.calisanSayisi)     

isci = Calisan("Rahime","Özer",28)
isci2 = Calisan("İnci","Boncuk",15)


isci.bilgileriDok()
isci.bilgileriDok()



# print(isci.adi)
# print(isci.soyadi)
# print(isci.yasi)





    
        
     

