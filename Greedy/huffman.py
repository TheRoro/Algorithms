text = "Este es mi texto"

mydict = {}
for el in text:
    if el in mydict:
        val = mydict[el]
        val+=1
        mydict[el] = val
    else:
        mydict[el] = 1

mydict = sorted(mydict.items(), key=lambda x: x[1], reverse=True)

print("Tabla de frecuencias")

for i in mydict:
    print("Letra", i, "->", mydict[i])

class Arbolito:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


