import numpy as np
import matplotlib.pyplot as plt
import random
import math

desiredProb = 0.41352941176

results = []
counter = 0
i = 1

cards = [i for i in range(1, 53)]

while(True):
    # liczba kart to 52, każda karta jest przyporządkowana liczbie z przedziału 1-52
    wylosowane = random.sample(cards, 3) # wybierz 3 różne karty

    # załóżmy, że karty trefla to karty z numerami większymi od 39
    if (wylosowane[0] <= 39 and wylosowane[1] <= 39 and wylosowane[2] <= 39):
        counter += 1
    
    prob = counter / i
    results.append(prob)
    i += 1
    
    if (i > 10 and abs(desiredProb - prob) < 0.0001):
        break

print("Oczekiwane prawdopobieństwo osiągnięto za " + str(i) + "-razem")
print("Prawdopodobieństwo: " + str(prob * 100) + "%")


plt.plot([j for j in range(1, i)], results)
plt.xlabel("Liczba symulacji")
plt.ylabel("Szansa na wyciągniecię trefla")
plt.title('Wykres prawdopodobieństwa wyciągnięcia trefla od liczby eksperymentów')
plt.show()