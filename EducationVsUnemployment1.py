"""
Ishaan Gupta
CS 112
Project #5
Education vs. Employment
"""
import matplotlib.pyplot as pyplot

def plotEducation(file):
    """Plots education vs unemployment for 366 metro areas

    Parameter:
        file: the file with the information on the metro areas

    Return Value: None
    """
    textFile = open(file, 'r', encoding = 'utf-8')
    metList = []                                                                    # names of metropolitan areas
    popTotalList = []                                                               # total populations of metropolitan areas
    noHSList = []                                                                   # unemployment amongst people with no HS diploma
    highSchoolList = []                                                             # unemployment amongst people with only a HS diploma
    someCollList = []                                                               # unemployment amongst people with some college
    collGradList = []                                                               # unemployment amongst people with a college degree
    textFile.readline()
    textFile.readline()
    for line in textFile:                                                           # iterates over each line of textFile
        lineList = line.split('\t')                                                 # creates a list of each tab separated word in a line
        metList.append(lineList[2])
        popTotalList.append(lineList[3])
        noHSList.append(round((int(lineList[15]) / int(lineList[11])) * 100, 1))
        highSchoolList.append(round((int(lineList[29]) / int(lineList[25])) * 100, 1))
        someCollList.append(round((int(lineList[43]) / int(lineList[39])) * 100, 1))
        collGradList.append(round((int(lineList[57]) / int(lineList[53])) * 100, 1))
    textFile.close()
    pyplot.xticks(range(len(metList)), metList, rotation = 270, fontsize = 'small') # formats the x-axis labels 
    pyplot.plot(noHSList, label = 'No High School Diploma Unemployment Rate')
    pyplot.plot(highSchoolList, label = 'High School Diploma Unemployment Rate')
    pyplot.plot(someCollList, label = 'Some College Unemployment Rate')
    pyplot.plot(collGradList, label = 'College Graduate Unemployment Rate')
    pyplot.legend(loc = 'upper right')
    pyplot.xlabel('Metropolitan Area')
    pyplot.ylabel('Unemployment Rate')
    pyplot.show()

def plotThirtyCities(file):
    """Plots education vs unemployment for 30 metro areas

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
            if lineList1[2] in metList:
                continue
            if str(population) == lineList1[3]:                                     # compares each value in popTotalList with each value in lineList at index 3
                metList.append(lineList1[2])
                noHSList.append(round((int(lineList1[15]) / int(lineList1[11])) * 100, 1))
                highSchoolList.append(round((int(lineList1[29]) / int(lineList1[25])) * 100, 1))
                someCollList.append(round((int(lineList1[43]) / int(lineList1[39])) * 100, 1))
                collGradList.append(round((int(lineList1[57]) / int(lineList1[53])) * 100, 1))
                textFile.seek(0)
                break
                
    textFile.close()
    pyplot.xticks(range(len(metList)), metList, rotation = 270, fontsize = 'xx-small')
    pyplot.plot(noHSList, label = 'No High School Diploma Unemployment Rate')
    pyplot.plot(highSchoolList, label = 'High School Diploma Unemployment Rate')
    pyplot.plot(someCollList, label = 'Some College Unemployment Rate')
    pyplot.plot(collGradList, label = 'College Graduate Unemployment Rate')
    pyplot.legend(loc = 'upper right')
    pyplot.xlabel('Metropolitan Area')
    pyplot.ylabel('Unemployment Rate')
    pyplot.show()   

def main():
    '''
    Calls the above functions
    
    Parameters:
         None
         
    Return Value:
         None
    '''
    plotEducation('acs.txt')
    plotThirtyCities('acs.txt')

main()
    
