import numpy as np
import matplotlib.pyplot as plt

# przedział rozkładu (a, b)
a, b = 0, 2

# generowanie 10000 losowych liczb z przedziału (a,b)
xSamples = np.random.uniform(a, b, 10000)

# obliczona analitycznie funkcja gestosci
def fy(y, n):
    return 1/2 * 1/(n * (y**(n-1))**(1/n))

# wymiary do sprawdzenia
dimensions = [2, 3, 4, 5, 20]

for n in dimensions:
    # histogram
    plt.figure(figsize=(8, 5))
    plt.hist(xSamples**n, bins=70, density=True, alpha=0.5, label='Histogram (n={})'.format(n))

    # analitycznie obliczona funkcja gestosci
    xValues = np.linspace(0, b**n, 200)
    yValues = [fy(x, n) for x in xValues]
    plt.plot(xValues, yValues, 'r', label='Analityczna (n={})'.format(n))

    plt.title('Objętość {}-wymiarych sześcianów o długości boku X'.format(n))
    plt.xlabel('Objętość')
    plt.ylabel('Gęstość prawdopodobieństwa')
    plt.legend()
    plt.show()
