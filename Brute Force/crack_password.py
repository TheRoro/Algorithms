import time 
import random
import itertools as it
import matplotlib.pyplot as plt 

A = ['x', 'y', 'z']
m = 5
password = ''.join([random.choice(A) for i in range(m)])
print("The secret password is:", password)

def crackPassword(A, m):
    for attemp in it.product(A, repeat=m):
        attemp=''.join(attemp)
        if attemp==password:
            print('The password is:', attemp)
            return

crackPassword(A, m)