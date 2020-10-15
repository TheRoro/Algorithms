n = 6

memo = [None]*(n+1)

def stairs(n):
    if n < 0:
        print("Noup")
    if n == 0 or n == 1:
        return n
    else:
        return stairs(n-1)+stairs(n+2)
    
stairs(10)