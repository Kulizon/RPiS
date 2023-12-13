import numpy as np
import matplotlib.pyplot as plt
import random
import math

def trapezoidal_pdf(x):
    a, b, c, d = -1, 0, 2, 3
    height = 1/3
    
    if a <= x < b:
        return height / (b - a) * (x - a)
    elif b <= x < c:
        return height
    elif c <= x <= d:
        return height / (d - c) * (d - x)
    else:
        return 0

def generate_trapezoidal_random_numbers(n):
    """
    odwróć tutaj dystrubantę, tak, jak na wykładzie, tzn. oblicz ja najpierw i tu wrzuc recepturke
    """
    # obliczona zostala na wykładzie
    random_numbers = []
    for _ in range(n):
        x = random.uniform(0, 1)

        if x <= 1/6:
            y = math.sqrt(6 * x) - 1
            random_numbers.append(y)
        elif x > 1/6 and x <= 5/6:
            y = 3 * x - 1/2
            random_numbers.append(y)
        else:
            y = 3 - math.sqrt(6 - 6*x)
            random_numbers.append(y)

    return random_numbers

def main(samples):
    #np.random.seed(42)  # Ustawienie seed dla powtarzalności wyników
    num_samples = samples
    random_numbers = generate_trapezoidal_random_numbers(num_samples)

    plt.hist(random_numbers, bins=50, density=True, alpha=0.5, label='Eksperymentalna FGP')

    x = np.linspace(-1, 3, 1000)
    y = [trapezoidal_pdf(xi) for xi in x]
    plt.plot(x, y, 'r', label='Teoretyczna FGP')

    plt.title('Porównanie eksperymentalnej i teoretycznej FGP')
    plt.xlabel('Wartość')
    plt.ylabel('Gęstość prawdopodobieństwa')
    plt.legend()
    plt.show()

main(10**3)
main(10**5)
