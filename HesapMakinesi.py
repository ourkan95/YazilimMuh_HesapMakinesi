import math
import numpy as np


print("Hesap Makinesine Hoş Geldiniz... Yapmak istediğiniz İşlemi Seçiniz:")
islem = int(input("Toplama için 1 Bölme için 2: "))

if islem == 1:
    x = float(input("Toplanmak istenen ilk sayıyı giriniz: "))
    y = float(input("Toplanmak istenen ikinci sayıyı giriniz: "))
    
    sonuc = x + y
    print(sonuc)
if islem == 2:
    print("Bölme özelliği henüz eklenmedi")    