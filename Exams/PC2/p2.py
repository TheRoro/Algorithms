import math
def solve():
    q, k = [int(x) for x in input().split()]

    tot_km = q*k

    Xi, Yi, Ri = [int(x) for x in input().split()]

    Xj, Yj, Rj = [int(x) for x in input().split()]

    n = int(input())

    others = []

    for _ in range(n):
        li = [int(x) for x in input().split()]
        others.append(li)


    if(len(others) == 0):
        #solo 2 escondites: inicio y fin
        p1 = []
        p1.append(Xi)
        p1.append(Yi)
        p2 = []
        p2.append(Xj)
        p2.append(Yj)
        distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
        actualDist = distance - Ri - Rj
        if(actualDist > tot_km):
            print("Gonzalo y Marcelo tuvieron que rendir sus finales como valientes")
        else:
            print("Gonzalo y Marcelo escaparon")
    else:
        #varios escondites
        last = []
        last.append(Xj)
        last.append(Yj)
        last.append(Rj)
        others.append(last)
        p1 = []
        p1.append(Xi)
        p1.append(Yi)
        dist1 = Ri
        i = 0
        valid = True
        while i < len(others) and valid == True: #len(others) = cantidad de otros escondites
            p2 = []
            p2.append(others[i][0])
            p2.append(others[i][1])
            distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
            actualDist = distance - dist1 - others[i][2]
            if(actualDist > tot_km):
                valid = False
            p1 = []
            p1.append(others[i][0])
            p1.append(others[i][1])
            dist1 = others[i][2]
            i+=1
        if valid == True:
            print("Gonzalo y Marcelo escaparon")
        else:
            print("Gonzalo y Marcelo tuvieron que rendir sus finales como valientes")

test_cases = int(input())

for _ in range(test_cases):
    solve()