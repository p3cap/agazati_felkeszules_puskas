def fájlbólBeolvasás(fájlnév):
    f = open(fájlnév, "r", encoding="UTF-8")
    mátrix = []
    for sor in f:
        mátrix.append(sor.replace("\n", "").strip().split())
    f.close()

    i = 0
    while i < len(mátrix):
        j = 0
        while j < len(mátrix[i]):
            mátrix[i][j] = int(mátrix[i][j])
            j += 1
        i += 1
    
    return mátrix

def foglalásOszlop(lst, oszlop):
    i = 0
    db = 0
    while i < len(lst):
        if lst[i][oszlop] > 0:
            db += 1
        i += 1
    return db

def kedvenc(lst):
    maxÉrték = foglalásOszlop(lst, 0)
    maxHely = 0

    i = 0
    while i < len(lst[0]):
        foglalás = foglalásOszlop(lst, i)
        print(f"{i + 1}. szék: {foglalás} foglalás")
        if foglalás > maxÉrték:
            maxÉrték = foglalás
            maxHely = i
        i += 1

    return maxHely + 1