import math

def kerulet(a,b):
    ker=(a+b)*2
    return ker

def terulet(a,b):
    ter=a*b
    return ter

def atlo(a,b):
    at=math.sqrt((a*a)+(b*b))
    return at

a=float(input("Kérem az egyik oldalt! "))
b=float(input("Kérem a másik oldalt! "))

print("A kerület: ",kerulet(a,b))
print("A terület: ",terulet(a,b))
print("Az átlói: ",atlo(a,b))