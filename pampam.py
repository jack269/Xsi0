control = True

mat = [[" ", " ", " "],
     [" ", " ", " "],
     [" ", " " , " "]]

k="x"
aux=0
for i in range(9):

    print("    0    1    2  ")
    z = 0
    for i in mat:
        print(z, i)
        z = z + 1


    if(k=="x"):
        print("Randul jucatorului 1")
    else :
        print("Randul jucatorului 2")

    control=False
    while(control==False):
        y = int(input("Alege coordonate x: "))
        x=int(input("Alege coordonata y: "))

        #Am incurcat variabilele x si y

        if(x>2):
            print("Coordonatele nu sunt bune")
        elif (y>2):
            print("Coordonatele nu sunt bune")
        elif (y<0):
            print("Coordonatele nu sunt bune")
        elif (x<0):
            print("Coordonatele nu sunt bune")
        elif (mat[x][y] == " "):
            mat[x][y] = k
            control = True
        else:
            print("Pozitia este ocupata")

    if(mat[0][0]==mat[0][1]==mat[0][2]==k):
        aux=k
        break
    elif (mat[1][0] == mat[1][1] == mat[1][2] == k):
        aux = k
        break
    elif (mat[2][0] == mat[2][1] == mat[2][2] == k):
        aux = k
        break
    elif (mat[0][0] == mat[1][0] == mat[2][0] == k):
        aux = k
        break
    elif (mat[0][1] == mat[1][1] == mat[2][1] == k):
        aux = k
        break
    elif (mat[0][0] == mat[1][0] == mat[2][0] == k):
        aux = k
        break
    elif (mat[0][0] == mat[1][1] == mat[2][2] == k):
        aux = k
        break
    elif (mat[0][2] == mat[1][1] == mat[2][0] == k):
        aux = k
        break

    if(k=="x"):
        k="y"
    else:
        k="x"


if(aux==0):
    print("Remiza")
else:
    if(aux=="x"):
        print("Jucatorul 1 a castigat")
    else:
        print("Jucatorul 2 a castigat")

