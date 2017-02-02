"""
Ishaan Gupta
CS 112
Project 5
Part 3: Analysis
"""
def questionOne(file):
    """Calculates the cities with the higher unemployment rate for HS graduates than thohse without a HS diplomw

    Parameter:
        file: the file with information on the metro areas

    Return Value: the cities where the unemployment rate is higher for high school graduates than non-graduates
    """
    textFile = open(file, 'r', encoding = 'utf-8')
    metList = []
    popTotalList = []
    noHSList = []
    highSchoolList = []
    higherUnempHSGrad = []
    textFile.readline()
    textFile.readline()
    for line in textFile:
        lineList = line.split('\t')
        popTotalList.append(int(lineList[3]))
    popTotalList.sort()
    popTotalList = popTotalList[-30:]                      # sets population list to only the 30 most populous

    textFile.seek(0)                                       # sets pointer in textFile back to first line
    textFile.readline()                                    # reads first line in the file
    textFile.readline()                                    # reads second line in the file                                        
    for population in popTotalList:                        # iterates over values in popTotalList
        for line1 in textFile:
            lineList1 = line1.split('\t')
            if lineList1[2] in metList:                    # if two cities have the same population, this statement would append the value to the right city
                continue
            if str(population) == lineList1[3]:            # compares each value in popTotalList with each value in lineList at index 3
                metList.append(lineList1[2])
                noHSList.append(round((int(lineList1[15]) / int(lineList1[11])) * 100, 1))
                highSchoolList.append(round((int(lineList1[29]) / int(lineList1[25])) * 100, 1))
                textFile.seek(0)
                break

    for index in range(len(highSchoolList)):
        if noHSList[index] < highSchoolList[index]:        # determines if the rate of unemployment is higher for those with a high school diploma
            higherUnempHSGrad.append(metList[index])       # this list is added to if the above is true
    return higherUnempHSGrad

def questionTwo(file):
    """Prints the cities with the maximum and minimum unemployment rates amongst each group

    Parameter:
        file: the file with information on the metro areas

    Return Value: None
    """
    textFile = open(file, 'r', encoding = 'utf-8')
    metList = []
    popTotalList = []
    noHSList = []
    highSchoolList = []
    someCollList = []
    collGradList = []
    textFile.readline()
    textFile.readline()
    for line in textFile:
        lineList = line.split('\t')
        popTotalList.append(int(lineList[3]))
    popTotalList.sort()
    popTotalList = popTotalList[-30:]                      # sets population list to only the 30 most populous

    textFile.seek(0)                                       # sets pointer in textFile back to first line
    textFile.readline()
    textFile.readline()
    for population in popTotalList:                        # iterates over values in popTotalList
        for line1 in textFile:
            lineList1 = line1.split('\t')
            if lineList1[2] in metList:                    # if two cities have the same population, the function will continue
                continue
            if str(population) == lineList1[3]:            # compares each value in popTotalList with each value in lineList at index 3
                metList.append(lineList1[2])
                noHSList.append(round((int(lineList1[15]) / int(lineList1[11])) * 100, 1))
                highSchoolList.append(round((int(lineList1[29]) / int(lineList1[25])) * 100, 1))
                someCollList.append(round((int(lineList1[43]) / int(lineList1[39])) * 100, 1))
                collGradList.append(round((int(lineList1[57]) / int(lineList1[53])) * 100, 1))
                textFile.seek(0)
                break
            
    maxNoHSCity = ''                                        # creates a space for the city string (same for those below)
    minNoHSCity = ''
    maxHighSchoolCity = ''
    minHighSchoolCity = ''
    maxSomeCollCity = ''
    minSomeCollCity = ''
    maxCollGradCity = ''
    minCollGradCity = ''
    maxNoHSList = noHSList[0]                               # creates a max list for no high school diploma
    minNoHSList = noHSList[0]                               # creates a min list for no high school diploma
    maxHighSchoolList = highSchoolList[0]                   # for this list and those below, creates a max or min for the leftover categories of educational attainment
    minHighSchoolList = highSchoolList[0]
    maxSomeCollList = someCollList[0]
    minSomeCollList = someCollList[0]
    maxCollGradList = collGradList[0]
    minCollGradList = collGradList[0]

    for index in range(len(metList)):                       # for the categories below, adds to the index of those lists if the values agree with the if statement
        if minNoHSList > noHSList[index]:
            minNoHSList = noHSList[index]
            minNoHSCity = metList[index]
        elif maxNoHSList < noHSList[index]:
            maxNoHSList = noHSList[index]
            maxNoHSCity = metList[index]
        if minHighSchoolList > highSchoolList[index]:
            minHighSchoolList = highSchoolList[index]
            minHighSchoolCity = metList[index]
        elif maxHighSchoolList < highSchoolList[index]:
            maxHighSchoolList = highSchoolList[index]
            maxHighSchoolCity = metList[index]
        if minSomeCollList > someCollList[index]:
            minSomeCollList = someCollList[index]
            minSomeCollCity = metList[index]
        elif maxSomeCollList < someCollList[index]:
            maxSomeCollList = someCollList[index]
            maxSomeCollCity = metList[index]
        if minCollGradList > collGradList[index]:
            minCollGradList = collGradList[index]
            minCollGradCity = metList[index]
        elif maxCollGradList < collGradList[index]:
            maxCollGradList = collGradList[index]
            maxCollGradCity = metList[index]

    print('The city with the maximum no high school unemployment is ' +maxNoHSCity)
    print('The city with the minimum no high school unemployment is ' +minNoHSCity)
    print('The city with the maximum high school grad unemployment is ' +maxHighSchoolCity)
    print('The city with the minimum high school grad unemployment is ' +minHighSchoolCity)
    print('The city with the maximum some college unemployment is ' +maxSomeCollCity)
    print('The city with the minimum some college unemployment is ' +minSomeCollCity)
    print('The city with the maximum college grad unemployment is ' +maxCollGradCity)
    print('The city with the minimum college grad unemployment is ' +minCollGradCity)    

