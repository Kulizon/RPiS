"""
jednorodny na przedziale [0,2]
1/(b-a) = 1/2

Y -> X^2
F_y(y) = 1/2 * sqrt(y)

Y -> X^3
F_y(y) = 1/2 * (y)**(1/3)

Y -> X^n
F_y(y) = 1/2 * (y)**(1/n)

a potem liczymy pochodna dF_y(y)/dy
i ta pochodna to nasza funkcja gestosci prawdopodobienstwa

chyba ^
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math

def Fy(y, n):
    return 1/2 * (y)**(1/n)

# na wykładzie 5 jest to wszystko
# dFy/dy
def fy(y, n):
    return 1/2 * 1/(n * (y**(n-1))**(1/n))


def main(n):
    k = 1000
    random_numbers = np.random.uniform(0, 2, k)
    
    plotVals = [[], []]
    for y in range(1, 2000):
        plotVals[0].append(y)
        plotVals[1].append(fy(y, n))
    
    plt.plot(plotVals[0], plotVals[1])


    plt.title('title')
    plt.xlabel('a')
    plt.ylabel('b')
    plt.legend()
    plt.show()

main(2)

