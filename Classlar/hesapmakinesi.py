""""HESAP MAKİNESİ YAPIMI"""

import tkinter as tk

def hesapla():
    metin = giris.get()
    result = eval(metin)
    giris.insert(tk.END,"=" + str(result))

anapencere = tk.Tk()

anapencere.title("hesap makinesi")
anapencere.geometry("500x100")

giris = tk.Entry(anapencere,width=15)
giris.pack(side=tk.LEFT)

btn = tk.Button(anapencere, text="hesapla", command=hesapla)
btn.pack(side=tk.LEFT)

anapencere.mainloop()