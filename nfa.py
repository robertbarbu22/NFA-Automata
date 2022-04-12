f = open("nfa.in", "r")
g= open("nfa.out", "w")
stari_finale=[]
noduri= int()
tranzitii=[]
cuvinte=[]
continuare=[]
linia1=f.readline()
noduri=linia1[0]
nr_tranzitii=linia1[2]
nr_tranzitii=int(nr_tranzitii)
for i in range(nr_tranzitii):
    linie=f.readline()
    tranzitii.append([linie[0],linie[2],linie[4]])   #punem tranzitiile intr-o lista
linie=f.readline()
stare_initiala=linie[0]  #memoram starea initiala
linie=f.readline()
nr_stari_finale=int(linie[0])
for i in range(2,nr_stari_finale*2+1, 2):
    stari_finale.append(linie[i])   #punem starile finale intr-o lista
linie=f.readline()
nr_cuvinte=int(linie[0])
for i in range(nr_cuvinte):
    linie=f.readline()
    linie=linie.split()
    cuvinte.append(linie)  #punem cuvintele intr-o lista
for cuvant in cuvinte:
    drum=[]
    cuvant=cuvant[0]
    prima_litera=cuvant[0]
    ultima_litera=cuvant[len(cuvant)-1]
    ok=0
    for i in range(nr_tranzitii):
        if prima_litera == tranzitii[i][2] and stare_initiala==tranzitii[i][0]: #verificam daca cuvantul incepe cu o litera care porneste din starea initiala
            for j in range(nr_tranzitii):
                if ultima_litera == tranzitii[j][2]:  # verificam daca ultima litera se afla intr-o stare finala
                    for p in range(nr_stari_finale):
                        if tranzitii[j][1]==stari_finale[p]:
                            ok=1
    if(ok==0):
        print("NU")
    else:  #cuvantul e eligibil ca stare initiala si finala si verificam daca exista un drum
        drum.append(stare_initiala)
        ord_litera=1
        nod_anterior=stare_initiala
        ok=1
        ct=0
        while ok==1:  #verific daca nodul pentru litera la care sunt acum are legatura cu nodul anterior si daca pentru litera urmatoare pot gasi o continuare a nodului acesta
            for i in range(nr_tranzitii):
                if tranzitii[i][2]==cuvant[ord_litera]:
                    for j in range(nr_tranzitii):
                        if tranzitii[j][0]== nod_anterior and tranzitii[j][1]== tranzitii[i][0] and tranzitii[j][2]==cuvant[ord_litera-1]:
                            for r in range(nr_tranzitii):
                                if tranzitii[r][0]==tranzitii[i][1] and tranzitii[r][2]==cuvant[ord_litera+1]:
                                    if ord_litera==len(cuvant)-2:
                                         drum.append(tranzitii[i][0])
                                         drum.append(tranzitii[r][0])
                                         drum.append(tranzitii[r][1])
                                    else:
                                        drum.append(tranzitii[i][0])
                                        p=tranzitii[i][0]
                                        ord_litera += 1
                                        nod_anterior=p

                if len(drum)==len(cuvant)+1:
                    break
            if ord_litera==len(cuvant)-2:
                ok=0
            if ord_litera!=len(cuvant)-2: #daca nu s-au gasit drumuri pentru toate literele cuvantul e gresit
                ok=0
        if(ok==0 and len(drum)<len(cuvant)+1):
            print("NU")
        else:
            print("DA")
            print("Traseu:", *drum)














