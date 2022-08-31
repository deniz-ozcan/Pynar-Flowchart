def turkcekarakter(A):
    turkishcharacters = "ÇçĞğİıÖöŞşÜü"
    for i in A:
        if i in turkishcharacters:
            raise ValueError(
                f"Şifreniz {A} olamaz {i} türkçe karakterini içeriyors.")

    print(f"\nŞifreniz: {A}\n")

par = input("Şifre gir: ")
try:
    turkcekarakter(par)
except ValueError as ex:
    print(ex)