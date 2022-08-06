from levenshtein import levenshteinDistanceMatrix

def calcDictDistance(word, numWords, search_type=None):
    file = open('kosa_kata.txt', 'r')
    lines = file.readlines()
    file.close()

    dictWordDist = []
    wordIdx = 0

    for line in lines:
        value = line.split(' - ')
        if len(value) != 3:
            continue
        if search_type == 'aceh-indonesia':
            # print('Nilai Line: ', value[0])
            wordDistance = levenshteinDistanceMatrix(word, value[0].strip())
        elif search_type == 'indonesia-aceh':
            wordDistance = levenshteinDistanceMatrix(word, value[1].strip())
            # print('Nilai Line: ', value[1])

        if wordDistance >= 10:
            wordDistance = 9
        
        if search_type == 'aceh-indonesia':
            dictWordDist.append(str(int(wordDistance)) + "-" + value[0].strip())
        elif search_type == 'indonesia-aceh':
            dictWordDist.append(str(int(wordDistance)) + "-" + value[1].strip())


        
        wordIdx += 1


    closestWords = []
    wordDetails = []
    currWordDist = 0
    dictWordDist.sort()
    # print(dictWordDist)
    for i in range(numWords):
        currWordDist = dictWordDist[i]
        wordDetails = currWordDist.split("-")
        closestWords.append(wordDetails[1])
    return closestWords

search_type = 'indonesia-aceh'
# search_type = 'aceh-indonesia'

for i in calcDictDistance('kamps', 2, search_type):
    print(i)
# print(type(calcDictDistance('text', 2)))