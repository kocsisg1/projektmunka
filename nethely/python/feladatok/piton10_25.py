print("1.feladat: Szökőév")
szev=int (input("Kérem az év számot: "))
if(szev%4==0 and szev%400==0 or szev%100!=0):
    print("Ez egy szökőév")
else:
    print("Ez nem egy szökőév")