"""

jegy [1...5]: 5
jegy [1...5]: 2
jegy [1...5]: 7
..helyetelen
jegy [1...5]: stop

"""
nev = input("Neve: ")
jegyek = []
while True:
  inp = input("jegy [1...5]: ")
  if inp == "stop": break
  elif 1 < int(inp) < 5:
    jegyek.append(int(inp))
  else: 
    print("..helyetelen")

f = open("03_vizsga.txt","w",encoding="UTF-8")
f.write(nev)