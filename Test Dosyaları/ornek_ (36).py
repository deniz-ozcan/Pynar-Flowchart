
n = int(input("Enter the limit Girin: "))  

if n <= 0:
    print("sıfırdan büyük sayılar giriniz")
else:
    teksayi = [i for i in range(1, n + 1, 2)]
    ciftsayi = [i for i in range(0, n + 1,2)]

print("tek sayılar: ", teksayi)
print("Çift sayılar: ", ciftsayi)