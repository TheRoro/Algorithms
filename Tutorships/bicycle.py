n = 24 #we can lend the bicycle for 12 hours a day

friends = 9 #I have 9 friends that I could lend my bicycle to
#This 9 friends want the bike in a determined interval
#e.g: Chamo             wants the bike from 02 to 03
#     Villegas          wants the bike from 02 to 04
#     Canaval           wants the bike from 01 to 07
#     Medina            wants the bike from 08 to 09
#     Marselo           wants the bike from 06 to 10
#     Juanka            wants the bike from 09 to 11
#     Piti              wants the bike from 08 to 13
#     CarlosVives       wants the bike from 10 to 15
#     El Bisho          wants the bike from 12 to 20

myFriends = ["Chamo", "Villegas", "Canaval", "Medina", "Marselo", "Juanka", "Piti", "Carlos Vives", "El Bisho"]

inicio = [2,2,1,8,6, 9, 8, 10,12]
final  = [3,4,7,9,10,11,13,15,20]

solucion = []

def prestar_bicicleta():
    solucion.append(0)
    puntero = final[0]
    for i in range(1,friends):
        if puntero <= inicio[i]:
            solucion.append(i)
            puntero = final[i]
    for el in solucion:
        print(el, "->",myFriends[el])


#prestar_bicicleta()



#Unordered
inicio    = [2,          1,          8,         6,        2,        9,      10,              12,        8]
final     = [4,          7,          9,         10,       3,        11,     15,              20,        13]
myFriends = ["Villegas", "Canaval", "Medina", "marselo", "Chamo", "Juanka", "Carlos Vives", "El Bisho", "Piti"]
solucion = []


inicio = [x for y, x in sorted(zip(final, inicio))]
myFriends = [x for y, x in sorted(zip(final, myFriends))]
final.sort()

print("inicio:", inicio)
print("final:", final)
print("My friends:", myFriends)

prestar_bicicleta()


