#  sonuc = (lambda a: a ** 2)(3)
multiply = lambda a: a ** 2
sonuc = multiply(5)

toplama = lambda a,b,c: a+b+c
sonuc = toplama(1,4,7)

tersCevir = lambda s: s[::-1]
sonuc = tersCevir("Sadık")

def myFunc(n):
    return lambda a: a * n

multiply2 = myFunc(2)
multiply3 = myFunc(3)

sonuc = multiply2(10)
sonuc = multiply2(20)
sonuc = multiply3(10)
print(sonuc)


sayilar =[1,2,5,7,9]
nensayilar =[1,-2,-5,-7,9]
kareleri=[]
str_sayilar =["1","2","5","7","9"]
isimler=["ali","deniz","veli","mehmet"]
kullanicilar=[
    {"ad":"deniz","soyad":"özcan"},
    {"ad":"özkan","soyad":"özcan"}
        
]
for sayi in sayilar:
    kareleri.append(sayi**2)

print(kareleri)

def kareAl(sayi):
    return sayi**2

sonuc1=map(kareAl, sayilar)
sonuc2=list(map(kareAl, sayilar))
sonuc3=list(map(lambda sayi: sayi**2, sayilar))
sonuc4=list(map(int, str_sayilar))# ınt to str
sonuc5=list(map(abs, nensayilar))
sonuc6=list(map(float, nensayilar))
sonuc7=list(map(len, isimler))
sonuc8=list(map(str.capitalize, isimler))
sonuc9=list(map(str.lower, isimler))
sonuc10=list(map(str.upper, isimler))
sonuc11=list(map(lambda x: x["ad"], kullanicilar))

print(sonuc2,sonuc3,sonuc4,sonuc5,sonuc6,sonuc7,sonuc8,sonuc9,sonuc10,sonuc11)

yaslar =[5,12,18,24,45]
sayilar =[0,1,2,25,6,8,9]
isimler=["Ali","deniz","veli","mehmet"]
kullanicilar=[
    {"ad":"deniz","tweets":["tw1","tw2","tw3","tw4"]},
    {"ad":"özkan","tweets":[]},
    {"ad":"alina","tweets":["tw1","tw3","tw7"]}
]
def yetiskimmi(x):
    if x<18:
        return False
    else:
        return True
for i in filter(yetiskimmi,yaslar):
    print (i)

sonuc1=list(filter(yetiskimmi,yaslar))
sonuc2=list(filter(lambda x: x>=18,yaslar))
sonuc3=list(filter(lambda x: x%2==0,sayilar))
sonuc4=list(filter(lambda x: x%2!=0,sayilar))
sonuc5=list(filter(lambda n: n[0]=="a" or n[0]=="A",isimler))
sonuc6=list(map(str.upper,filter(lambda n: n[0]=="a" or n[0]=="A",isimler)))
sonuc7=list(map(lambda n: n.lower(),filter(lambda n: n[0]=="a"or n[0]=="A",isimler)))
sonuc8=list(filter(lambda u: len(u["tweets"])>0,kullanicilar))
sonuc9=list(map(lambda u: u["ad"] ,filter(lambda u: len(u["tweets"])>0,kullanicilar)))
sonuc10= [user["ad"].upper() for user in kullanicilar if len(user["tweets"])>0]
print(sonuc1,sonuc2,sonuc3,sonuc4,sonuc5,sonuc6,sonuc7,sonuc8,sonuc9,sonuc10)

# ANYALL
sonuc = all([True,True,False])
sonuc = all([True,True,True])
sonuc = any([True,False,False])

#  And => True and True => True => All()
#  Or  => True or False => True => Any()

sayilar = [0,1,3,6,8,9,10]

sonuc = any([bool(sayi) for sayi in sayilar])
sonuc = all([bool(sayi) for sayi in sayilar])
sonuc = all([bool(sayi) for sayi in sayilar if sayi%2==1])
sonuc = all([sayi%2==0 for sayi in sayilar])
sonuc = any([sayi%2==0 for sayi in sayilar])

kisiler = ["ali","ahmet","çınar"]

sonuc = any([kisi[0]=='a' for kisi in kisiler])
sonuc = all([kisi[0]=='a' for kisi in kisiler if kisi[0]=='a'])

print(sonuc)

# SORTED
sayilar = [1,53,45,67,97,5,7]

#  sayilar.sort()
sonuc = sorted(sayilar)
sonuc = sorted(sayilar, reverse=True)
sonuc = sorted((1,53,45,67,97,5,7))


users = [
    {"username":"sadikturan", "tweets":["tweet 1","tweet 2"],"email":"info@gmail.com"},
    {"username":"cinarturan", "tweets":[]},
    {"username":"senaturan", "tweets":["tweet 1"],"name":"","phone":"434312134"}
]

sonuc = sorted(users, key=len)
sonuc = sorted(users, key=len, reverse=True)
sonuc = sorted(users, key=lambda user: user["username"])
sonuc = sorted(users, key=lambda  user: len(user["tweets"]))

kurslar = [
    {"title":"python kursu","students":25000},
    {"title":"web geliştirme kursu","students":35000},
    {"title":"javascript kursu","students":5000}
]

sonuc = sorted(kurslar, key=lambda kurs: kurs["students"])
sonuc = sorted(kurslar, key=lambda kurs: kurs["students"],reverse=True)
sonuc = map(lambda kurs: kurs["title"], sorted(kurslar, key=lambda kurs: kurs["students"],reverse=True))

print(list(sonuc))

# MIN-MAX
sayilar = [1,5,7,45,25,89]
harfler = ['a','v','h','s']
isimler = ['ahmet','ismail','ada','sena','sadık']

sonuc = min(sayilar)
sonuc = max(sayilar)

sonuc = min(harfler)
sonuc = max(harfler)

sonuc = min(isimler)
sonuc = max(isimler)

sonuc = min([len(isim) for isim in isimler])
sonuc = max([len(isim) for isim in isimler])

sonuc = max(isimler, key=lambda n: len(n))
sonuc = min(isimler, key=lambda n: len(n))

urunler = [
    {"title":"iphone x","price":5000},
    {"title":"iphone xr","price":6000},
    {"title":"iphone 11","price":7000}
]

sonuc = min(urunler, key=lambda urun: urun['price'])
sonuc = min(urunler, key=lambda urun: urun['price'])['title']
sonuc = max(urunler, key=lambda urun: urun['price'])['title']

max = 0

for urun in urunler:
    if urun["price"]>max:
        max = urun["price"]

print(max)

print(sonuc)

# SUM-ROUND
sayilar = [34,2,5,7,98]

sonuc = sum(sayilar)
sonuc = sum(sayilar, 10)

urunler = [
    {"title":"iphone x", "price": 5000},
    {"title":"iphone xr", "price": 6000},
    {"title":"iphone 11", "price": 7000},
    {"title":"iphone 11 Pro", "price": 0},
]


toplamFiyat = sum([urun["price"] for urun in urunler])
urunAdeti = len([urun for urun in urunler if urun["price"]>0])
sonuc = toplamFiyat / urunAdeti

sonuc = round(10.2)
sonuc = round(10.6)
sonuc = round(10.5)
sonuc = round(1.424242, 2)
sonuc = round(1.426242, 2)
sonuc = round(1.426242, 4)