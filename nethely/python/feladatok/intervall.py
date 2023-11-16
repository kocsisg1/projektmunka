szam=0
osszeg=0
intervall=[]
while szam>=-5 and szam<=5:
    szam=int(input("Adj meg egy számot(-5 5): "))
    if szam<-5 or szam>5:
        break
    intervall.append(szam)
    osszeg=osszeg+szam
print(osszeg)
print(intervall)
    

