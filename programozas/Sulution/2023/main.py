from random import randint
##
print("1. feladat")

elemek = []
elemek = [randint(0, 9) for _ in range(10)]
print(f"A lista tartalma: {elemek}")

smaller5 = 0
larger5 = 0
for e in elemek:
  if e > 5:
    larger5 += e
  elif e < 5:
    smaller5 += e
print(f"5-nél kisebb elemek összege: {smaller5}\n5-nél nagyobb elemek összege: {larger5}")
##
print("2. feladat")

even_nums = 0
for e in elemek:
  if e % 2 == 0:
    even_nums += 1

largest = elemek[0]
for e in elemek:
  if e > largest: largest = e

lrgst_occur_1 = 0
lrgst_occur_2 = 0
for i in range(len(elemek)):
	if elemek[i] == largest:
		if i < len(elemek)/2:
			lrgst_occur_1 += 1
		else:
			lrgst_occur_2 += 1

print(f"A listában lévő páratlan elemek száma: {len(elemek)-even_nums}db")
print("Nem igaz az állítás!" if even_nums > 4 else "Igaz az állítás!") 
print(f"A listában lévő legnagyobb elem: {largest}")
print(f"A legnagyobb elem előfordulása a lista első felében: {lrgst_occur_1} db")
print(f"A legnagyobb elem előfordulása a lista első felében: {lrgst_occur_2} db")
print("Igaz az állítás!" if lrgst_occur_1 > lrgst_occur_2 else "Nem igaz az állítás!")
##
print("3. feladat")

def adatokBeolvasása():
	with open("eladasok.txt") as f:
		data = []
		for e in f:
			line = e.strip().split()
			line = [int(e) if e.isnumeric() else e for e in line]
			data.append(line)
		return data

months = ["Január", "Február", "Március", "Április", "Május", "Június",
          "Július", "Augusztus", "Szeptember", "Október", "November", "December"]

def haviEladás(data):
	print("Notebookok eladásai havi bontásban:")
	monthly = [0] * (len(data[0]) - 1)
	for row in data:
		for i in range(1, len(row)):
			monthly[i - 1] += row[i]
	for i in range(len(monthly)):
		print(f"{months[i]}: {monthly[i]} db")

haviEladás(adatokBeolvasása())
