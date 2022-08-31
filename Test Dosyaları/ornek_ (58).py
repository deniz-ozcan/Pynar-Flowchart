list = ["1", "2", "5a", "10b", "abc", "10", "50"]

for i in list:
    try:
        a = int(i)
        print(10*a)
    except ValueError:
        print("Sayısal bilgi giriniz.")
        continue


while True:
    x = input("bir deger giriniz: ")
    if (x == "q"):
        break
    try:
        a = int(x)
        print(f"girilen sayi {a}.")
        break
    except ValueError:
        print("bilinmeyen bir hata oluştu")
        continue

urun = {"urunAdi:": "XR"}


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None
print(get(urun, "fiyat"))
