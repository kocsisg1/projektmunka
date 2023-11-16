def siker(pont):
    if pont>=48:
        return True
    else:
        return False


nev=None
while nev!="":
    nev=input("Add meg a vizsgázó nevét! ")
    if nev=="":
        break
    pontsz=int(input("Add meg a pontszámát! "))
    if siker(pontsz):
        print(nev," vizsgája sikeres!")
    else:
        print(nev," vizsgája sikertelen!")

