def kezdo(szo):
    if szo.startswith("a"):
        return True
    else:
        return False
szo=None
while szo!="":
    szo=input("Vigyél be egy szót!: ")
    if kezdo(szo)==True:
        print("A szó a betűs")
    else:
        print("A szó nem a betűs")
        