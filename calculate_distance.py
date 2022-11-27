from levenshtein import levenshteinDistanceMatrix
from app.utilities import calculate_percentage_accuracy, insert_distance_percentage

def calcDictDistance(word, numWords, search_type, csv_filename):
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
    alldata = []
    for i in range(numWords):
        currWordDist = dictWordDist[i]
        wordDetails = currWordDist.split("-")
        percentage_accuracy = calculate_percentage_accuracy(int(wordDetails[0]), len(word))
        data = [word, wordDetails[1], len(word), f'{str(int(percentage_accuracy))}%', wordDetails[0]]
        alldata.append(data)
        print(f'{word} - {wordDetails[1]} - {int(percentage_accuracy)}% | {len(word)} {wordDetails[0]}')
        closestWords.append(wordDetails[1])

    insert_distance_percentage(alldata, csv_filename)    
    perbedaan.sort()
    return [closestWords]
