# Bu dersin konusu Hata Yakalama...

# Bizim programcı olarak yakalayamadığımız hataları ,
# programın yakalaması için vaziyet alma ...
# import:çağır,aktar
# pass:geç ,görmezden gel demek.
# try:
#    import gmap
# except ModuleNotFoundError as e:
#     print("Kutuphane bulunamadi")
# except Exception as e:
#     print("Daha genel bir hata aldim..",str(e)) 
# else:     
#     print("Kutuphane bulundu..")
# finally:
#     print("Bu blokda işim bitti..") 
# print("Son print")       

# mList = [0,5,9]
# try:
#     print(mList[2])
# except Exception as e:
#     print("Bulunan Hata : ", str (e))
# else: 
#     print("Hata mevcut değil")
# finally:
#     print("Burda işim bitti.")

# print("Kodun son satiri..")


# ZeroDivisionEror:Sıfıra bölünebilinir mi? 
# a = 10 
# b = 0 
# try:
#     print (a/b)
# except ZeroDivisionError as e:
#     print("Sifira bolunur mu kardeşim..")    
# except Exception as e :
#     print("Hata : ",str (e))
# else:
#     print("İşlem başarili")
# finally:
#     print("Burda işim bitti")

# print("Program burda devam ediyor")




# a = "Merhaba"
# b = 5.2

# try:
#     print(a*b)
# except TypeError as e:
#     print("Float ve Str çarpilmaz..")
#     print("Ama Int ile çarpabilirsin")    
# except Exception as e:
#     print("Hata :",str (e))


# import math as m 
# z = -10
# try:
#     print(m.sqrt(z))

# except ValueError as e:
#     print("negatif sayının karekökü olmaz...")    
# except Exception as e:
#     print("Hata : ",str(e))

# print("matematik çok güzel")



# x=10
# try:
#     print(x)
# except NameError as e:
#     print("Bu nediir ")
# except Exception as e:
#     print("Hata :",str(e))        
# else:
#     print("İşlem başarılı")
# finally:
#     print("Burda işim bitti")    

# while True:
#     try: 
#         secim = input("Bir tam sayı giriniz :")
#         if secim.isdigit():
#             sonuc = secim*2
#             print("İşlem sonucu :", sonuc)
#             break
#     except AttributeError as e :
#         print("String bir fonksiyon yok..", str (e))
#     except ValueError as e:
#         print("Girdiğiniz değer int mi emin olun...",str (e))
#     except TypeError as e:
#         print("String değer ile üs alma işlemi yapılmaz..",str (e))            
#     except Exception as e:
#         print("Hata :",str(e)) 
#     else:
#         ("işlem başarılı") 
#     finally:
#         ("Burda işim bitti") 



# try:
#     dosya = open ("metin.txt","r")
# except NameError as r:
#     print("Değişken Tanımlanmadı..")    
# except Exception as e:
#     print(str(e))
# else:
#     print(dosya.read())
# finally:
#     dosya.close()            

# print(dosya.read())
       
# dosya açma modlarına bak!!!

