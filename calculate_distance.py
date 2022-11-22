from levenshtein import levenshteinDistanceMatrix

def calcDictDistance(word, numWords, search_type):
    file = open('kosa_kata.txt', 'r')
    lines = file.readlines()
    file.close()

    dictWordDist = []
    wordIdx = 0
    perbedaan = []

    for line in lines:
        value = line.split(' - ')
        if len(value) != 3:
            continue
        if search_type == 'aceh_indonesia':
            wordDistance = levenshteinDistanceMatrix(word, value[0].strip())
            perbedaan.append(wordDistance)
        elif search_type == 'indonesia_aceh':
            wordDistance = levenshteinDistanceMatrix(word, value[1].strip())
            perbedaan.append(wordDistance)

        if wordDistance >= 10:
            wordDistance = 9
        
        if search_type == 'aceh_indonesia':
            dictWordDist.append(str(int(wordDistance)) + "-" + value[0].strip())
            perbedaan.append(wordDistance)

        elif search_type == 'indonesia_aceh':
            dictWordDist.append(str(int(wordDistance)) + "-" + value[1].strip())
            perbedaan.append(wordDistance)
        
        wordIdx += 1


    closestWords = []
    wordDetails = []
    currWordDist = 0
    dictWordDist.sort()
    for i in range(numWords):
        currWordDist = dictWordDist[i]
        wordDetails = currWordDist.split("-")
        print('hasil distance: ', wordDetails[0] ,"-", wordDetails[1])
        closestWords.append(wordDetails[1])

    perbedaan.sort()
    return [closestWords]
