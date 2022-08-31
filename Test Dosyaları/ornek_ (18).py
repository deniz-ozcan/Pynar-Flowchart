
def factorial(n):
    fact = 1
    while n >= 1:
        fact = fact * n
        n = n - 1

    return fact


def permutation(n, r):
    return factorial(n) / factorial(n - r)


def combination(n, r):
    return permutation(n, r) / factorial(r)


def main():
    print("choose between operator 1,2,3")
    print("1) Faktöriyel")
    print("2) Permütasyon")
    print("3) Kombinasyon")
    print("4) Çıkış")
    operation = input("\n")
    while(int(operation)>0):
        if operation == "1":
            print("Faktöriyel\n")
            while True:
                try:
                    n = int(input("\n Hangi sayının: "))
                    print("Faktöriyel {} = {}".format(n, factorial(n)))
                    break
                except ValueError:
                    print("Yanlış Değer")
                    continue

        elif operation == "2":
            print("Permütasyon\n")
            while True:
                try:
                    n = int(input("\nHangi sayının: "))
                    r = int(input("\nHangi sayıya: "))
                    print("Permütasyon {}P{} = {}".format(n, r, permutation(n, r)))
                    break
                except ValueError:
                    print("Yanlış Değer")
                    continue

        elif operation == "3":
            print("Kombinasyon\n")
            while True:
                try:
                    n = int(input("\nHangi sayının: "))
                    r = int(input("\nHangi sayıya: "))
                    print("Combination of {}C{} = {}".format(n, r, combination(n, r)))
                    break
                except ValueError:
                    print("Yanlış Değer")
                    continue
        elif operation == "4":
            print("Program Sonlandırıldı")
            break
        else:
            print("Yanlış Seçim yeniden deneyiniz.")
            continue
if __name__ == "__main__":
    main()
