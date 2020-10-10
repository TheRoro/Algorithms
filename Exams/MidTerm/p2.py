from itertools import product
def solve():

    #change nice_output to True in order to get a more clear output
    nice_output = True

    def add_value(listy):
        cont=0
        for i in listy: cont+=i
        return cont

    def getmaxConsecutive(nE, st):
        cont=set()

        for i in range(nE):
            prod=product(st, repeat=i+1)
            for j in prod:
                cont.add(add_value(j))

        cont=list(cont)

        for i in range(len(cont)-1):
            if cont[i]+1==cont[i+1]:
                continue
            else:
                return cont[i]

        return cont[-1]

    nE, nD=[int(r) for r in input().split()]
    values=[1]
    maxi=1

    for i in range(nD-1):
        possible=maxi
        maxi=1
        find = True

        while find:

            possible+=1
            possible_list=list(values)
            possible_list.append(possible)
            fm=getmaxConsecutive(nE, possible_list)

            if fm>maxi:
                maxi=fm
            elif fm<maxi:
                values.append(possible-1)
                find = False

    ans = getmaxConsecutive(nE, values)

    if(nice_output):
        print("Imprima estampillas de", end=" ")
        for e in values:
            print("S/.", e, end=" ")
        print(", le permite tener", ans, "combinaciones consecutivas")
    else:
        print(ans)
        print(values)
    
solve()
