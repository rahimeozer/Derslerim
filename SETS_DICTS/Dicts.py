# # Dersin Konusu: Dictionary yapısı !!!
# arabam = {
#     "Marka" : "Mercedes",
#     "Model" : "E200",
#     "Yılı"  : 2023,
#     "Yakıtı": "LPG",
#     "Rengi" : "Siyah"
#  }

# arabam2 = dict(marka = "Doğan", model="slx",yili=1993,yakiti="LPG",rengi="Gri")

# print(arabam)
# print()
# print(arabam2["marka"])
# print(len(arabam))

# benimMarkam = arabam.get("Marka")
# print(benimMarkam)

# print(type(arabam.keys()))
# print(type(arabam.values()))

# arabam["Yılı"]=2024
# print(arabam)
# değiştirme burası

# items=arabam.items()
# print(items)

# keys içerisinde aratma için kullanılır...
# if "Mercedes" in arabam2:
#     print("Buldum")
# else:
#     print("Bulunamadı...")

# arabam.update({"Jant":25})
# print(arabam)

# silme
# arabam.popitem()
# print(arabam)

# del arabam["Rengi"]
# print(arabam)

# komple içini boşaltmak istersek
# arabam.clear()
# print(arabam)

# for i in arabam :
#     print(arabam[i])

# for anahtar,değer in arabam.items():
#    print(anahtar + " : " + str (değer)) 

# değiştirme , yeni kopyasını oluşturma 
# seninAraban = arabam.copy
# seninAraban = arabam (İkisini değiştirir..)
# seninAraban["Marka"]="Skoda"
# seninAraban["Model"]="Fabia"
# seninAraban["Yılı"] = 2012

# print(arabam)
# print(seninAraban)

# İç içe Dictionary :
# ailem = {
#     "Anne":{
#         "Adı":"Rahime ",
#         "Yasi": 28
#         },
#     "Baba":{"Adı":"Cabbar",
#             "Yasi": 35
#             },
#     "Kardeş":{
#         "Adı":"Aydan",
#         "Yasi":28
#         }

# }

# for anahtar,degerler in ailem.items():
#     print(anahtar)
#     for deger in degerler:
#         print(deger,":",degerler[deger]) 

# listem = [[1, 5, 7],
#           [10, 15, 18],
#           [30, 37, 39]
#           ]
# # Listeleri tek tek döndürüp yazdırır!!!
# for i in listem:
#     for j in i :
#         print(j,end=" ")
#     print()    
