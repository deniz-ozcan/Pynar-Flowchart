def Prime_Perfection(n):
    if(n > 0):
        total1 = 0
        for i in range(1, int(n/2)+1):
            if(n % i == 0):
                total1 += i
        if(total1 == n):
            return f"{n} is a perfect number."
        total2 = []
        for i in range(2, int(n//2)+1):
            if(n % i == 0):
                total2.append(i)
        if(len(total2) == 0 and n != 0 and n != 1):
            return f"{n} is a prime number."
    elif(n == 0):
        return "Divide by zero error encountered."
    else:
        return "Negative numbers can not be one of either a prime numbers or a perfect numbers."

x=input()
for i in range(1, 30):
    if(Prime_Perfection(i) != None):
        print(Prime_Perfection(i))

