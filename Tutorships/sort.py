adj = [
    [(2,10), (3,7), (4,5)],
    [(0,4), (3,9), (1,7)],
]

adj2 = [
    [(4,5), (3,7), (2,10)], #tuplas el 2do elemento es el peso de la arista
    [(0,4), (1,7), (3,9)],
]

sortedAdj = []

for el in adj:
    sortedAdj.append(sorted(el, key=lambda x: x[1]))

print(sortedAdj)