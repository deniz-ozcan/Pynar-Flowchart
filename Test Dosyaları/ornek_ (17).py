
a = ["Hello", 35, "b", 45.5, "world", 60]
i = f = s = 0
for j in a:
    if isinstance(j, int):
        i = i + 1
    elif isinstance(j, float):
        f = f + 1
    else:
        s = s + 1
print(f"Tam sayılar: {i}")
print(f"Rasyonel sayılar: {f}")
print(f"String: {s}")
