""" 01_ágazatai_SOLVED
█▀█ ▄▀▄ █▀█ █ █ █▀▀ █▀▀ █▀▀ ▀█▀ █▄ █ █▀▄ █▀▀ █▀█ 
█▀▀ █▀█ █▀▀ █▄█ █▄▄ ▄██ █▀  ▄█▄ █ ▀█ █▄▀ ██▄ █▀▄ 

A mátrix egy térkép a nappalid padlójáról. 1 = papucs, 0 = üres. A cél: papucs megtalálása a
lehető legkevesebb nézéssel.

"""
"""
a,  Generálj egy 5x3 mátrixot 0-1 értékekkel.
pl:
padlo =
[	[0,0,1,0,1]
  [0,0,1,0,1]
	[0,0,1,0,1] ]
"""
import random
padlo = []

for _ in range(5): #"sorok"
  sor = []
  for _ in range(3): #"oszlopok"
    papucs = random.randrange(0,1)
    sor.append(papucs)

"""
b, Számold meg, hány papucs (1) van.
"""
papucs_db = 0
for sor in padlo: #"sorok"
  for papucs in sor: #"oszlopok"
    if papucs == 1:
      papucs_db += 1

"""
c, Keresd meg a leghosszabb papucs-sorozatot vízszintesen (egymás után).
d, Írd ki a sor indexét, ahol a legtöbb papucs egy sorban van.
"""
max_sor_hossz = 0
max_sor_index = 0

index = 0
for sor in padlo:
  hossz = 0
  for papucs in sor:
    if papucs == 1:
      hossz += 1
    else:
      hossz = 0
    
    if hossz > max_sor_hossz:
      max_sor_hossz = hossz
      max_sor_index = index
    
    index += 1

""" 
e, mentsd a mátrixot egy 01_PAPUCS.txt fájlba.
"""
file = open("Sultions\01_PAPUCS.txt","w")
for sor in padlo:
  for oszlop in sor:
    file.write(oszlop)
  file.write("\n")

file.close()