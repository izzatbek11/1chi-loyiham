def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

# Misol uchun
print(kopaytma(2, 3, 4))
print(kopaytma(1, 5, 7, 2))
