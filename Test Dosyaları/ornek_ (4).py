
def FizzBuzz():
    num = int(input("Enter the number here: "))
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("3e ve 5e bölünenen sayılar: ", i)
        elif i % 3 == 0:
            print("3e bölünen sayılar: ", i)
        elif i % 5 == 0:
            print("5e bölünen sayılar: ", i)
        else:
            print(i)

FizzBuzz()