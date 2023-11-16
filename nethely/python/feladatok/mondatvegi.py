def mondatveg(szo):
    if szo.endswith("."):
        kijelent="Ez egy kijelentő mondat."
        return kijelent
    elif szo.endswith("?"):
        kerdo="Ez egy kérdő mondat"
        return kerdo
    elif szo.endswith("!"):
        ffo="Ez egy felkiáltó, felszólitó vagy óhajtó mondat"
        return ffo

szo=None

while szo!="":
    szo=input("Vigyél be egy mondatot!: ")
    print(mondatveg(szo))

    