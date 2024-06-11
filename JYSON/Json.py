import json 

myDict = {"Adi":"Python","yasi":45, "renklimi": False,"hayattami": True,"sevdiği meyve": None}

# print(myDict["hayattami"])

# for key, val in myDict.items():
#     print(key,val)

# print(myDict)
# print(type(myDict))
# jsonStr = json.dumps(myDict,indent=4,sort_keys=True)
# print(jsonStr)
# print(type(jsonStr))

# try:
#     myJsonStr = '{"Adi": "Python", "yasi": 45, "renklimi": False, "hayattami": true, "sevdi\u011fi meyve": null}'
#     newDict = json.loads(myJsonStr)
# except Exception as e :
#     print(str(e))
#     print:("JSON String Dönüşüm Hatası")
# else:
#     print(type(newDict))
#     print(newDict)

#try:Hele bi qardaşş dene 
# except : Exception as e :  sorun çıkarsa bunu yap 
# else : çıkmazsa bunu yap 
# finally :  

# ...........................................................................
# Dosya açma 
path = "C:\\Users\\Rahos\\Documents\\Derslerim\\JYSON\\some.json"

with open(path)as jFile:
    data = json.load(jFile)
    print(type(data))
    print(data)

jString = json.dumps(data,indent=4) 
print(jString) 

print(data["cars"][1]["hacim"])
