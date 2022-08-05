from turtle import distance
import numpy

def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    a, b, c = 0, 0, 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                print('nilai sama: ', token1[t1-1])
                print('nilai distances[t1][t2]: ', distances[t1][t2])
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
                print('nilai distances[t1][t2] Updated: ', distances[t1][t2])

            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

        
    printDistances(distances, len(token1), len(token2))
    return int(distances[len(token1)][len(token2)])

def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()


distances = levenshteinDistanceDP("kelm", "hello")
print(distances)