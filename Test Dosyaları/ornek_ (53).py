e = int(input("1.sınav: "))
r = int(input("2.sınav: "))
t = int(input("3.sınav: "))
sonuc4 = (e+r)*(0.6)+(t*0.4)
if sonuc4 > 50 and t > 50:
    print("Geçti")
elif sonuc4 > 50 and t < 50:
    print("final ile kaldı")
elif sonuc4 < 50:
    print("50 altı ortalalama ile kaldı")
elif t > 70:
    print("ortalamaya bakılmadan geçti")
else:
    print("hatalı tuşlama yaptınız.")