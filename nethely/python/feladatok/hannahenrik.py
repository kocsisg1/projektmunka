def kosar(gyerek1, gyerek2):
    if gyerek1=="Igen" and gyerek2=="Igen":
        ketto=print("Mind ketten jönnek kosarazni ")
        return ketto
    elif gyerek1=="Igen" and gyerek2=="Nem":
        egy=print("Csak az egyikük jön kosarazni ")
        return egy
    elif gyerek1=="Nem" and gyerek2=="Igen":
        egy=print("Csak az egyikük jön kosarazni ")
        return egy
    elif gyerek1=="Nem" and gyerek2=="Nem":
        nulla=print("Egyikük sem jön kosarazni ")
        return nulla
    
gyerek1=input("Jön Henrik ma kosarazni? ")
gyerek2=input("Jön Hanna ma kosarazni? ")

print(kosar(gyerek1, gyerek2))