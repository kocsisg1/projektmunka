class Person:
    def __init__(self,name, point, email ):
        self.name=name
        self.point=point
        self.email=email


jatekoslista=[]
for x in range(3):
    nev=input("Kérem a nevet! ")
    pont=int(input("Kérem a pontszámát! "))
    email=input("Kérem az emailt! ")
    p=Person(nev,pont,email)
    jatekoslista.append(p)

legkisebb=jatekoslista[0]
for x in jatekoslista:
    if x.point<legkisebb.point:
        legkisebb=x
print(legkisebb.name, legkisebb.point)