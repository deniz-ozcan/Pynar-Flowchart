def fib(term):
    if term <= 1:
        return term
    else:
        return fib(term - 1) + fib(term - 2)

for i in range(int(input("Enter the number of terms: "))):
    print(fib(i))
