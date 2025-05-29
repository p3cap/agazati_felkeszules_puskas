"""
Ágazati alapvizsga - 2022. április 12.
Programozás Python nyelven

1. feladat - 8 pont

Írj programot, amelyik megoldja a következő feladatokat!

a) A példában látható módon kérj be a felhasználótól egy listaméretet! A program csak 10 és 20 közötti értéket fogadjon el! Ha a felhasználó által megadott érték nem esik bele a megadott tartományba, akkor a program írjon ki egy hibaüzenetet és kérje be újra a listaméretet! (4 pont)

b) Hozz létre egy üres listát elemek néven, és töltsd fel ezt a listát annyi darab 1 és 5 közötti egész véletlenszámmal, amennyiket a felhasználó az a) feladatrészben megadott! (2 pont)

c) Írd ki a lista tartalmát a példában látható módon! (2 pont)

PÉLDA:

Add meg a lista méretét [10...20]: 25  
Hibás adatbevitel! Próbáld újra!  
Add meg a lista méretét [10...20]: 12  
A lista tartalma: [1, 1, 5, 2, 3, 2, 3, 2, 4, 1, 4, 5]
"""
import random

while True:
	meret = int(input("Add meg a lista méretét [10...20]:"))
	if 10 <= meret <= 20:
		break
	else:
		print("Hibás adatbevitel! Próbáld újra!")

elemek = []

for i in range(meret):
  elemek.append(random.randint(1,5))
print(f"A lista tartalma: {elemek}")

"""
2. feladat - 14 pont

Írj programot, amelyik megoldja a következő feladatokat! A feladatok megoldásához használd fel az 1. feladatban létrehozott elemek listát!
Amennyiben nem sikerült megoldanod az 1. feladatot, akkor hozd létre a programban az elemek listát és kézzel írj bele 10 darab 1 és 5 közötti egész számot!

a) A példában látható módon írd ki a listában lévő elemek összegét! (6 pont)

b) A példában látható módon írd ki, hogy melyik a listában lévő legnagyobb szám és az hányadik pozícióban szerepel a listában! A program az „első legnagyobb szám” számot adja meg! (8 pont)

PÉLDA:

A listában lévő elemek összege: 32  
A listában lévő legnagyobb szám: 5, helye: 3. pozíció
Ha szeretnéd, kiírhatom ezt fájlba is. 
"""
summ = 0
for e in elemek:
  summ += e
print(f"A listában lévő elemek összege: {summ}")

max_index = 0
for i in range(len(elemek)):
  if elemek[i] > elemek[max_index]:
    max_index = i
print(f"A listában lévő legnagyobb szám: { elemek[max_index] }, helye: { max_index+1 }. pozíció")

"""
3. feladat
A fuvarok.txt fájlban egy fuvarozással foglalkozó cég teherautóinak 2021-es futásteljesítményei láthatók havi bontásban. A fájlban az adatok szóközzel vannak elválasztva.

ABC-123 782 2138 903 4200 0 0 0 980 3905 2045 655 4495  
DEF-456 3162 4372 102 487 3279 0 2238 0 4028 2149 2677 259

A fájl egy sorában az első oszlopban a teherautó rendszáma található, utána pedig a 12 db egész szám januártól kezdve a havi futásteljesítményeket mutatja (azaz az ABC-123 rendszámú teherautó januárban 782 km-t, februárban 2138 km-t, márciusban 903 km-t stb. teljesített az utakon).

Írj programot, amelyik megoldja a következő feladatokat!

a) Írj függvényt adatokBeolvasasa néven, amely beolvassa a fájl tartalmát egy megfelelő adatszerkezetbe! Ügyelj arra, hogy a havi futásteljesítmények numerikus értékként legyenek eltárolva az általad választott adatszerkezetben! (8 pont)

b) Írj függvényt nullaKm néven, amelyik visszaadja a hívás helyére, és utána példában látható módon kiírja a képernyőre, hogy hány olyan hónap volt 2021-ben a teljes adathalmazban, amikor egy teherautó egy hónapban nulla km-t tett meg. A nullaKm függvény által visszaküldött darabszám értéket a főprogramban kell kiírni! (10 pont)

PÉLDA (a példa a program egy lehetséges futási eredményét mutatja):
Az adatbázisban 29 db 0 km havi futásteljesítményt tartalmazó hónap van.
"""
adat = []
def adatokBeolvasasa():
  f = open("fuvarok.txt","r",encoding="UTF-8")
  for e in f:
    sor = e.strip().split()
    for i in range(1,len(sor)):
      sor[i] = int(sor[i])
    adat.append(sor)
  
  f.close()

def nullaKm():
  db = 0
  for sor in adat:
    for oszlop in sor:
      if oszlop == 0:
        db += 1
  return db

adatokBeolvasasa()
print(f"Az adatbázisban {nullaKm()} db 0 km havi futásteljesítményt tartalmazó hónap van.")