def questionThree(file):
    """Finds the city with the maximum difference between the college and high school graduates' unemployment rates

    Parameter:
        file: the file with information on the metro areas

    Return Value: The city with the maximum difference and the difference
    """
    textFile = open(file, 'r', encoding = 'utf-8')
    metList = []
    popTotalList = []
    noHSList = []
    highSchoolList = []
    someCollList = []
    collGradList = []
    textFile.readline()
    textFile.readline()
    for line in textFile:
        lineList = line.split('\t')
        popTotalList.append(int(lineList[3]))
    popTotalList.sort()
    popTotalList = popTotalList[-30:]                                               # sets population list to only the 30 most populous

    textFile.seek(0)                                                                # sets pointer in textFile back to first line
    textFile.readline()
    textFile.readline()
    for population in popTotalList:                                                 # iterates over values in popTotalList
        for line1 in textFile:
            lineList1 = line1.split('\t')
            if lineList1[2] in metList:                                             # if two cities have the same population, the function will continue
                continue
            if str(population) == lineList1[3]:                                     # compares each value in popTotalList with each value in lineList at index 3
                metList.append(lineList1[2])
                highSchoolList.append(round((int(lineList1[29]) / int(lineList1[25])) * 100, 1))
                collGradList.append(round((int(lineList1[57]) / int(lineList1[53])) * 100, 1))
                textFile.seek(0)
                break

    difference = abs(collGradList[0] - highSchoolList[0])                           # defines difference
    maxDiffCity = metList[0]                                                        # sets maxDiffCity equal to the first item in the metList
    for index in range(1,len(metList)):
        if abs(collGradList[index] - highSchoolList[index]) > difference:
              difference = abs(collGradList[index] - highSchoolList[index])         # redefines difference
              maxDiffCity = metList[index]                 
              
    return maxDiffCity, difference

def questionFour(file):
    """Orders the cities with the highest college graduate unemployment rates and prints a formatted table of them

    Parameter:
        file: the file with information on the metro areas

    Return Value: None
    """
    textFile = open(file, 'r', encoding = 'utf-8')
    metList = []
    popTotalList = []
    noHSList = []
    highSchoolList = []
    someCollList = []
    collGradList = []
    textFile.readline()
    textFile.readline()
    for line in textFile:
        lineList = line.split('\t')
        popTotalList.append(int(lineList[3]))
    popTotalList.sort()
    popTotalList = popTotalList[-30:]                                               # sets population list to only the 30 most populous

    textFile.seek(0)                                                                # sets pointer in textFile back to first line
    textFile.readline()
    textFile.readline()
    for population in popTotalList:                                                 # iterates over values in popTotalList
        for line1 in textFile:
            lineList1 = line1.split('\t')
            if lineList1[2] in metList:                                             # if two cities have the same population, the function will continue
                continue
            if str(population) == lineList1[3]:                                     # compares each value in popTotalList with each value in lineList at index 3
                metList.append(lineList1[2])
                collGradList.append((float(lineList1[57]) / float(lineList1[53])) * 100)
                textFile.seek(0)
                break

    rankedCitiesTable = {}                                                          # creates a dictionary
    for index in range(len(metList)):
        if metList[index] in rankedCitiesTable:
            continue
        rankedCitiesTable[collGradList[index]] = metList[index]
    collGradList.sort()                                                             # sorts the list
    for value in collGradList:
        print('{0:<10} {1:>50}'.format(value, rankedCitiesTable[value]))            # prints the table with particular formatting
         
def main():
    print(questionFour('acs.txt')) 

main()










        
        
