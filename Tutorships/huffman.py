s = "AAAEEEIIIOOU"

mydic = {}

for el in s:
    if el not in mydic:
        mydic[el] = 1
    else:
        mydic[el]+=1

print(mydic)

q = []

for el in mydic:
    q.append((el, mydic[el]))

#print(mydic)
#print(q)

class Arbol:
    def __init__(self, left, right):
        self.left = left
        self.right = right

q = sorted(q, key=lambda x: x[1])

print(q)

while len(q) != 1:
    #combinar los subarboles, arboles o nodos
    left = q.pop(0)
    right = q.pop(0)
    arbol = Arbol(left[0], right[0])
    suma = left[1] + right[1]
    obj = (arbol, suma)
    q.append(obj)
    q = sorted(q, key=lambda x: x[1])


ans = []
def buscar(node, search, string=''):
    if type(node) is str: #es un nodo hoja y tiene valor
        if node == search:
            ans.append((node, string))
        return (node, string)
    (l, r) = buscar(node.left, search, string + '0'), buscar(node.right, search, string + '1')
    return 0

buscar(q[0][0], 'O', '')
print(ans[0][0], ans[0][1])