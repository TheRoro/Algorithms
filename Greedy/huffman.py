def countFrequencies(text):
    mydict = {}
    for el in text:
        if el in mydict:
            mydict[el]+= 1
        else:
            mydict[el] = 1
    return mydict

def sortFrequencies(mydict):
    subtrees = []
    for el in sorted(mydict, key=mydict.get):
        subtrees.append((el, mydict[el]))

    freq = subtrees #save the freq as auxiliary
    return subtrees, freq

class SubArbol:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def generateSubTrees(subtrees):
    while len(subtrees) != 1:
        left = subtrees[0]
        right = subtrees[1]
        subtrees = subtrees[2:]
        subtree = SubArbol(left[0], right[0])
        subtrees.append((subtree, left[1] + right[1]))
        subtrees = sorted(subtrees, key=lambda x: x[1])
    return subtrees

def encode(node, left=True, string=''):
    if type(node) is str:
        return {node: string}
    (l, r) = node.left, node.right
    d = dict()
    d.update(encode(l, True, string + '0'))
    d.update(encode(r, False, string + '1'))
    return d

def PreOrder(node, left=True, string=''):
    if type(node) is str:
        print(node, string)
        return (node, string)
    (l, r) = PreOrder(node.left, True, string + '0'), PreOrder(node.right, False, string + '1')
    return 0

def searchString(node, search, ans, left=True, string=''):
    if type(node) is str:
        if node == search:
            ans.append((node, string))
            #print("The character", node, "was found, with a string of:", string)
        return (node, string)
    (l, r) = searchString(node.left, search, ans, True, string + '0'), searchString(node.right, search, ans, False, string + '1')
    return 0

def searchInTree(subtree, char):
    ans = []
    searchString(subtree, char, ans)
    if(len(ans) == 0):
        print("Char", char, "is not in the Tree")
    else:
        print("The character", char, "was found, with a string of:", ans[0][1])

def printFrequencyTable(text, freq, code):
    print("Char", "Freq", "String", "Size", sep="\t")
    total_size = 0
    total_char = len(freq)
    total_freq = 0
    for el in freq:
        s = code[el[0]]
        size = len(s)*el[1]
        fre = el[1]
        print(el[0], fre, s, size, sep="\t")
        total_size+=size
        total_freq+=fre
    huffman_bits = total_size+total_char*8+total_freq
    non_huffman_bits = 8*len(text)
    print("Total Size:", huffman_bits)
    print("Size without compression:", non_huffman_bits)
    if huffman_bits < non_huffman_bits:
        print("You saved:", non_huffman_bits - huffman_bits, "bits.")
        print("Percentage: ", (1-huffman_bits/non_huffman_bits)*100, "%", " of memory saved", sep="")
    else:
        print("Is more convenient not to use Huffman Algorithm")
#Variables

text = "Este es mi texto AAAAAAAAAAAAA"
mydict = {}
subtrees = []
freq = []
code = {}

#Algorithm

mydict = countFrequencies(text)
subtrees, freq = sortFrequencies(mydict)

subtrees = generateSubTrees(subtrees)
code = encode(subtrees[0][0])

printFrequencyTable(text, freq, code)

#PreOrder(subtrees[0][0])
searchInTree(subtrees[0][0], "A")