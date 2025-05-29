""" 04_agazati_cucc
█▄ ▄█ ▄▀▄ █▀▀ █▀▀ █▄▀ ▄▀▄ " ▄▀▄ ▀█▀ "
█ ▀ █ █▀█ █▄▄ ▄██ █ █ █▀█   █▀█ ▄█▄ 

Készíts egy "mesterséges intelligenciát", ami megtanít egy macskát viselkedni! 
Van egy fájl, amely minden sorában egy-egy *macskás viselkedési javaslatot* tartalmaz. 
A felhasználó megmondja, mit szabad és mit nem - a script eldönti, hogy 
a macska jó macska-e vagy anarchista démon.
"""
"""
a, Olvasd be a 04_viselkedés.txt-t, ami soronként tartalmaz macska viselkedéseket, táröld ezeket egy listába és írd ki őket egymás alá!
"""
file = open("Sultions\\04_viselkedés.txt","r",encoding="UTF-8")
viselkedesek = []
for e in file.readlines():
  viselkedesek.append(e.strip()) # .strip() -> enterek kivétele

for e in viselkedesek: # egymás alá
  print(e)

"""
b, Kérd be a felhasználótól, mely viselkedések számítanak „jó” macskának. 
pl.:
Megfigyelt viselkedések: ["alszik", "kakil", "ugat"]
jó viselkedés (x -> kilépés): alszik
jó viselkedés (x -> kilépés): szaltó
Nincs ilyen viselkedés!
jó viselkedés (x -> kilépés): x
"""

good = []
bad = []

while True:
	viselkedes_input = input("jó viselkedés (x -> kilépés): ")
	if viselkedes_input in viselkedesek:
		good.append(viselkedes_input)
	elif viselkedes_input == "x":
		break
	else:
		print("Nincs ilyen viselkedés!")

for e in viselkedesek:
  if e not in good: # ha nincs a jók közt
    bad.append(e)


"""
c, Írd ki az összes jó illetve nem jó viselkedést amit a cica csinált 
(minden nem jó viselkedés rossznak számít)
pl.:
-jó viselkedés-
dorombol
alszik
-rossz viselkedés-
kakil
meghal
nyávog
"""

print("-jó viselkedés-")
for e in good:
  print(e)


print("-rossz viselkedés-")
for e in bad:
	print(e)


"""
e, Ha 10-nél több rossz viselkedése van íja ki, hogy 
"Ez a cica egy ANARCHISTA DÉMON" különben írja ki, hogy "icipicicukicica"
"""

if len(bad) > 10:
  print("Ez a cica egy ANARCHISTA DÉMON")
else:
  print("icipicicukicica")