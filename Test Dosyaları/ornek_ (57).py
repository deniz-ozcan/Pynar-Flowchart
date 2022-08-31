


def hesapla(kisa, uzun):
    alan = kisa * uzun
    cevre = 2 * (kisa + uzun)

    return f"alan: {alan} çevre: {cevre}"


print(hesapla(5, 7))


def tambolen():
    x = int(input("sayi: "))
    i = 0
    while i < x:
        i += 1
        if(x % i == 0):
            print(f"1. tam bolen {i}")


tambolen()