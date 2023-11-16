#0-1000 számolás
for x in range(1001):
    x   

#100-800 számolás

for x in range(100, 801):
    x

#10 természetes szám

for x in range(1, 11):
    print(x)

print(" ")

#párosak
for x in range(0, 11, 2):
    print(x)

print(" ")

#/3
for x in range(0, 101, 3):
    print(x)

print(" ")

#bekeres*2
szam=int(input("Kérek egy számot: "))
print(szam*2)

print(" ")

#első 5 szam
szam1=0
for x in range(1, 6):
    szam1+=x
print(szam1)

print(" ")

#1-10ig négyzete
for x in range(1, 11):
    print(x*x)

print(" ")

#1től négyzetek 1000ig

print("1000-IG!!!!!")

i=0
while i*i<1000 & i<100:
  i+=1
  if i*i>=1000:
   print(i*i)
   break

print(" ")

#páros

for x in range(0, 101, 2):
    print(x)

print(" ")

#két négyzet

szam4=int(input("Kérek egy számot!: "))
szam5=int(input("Kérek még egy számot!: "))
print(szam4*szam4)
print(szam5*szam5)

print(" ")

#páros számok 50-10

for x in range(-50, -9, 2):
    print(x*-1)

print(" ")

aoldal=int(input("Írd le a négyzet oldalát: "))
print("Kerület: ")
print(aoldal*4)
print("Terület: ")
print(aoldal*aoldal)

print(" ")
#téglalap oldalai

roldal=int(input("Rövidebbik oldal: "))
holdal=int(input("Hosszabbik oldal: "))
print("Kerület: ") 
print(2*(roldal+holdal))
print("Terület: ")
print(roldal*holdal)

print(" ")

#első 10 páros szám összeadva

ossz=0
for x in range(2, 21, 2):
    ossz+=x
print(ossz)

print(" ")

#80-20ig páratlan

for x in range(-79, -20, 2):
    print(x*-1)

print(" ")

#atlag

atl1=int(input("Átlagolandó szám1: "))
atl2=int(input("Átlagolandó szám2: "))
atl3=int(input("Átlagolandó szám3: "))
print((atl1+atl2+atl3)/3)

print(" ")

#páratlanok 1-90ig

for x in range(1, 91, 2):
    print(x)

print(" ")

#60-15ig páratlan

for x in range(-59, -14, 2):
    print(x*-1)

print(" ")

#70-25ig páratlan

for x in range(-70, -24, 2):
    print(x*-1)

print(" ")

#pozitív egész számok

szam7=int(input("Kérek egy számot"))
for x in range(1, szam7):
    print(x)

print(" ")

#nagyobbik

szamok1=int(input("Kérek számot! "))
szamok2=int(input("Kérek még egyet! "))
if szamok1<szamok2:
    print(szamok2)
else:
    print(szamok1)


