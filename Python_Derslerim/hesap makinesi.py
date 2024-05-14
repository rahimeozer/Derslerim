def toplama(num1:int, num2:int)->int:
    return num1+num2 

def cikarma(num1:int, num2:int)->int:
    return num1-num2

def çarpma(num1:int, num2:int)->int:
    return num1*num2

def bölme(num1:int, num2:int)->int:
    return num1/num2 

def kokalma(num1:int, num2:int)->int:
    return num1**1/num2 

def kuvvetalma(num1:int, num2:int)->int:
    return num1**num2

def bölümdenkalan(num1:int, num2:int)->int:
    return num1%num2
while True :
   secim = input("1.Toplama\n"\
              "2.Cikarma\n"\
              "3.Çarpma\n"\
              "4.Bölme\n"\
              "5.Kok Alma\n"\
              "6.Kuvvetini Alma\n"\
              "7.Bölümden Kalani Bulma\n"\
              "8.Cikiş\n"\
              "Seçiminiz > " )
   if secim =="8":
        exit() 
                
   if not secim.isdigit():
        print("Lütfen 1-8 arasi sayi giriniz.")
   elif int(secim) not in range(1,9):
       print("Aralik disi sayi girdiniz!!!")

   a = int(input("1.Sayiyi Giriniz: "))
   b = int(input("2.Sayiyi Giriniz: "))

   sonuc = 0

   if secim == "1":
       sonuc=toplama(a,b)
   elif secim == "2":
       sonuc=cikarma(a,b)
   elif secim == "3":
       sonuc=çarpma(a,b)
   elif secim == "4":
       sonuc=bölme(a,b)
   elif secim == "5":
       sonuc=kokalma(a,b)
   elif secim == "6":
       sonuc=kuvvetalma(a,b)
   elif secim == "7":
       sonuc=bölümdenkalan(a,b) 

   print("İşleminizin sonucu:",format(sonuc))       


