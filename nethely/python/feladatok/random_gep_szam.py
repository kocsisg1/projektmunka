import random

def gep():
    return random.randint(1,5)
gepszam=gep()
szam=0
while szam!=gepszam:
    print("Gondoltam egy számra 1 és 5 között")
    szam=int(input("Kérem adjon meg egy számot 1 és 5 között: "))

    if szam==gepszam:
        print("Eltaláltad!")
    elif szam<gepszam:
        print("Ennél nagyobb szám")
    elif szam>gepszam:
        print("Ennél kisebb szám")