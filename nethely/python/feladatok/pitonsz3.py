import math
import random
print("31.feladat")
sz1=int (input("Kérek egy számot:"))
sz2=int (input("Kérek még egy számot:"))
sz3=int (input("Kérek még egy számot:"))
print(min(sz1,sz2,sz3))

print("32.feladat")
tri1=int (input("Háromszög egyik oldala:"))
tri2=int (input("Háromszög másik oldala:"))
tri3=int (input("Háromszög harmadik oldala:"))

if(tri1 + tri2 > tri3 | tri1 + tri3 > tri1 | tri3 + tri2 > tri1):
    print("A háromszög megszerkezthető") 
else:
    print("A háromszög nem megszerkezthető")

print("34.feladat")
der1=int(input("Kérek egy oldalt:"))
der2=int(input("Kérek még egy oldalt:"))
print("Átfogó hossza",round(math.sqrt(der1*der1+der2*der2),2))

print("35.feladat")
reci1=int(1)
for x in range(1, 11):
    reci1=1/x
    print(x,".",reci1)

print("36.feladat")
hatv=int(input("Hatványt kérek:"))
kite=int(input("Kitevőt kérek:"))
print("Hatványérték=",(math.pow(hatv,kite)))

print("37.feladat")
poz=float(input("CSAK POZITÍV:"))
pozi=True
while pozi:
    if(poz<=-1):
        pozi=False
        print("Nem jó, próbáld újra")
        poz=float(input("CSAK POZITÍV:"))
    else:
        pozi=True
        break

print("38.feladat")
sza1=int(input("Első szám"))
sza2=int(input("Második szám"))
print (abs(sza1-sza2))

print("39.feladat")
sza1=int(input("Első szám"))
sza2=int(input("Második szám"))
print("Átlagja: ",(sza1+sza2)/2)

print("40.feladat")
osszeg=0
while osszeg<100:
    szam=int(input("Kérem a számot"))
    osszeg+=szam
print("Az összeg meghaladta a 100-at.")

print("41.feladat")
tizes=True
ossz=0
szam=int(input("Kérem a számot: "))
while tizes:
    if(szam<10):
        szam=int(input("Kérem a számot: "))
        ossz+=szam
    else:
        tizes=False
        print("Az szám meghaladta a 10-et.", szam )
        break

print("42.feladat")
vszam=random.randint(0, 101)
print(vszam)

print("43.feladat")
vszam=random.randint(10, 51)
print(vszam)

print("44.feladat")
vszam=random.randint(132, 148)
print(vszam)

print("45.feladat")
vszam=random.randrange(132, 149, 2)
print(vszam)

