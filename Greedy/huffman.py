def countFrequencies(text):
    mydic = {}
    for el in text:
        if el in mydic:
            mydic[el]+= 1
        else:
            mydic[el] = 1
    return mydic

def sortFrequencies(mydic):
    subtrees = []
    for el in sorted(mydic, key=mydic.get):
        subtrees.append((el, mydic[el]))
    return subtrees

class SubArbol:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def generateSubTrees(subtrees):
    while len(subtrees) != 1:
        left = subtrees.pop(0)
        right = subtrees.pop(0)
        subtree = SubArbol(left[0], right[0])
        subtrees.append((subtree, left[1] + right[1]))
        subtrees = sorted(subtrees, key=lambda x: x[1])
    return subtrees

def encode(node, left=True, string=''):
    if type(node) is str: #Si el nodo es una hoja
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

def printFrequencyTable(text, mydic, code):
    print("Char", "Freq", "String", "Size", sep="\t")
    total_size = 0
    total_char = len(mydic)
    total_freq = 0
    for el in mydic:
        s = code[el]
        size = len(s)*mydic[el]
        fre = mydic[el]
        print(el, fre, s, size, sep="\t")
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

#text = "Este es mi texto AAAAAAAAAAAAA"
text = "BCAADDDCCACACAC"
mydic = {}
subtrees = []
code = {}

#Algorithm

mydic = countFrequencies(text)
subtrees = sortFrequencies(mydic)

subtrees = generateSubTrees(subtrees)
code = encode(subtrees[0][0])

printFrequencyTable(text, mydic, code)

#PreOrder(subtrees[0][0])
searchInTree(subtrees[0][0], "A")