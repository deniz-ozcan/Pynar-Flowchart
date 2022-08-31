N = int(input("Dizi Boyutunu Girin: "))
list = []
for i in range(0, N):
    temp = int(input("Sayı Girin: "))
    list.append(temp)
finalList = []
d = int(input("Diziyi Döndürmek İstediğiniz Sayıyı Girin: "))
for i in range(0, N):
    finalList.append(list[(i + d) % N])
print(finalList)