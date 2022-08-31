urunler = [
    {"id":1, "urunAdi":"iphone 8", "fiyat":5000},
    {"id":2, "urunAdi":"iphone XR", "fiyat":6000},
    {"id":3, "urunAdi":"iphone 11", "fiyat":7000},
    {"id":4, "urunAdi":"iphone 12", "fiyat":8000}
]

def urunEkle(urunAdi,fiyat):
    urunler.append({
        "id": len(urunler) + 1,
        "urunAdi": urunAdi,
        "fiyat": fiyat
    })

def urunGuncelle(id, urunAdi, fiyat):
    for urun in urunler:
        if(urun["id"] == id):
            urun["urunAdi"] = urunAdi
            urun["fiyat"]=fiyat
            break

def urunleriGetir():
    for urun in urunler:
        print(f"id {urun['id']} ürün adı: {urun['urunAdi']} fiyat: {urun['fiyat']}")

urunleriGetir()
print("******")

urunEkle("iphone 11 pro", 8000)
urunEkle("iphone 7s", 5000)
urunleriGetir()

urunGuncelle(6, "iphone 8s", 6000)
print('******')
urunleriGetir()