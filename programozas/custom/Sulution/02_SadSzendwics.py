""" 02_ágazati cucc
█▀▀ ▄▀▄ █▀▄  █▀▀ ▀██ █▀▀ █▄ █ █▀▄ █ █ █ ▀█▀ █▀▀ █▀▀ 
▄██ █▀█ █▄▀  ▄██ ██▄ ██▄ █ ▀█ █▄▀ ▀▄▀▄▀ ▄█▄ █▄▄ ▄██ 

A szendvicsed egy négyzet alakú mátrix, minden falat egy szám: 0 = íztelen, 5 = csodás. 
A robot szerint ha túl sok *egymás melletti* íztelen falat van, az már „szendvics trauma”.

A cél: a felhasználó megadja, hány egymás melletti nulla számít traumának, és megkeressük az ilyen *traumatikus sorokat*.
"""

"""
a, Kérd be a felhasználótól, hogy "Hány egymás melletti íztelen(0) érték számít traumának [1-4]: ". Csak 1-4 lehet!
"""

while True:
  trauma_sorozat = int(input("Hány egymás melletti íztelen(0) érték számít traumának [1-4]: "))
  if trauma_sorozat <= 4 and trauma_sorozat >= 1:
    break
1
"""
b, Generálj egy 10x9-es mátrixot, ahol az értékek 0-5 közöttiek (egész számok, véletlenszerűen).
"""
import random

szendwics = []
for i in range(10): #sor
  sor = []
  for j in range(9): #oszlop
    sor.append(random.randint(0,5))
  
  szendwics.append(sor)

"""
c, Írd ki a teljes mátrixot szépen soronként, „sor X:” formában.
pl:
sor 0: 0, 5, 2, 0, 10, 0, 
sor 1: 0, 5, 2, 0, 10, 0, 
...
"""
for sor_index in range(len(szendwics)):
	#                 ^^olyan listát csinál amibe 0 - hosszúság-1 -ig vannak elemek
	#                 pl.: lista = ["hi","szia"]; range(len(lista)) -> [0,1]
	#                 tehát a sor_index változó olyan lesz mint a while ciklus 'i' változója
	print(f"sor {sor_index}: ",end="")
	for oszlop_elem in szendwics[sor_index]:
		print(oszlop_elem,end=", ")
  
	print()#enter

i = 0
while i < len(szendwics):
	#print(f"sor {i}: ",end="")
	j=0
	while j < len(szendwics[i]):
		#print(szendwics[i][j],end=", ")
		j+=1
	#print()#enter
	i+=1

"""
d, Keresd meg, mely sorokban van legalább annyi egymás melletti 0, amennyit a felhasználó traumaként megadott.
"""
trauma_indexek = []

index = 0
for sor in szendwics:
	egymas_mellett = 0
	for oszlop in sor:
		if oszlop == 0:
			egymas_mellett += 1
		else:
			egymas_mellett = 0 # reset
		if egymas_mellett >= trauma_sorozat:
			trauma_indexek.append(index)

	index += 1

i=0
while i < len(szendwics):
	egymas_mellett = 0
	j=0
	while j < len(szendwics[i]):
		if szendwics[i][j] == "0":
			egymas_mellett += 1
		else:
			egymas_mellett = 0 # reset
		if egymas_mellett >= 4:
			trauma_indexek.append(i)

		j+=1
	i += 1

"""
e, Írd ki a sorok sorszámát, amelyek „traumásak”. Ha nincs ilyen, írd: „Ez a szendvics... meglepően jó volt.”
Az eredményt a „02_SZENDVICS.txt” fájlba írd ki. (ha jó akkor 
"Ez a szendvics... meglepően jó volt. -értékelő") 
ha nem akkor 
"Kórházba kerültem miatta, 2csillag. -értékelő"
"""
file = open("Sultions\\02_SZENDVICS.txt","w",encoding="UTF-8")
if len(trauma_indexek) > 0:
	for i in trauma_indexek:
		print(szendwics[i])
	file.write("Kórházba kerültem miatta, 2csillag. -értékelő")
else:
	file.write("Ez a szendvics... meglepően jó volt. -értékelő")

file.close()

