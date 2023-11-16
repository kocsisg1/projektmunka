import random

def pénzfeldobás():
    gép_dobás = random.choice(["fej", "iras"])
    return gép_dobás


találatok = 0

for _ in range(3):
        tip = input("Válassz fej vagy írás: ")
        gépdobas = pénzfeldobás()

        print("A gép dobása:", gépdobas)

        if tip == gépdobas:
            print("Talált!")
            találatok += 1
        else:
            print("Nem találtad el.")

print("A három körből ", találatok, "alkalommal találtál el.")
