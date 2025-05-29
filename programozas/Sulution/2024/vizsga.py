import vizsga_fv

# 1. feladat
print("\n1. feladat:")

# 1/a feladat
terem1 = [4, 4, 0, 0, 5, 6, 6, 5, 0, 0, 0, 4]

# 1/b feladat
i = 0
while i < len(terem1):
    print(f"{i + 1}. szék: ", end="")
    if terem1[i] > 0:
        print("foglalt")
    else:
        print("üres")
    i += 1

# 1/c feladat
db = 0
for e in terem1:
    if e == 0:
        db += 1
print(f"Az 1-es teremben lévő üres helyek száma: {db} db")

# 2. feladat
print("\n2. feladat:")

# 2/a feladat
while True:
    alapár = int(input("Add meg az alapárat [1000...5000]: "))
    if alapár >= 1000 and alapár <= 5000:
        break
    print("Hibás adatbevitel! Próbáld újra...")

# 2/b feladat
i = 0
összeg = 0
while i < len(terem1):
    összeg += terem1[i] * alapár
    i += 1
print(f"Az 1-es terem bevétele: {összeg} Ft")

# 3. feladat
print("\n3. feladat:")

# 2/a feladat
terem2 = vizsga_fv.fájlbólBeolvasás("fogl2.txt")

# 2/b feladat
print(f"Legtöbb foglalás: {vizsga_fv.kedvenc(terem2)}. szék")

print()