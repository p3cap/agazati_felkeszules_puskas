""" 03_agazati_cucc
█ █ ▀█▀ ▀██ █▀▀ █▀▀ ▄▀▄ 
▀▄▀ ▄█▄ ██▄ ▄██ █▄█ █▀█ 

Egy fájlban diákok nevei és az ő vizsgaeredményeik találhatóak. 
A feladat, hogy elemezd a fájlt és számold ki az átlagos vizsgaeredményeket.
"""
"""
a, Olvasd be a diákok nevét és vizsgaeredményeit tartalmazó fájlt (03_diakok.txt).
"""
file = open("Sulutions\\03_diakok.txt","r",encoding="UTF-8")
diakok = []
for sor in file.readlines():
	diakok.append(sor.strip().split())

"""
b, Számold ki a diákok átlagos vizsgaeredményeit, az átlag számítás legyen def!
"""
def avrg(diak):
	jegy_num = 0
	summ = 0
	for i in range(len(diak)):
		if i != 0:
			jegy_num += 1
			summ += int(diak[i])
		
	return summ / jegy_num

for diak in diakok:
  print(f"{diak[0]} átlaga: {avrg(diak)}")

"""
c, Írd ki a legjobb és legrosszabb eredményt elért diákokat.
"""
legjobb_index = 0
legrosszabb_index = 0

for i in range(len(diakok)):
	if avrg(diakok[i]) > avrg(diakok[legjobb_index]):
		legjobb_index = i
	if avrg(diakok[i]) < avrg(diakok[legrosszabb_index]):
		legrosszabb_index = i

print(f"Legjobb diák: {diakok[legjobb_index][0]}")
print(f"Legrosszabb diák: {diakok[legrosszabb_index][0]}")

"""
d, Írd ki az össz átlagot.
"""

ossz_atlag = 0
for diak in diakok:
  ossz_atlag += avrg(diak) / len(diakok)

print(f"össz átlag: {ossz_atlag}")
