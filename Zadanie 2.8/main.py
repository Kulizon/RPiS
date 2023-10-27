import random   

# 4P = pi, gdzie P to prawdopodobieństwo trafienie w ćwiartkę koła w kwadracie

def calcPi(N):
    counter = 0
    for i in range(N):
        x = random.random()
        y = random.random()

        if ((x*x + y*y) < 1): # sprawdzenie czy punkt znajduje się w kole o promieniu 1
            counter += 1

    P = counter / N
    pi = 4 * P
    print("Dla N = " + str(N) + " liczba π wynosi: " + str(pi))

calcPi(10)
calcPi(100)
calcPi(100)
calcPi(100000)
