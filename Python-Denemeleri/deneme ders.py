from random import randint

bilgisayarSecimi = randint(1,100)
MIN = 1
MAX = 100
tahminListesi = []
while True:
    kullaniciSecimi = input("{}-{} arasinda sayi  giriniz : ".format(MIN,MAX))

    if kullaniciSecimi== "q":
        break
    elif not kullaniciSecimi.isdigit():
        print( "Sayi giriniz..")
        continue
    
    kullaniciSecimi=int(kullaniciSecimi)

    tahminListesi.append(kullaniciSecimi)
    
    if kullaniciSecimi > bilgisayarSecimi:
        print("Daha küçük olmali")
        MAX = kullaniciSecimi

    elif bilgisayarSecimi > kullaniciSecimi:
        print("Daha büyük olmali")
        MIN = kullaniciSecimi

    elif bilgisayarSecimi == kullaniciSecimi:
        print("Tebriklerrr....")
        break
    
for idx,i in enumerate(tahminListesi):
    print(idx+1,".Tahmin :",i)

print("Kullanicinin Tahmin Sayisi : {} ".format(len(tahminListesi)))
    
