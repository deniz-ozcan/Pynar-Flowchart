def Kaybolan_sayılar(num_list):
    return sum(range(num_list[0], num_list[-1] + 1)) - sum(num_list)


print(Kaybolan_sayılar([1, 2, 3, 4, 6, 7, 8]))

print(Kaybolan_sayılar([10, 11, 12, 14, 15, 16, 17]))
