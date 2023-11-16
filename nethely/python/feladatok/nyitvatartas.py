print("Nyitvatartás")
zaras=int(16)
nyitas=int(8)
ora=int(input("Hány óra van most?: "))
if(ora>nyitas and ora<zaras):
    print("A bolt nyitva van")
    print("Ennyi időd van még zárásig: ", (16-ora))
else:
    print("A bolt zárva van")