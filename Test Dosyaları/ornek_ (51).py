kilo = int(input("kilonuz(KG): "))
boy = int(input("boyunuz(CM): "))
sonuc5 = (kilo)/((boy/100)**2)
if sonuc5 > 0.0 and 18.4 > sonuc5:
    print("ZAYIF")
elif sonuc5 > 18.5 and sonuc5 < 24.9:
    print("NORMAL")
elif sonuc5 > 25.0 and sonuc5 < 29.9:
    print("FAZLA KİLOLU")

elif sonuc5 > 30.0 and sonuc5 < 34.9:
    print("OBEZ")
else:
    print("hatalı tuşlama yaptınız.")