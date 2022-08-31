ogrenciler={
    100:{
        "ad":"ali",
        "soyad":"veli",
        "yas":"21",
        "notlartuple":(10,15,90),# değiştirilemez
        "notlarlist":[25,35,90]# changable
    },
    101:{
        "ad":"selin",
        "soyad":"melin",
        "yas":"19"
    }         
}
print(ogrenciler)
print(ogrenciler[100])
print(ogrenciler[101]["ad"])
print(ogrenciler[101]["soyad"])
print((ogrenciler[100]["notlarlist"][0]+ogrenciler[100]["notlarlist"][1]+ogrenciler[100]["notlarlist"][2])/3)

urunler={
    '123': {'ad': 'araba', 'fiyat': '50000'
            }, 
    '120': {'ad': 'ev', 'fiyat': '90000'
            }, 
    '121': {'ad': 'telefon', 'fiyat': '9000'}
    }
id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")
    
urunler[id]={

        "ad":ad,
        "fiyat":fiyat,
            
}
id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")
urunler[id]={

        "ad":ad,
        "fiyat":fiyat,
            
}
id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")
urunler[id]={

        "ad":ad,
        "fiyat":fiyat,
            
}

id = input("aramak istediğiniz urun id: ")
urun = urunler [id]
print(urun)
print(f'id: {id} ürün adı: {urun["ad"]} ürün fiyatı: {urun["fiyat"]} ')