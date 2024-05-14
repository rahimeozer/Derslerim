

dosya =open("C:\\Users\\Rahos\\Documents\\Derslerim\\Python-Denemeleri\\DosyaIslemleri\\mtin.txt","r",encoding="UTF-8")


icerik = dosya.readlines()
for satir in icerik:
    print(satir)

#Bu değişikliği öylesinde yaptım.
