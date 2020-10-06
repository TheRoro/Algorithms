#bubble sort

a = [0,2,3,4,5,5,4,3,2,0,9]

n = len(a)

for i in range(n):
    for j in range(i+1, n):
        if(a[i] > a[j]):
            a[i], a[j] = a[j], a[i]


print(a)

#backtracking O(n*m)

strmaze = """
000000000000000000000000000000
011111111111111111111101111111
010000000000001000000001000000
010111111100001000000001000000
010100000000001000000001000000
010111111111111111111111000000
010000000000000000000000000000
011111111111111111111111111110
000000000000000000000100001010
000000000000000000000111101010
000000000000000000000000001010
000000000011111111111111111010
000000000000000000000000000010
111111111111111111111111111110
000000000000000000000000000000
"""


def backtracking_maze(x, y):
    
    if(mat[x][y] == 1):
        return False
    else:
        if(mat[x+1][y] == 0): #derecha
            backtracking_maze(x+1, y)
        if(mat[x][y+1] == 0): #arriba
            backtracking_maze(x, y+1)
        if(mat[x][y-1] == 0):
            backtracking_maze(x-1, y)
        if(mat[x-1][y] == 0):
            backtracking_maze(x-1, y)


def nqueensbt(board, row):
    n = len(board)
    if row < n:
        for col in range(n): #O(n2)
            if valid(board, row, col):
                board[row] = col
                if nqueensbt(board, row + 1):
                    return True
    else:
        draw(board)
        return True


def valid(board, row, col):
    n = len(board)
    for i in range(row):
        if board[i] == col:
            return False
        d = row - i
        if board[i] + d == col or board[i] - d == col:
            return False
    return True


#Problema chevere
#Fuerza Bruta

#Encontrar la cantidad de veces que aparece un substring
#Dado un string de tamaño mayor

#Ejemplo:

#hola que tal
#ol
#1

#sasasasasas
#sa
#5




#Problema Chevere 2
#Divide Y venceras
#Encontrar la cantidad de palabras que tiene un texto

#Ejemplo:

#texto = "MI nombre es Vilaron Martinez"
#rpta: 5 palabras

stri = "babababababaababa"
substr = "ba"
print("Python's solution:", stri.count(substr))

#Divide and conquer:

#O(nlogn)

#Hola que tal como estas

#O(n)

cont = 0

s = "hola como estas"

for i in s:
    if i == " ":
        cont+=1

print(cont+1)
