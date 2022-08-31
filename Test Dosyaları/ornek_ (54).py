
# LISTSCOMPREHENSION
sayilar1 = []
for i in range(10):
    sayilar1.append(i)
# [expression for item in list]
sayilar2 = [i for i in range(12)]
sayilar3 = [i*i for i in range(12)]
sayilar4 = [i**3 for i in range(12)]
print(sayilar1, sayilar2, sayilar3, sayilar4)
sayilar5 = []
liste1 = [10, 4, 7, 9, 70]
for i in liste1:
    i *= 2
    sayilar5.append(i)
print(sayilar5)
sayilar6 = [i*2 for i in liste1]
print(sayilar6)

isim = "deniz"
isimler = ["deniz", "ahmet", "mehmet", "çınar"]
print([c.upper() for c in isim])
print([str(c) for c in liste1])
print([c.upper() for c in isimler])
print([c.lower() for c in isimler])
