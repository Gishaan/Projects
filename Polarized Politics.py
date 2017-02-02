"""
Purpose: To ananlyze voting behavior and polarization of the U.S. House over time
Author : Ishaan Gupta
Date   : November 2, 2016
Project 4
CS 112, Fall 2016
"""

import urllib.request as  web
import matplotlib.pyplot as pyplot


def partyLine(year,number):
    """Determines whether House roll call vote number from the given year was a party line vote

     parameters:
          year: Year of vote
          number: Roll call number
     Return value:
           True or False
    """
    str1 = ('{0:03}'.format(number))
    url='http://clerk.house.gov/evs/'+str(year)+'/roll'+str1+'.xml'
    webpage= web.urlopen(url)
    republicanMember=0
    republicanSayYes=0
    republicanSayNo=0
    democraticMember=0
    democraticSayYes=0
    democraticSayNo=0
    for line in webpage:                       #loop to check each line for tag <recorded-vote>
        line= line.decode('utf-8')             #decodes the line
        if line[:15]=='<recorded-vote>':
            for i in range(len(line)):         #loop to check each line for party="R"
                if line[i:i+9]=='party="R"':
                    republicanMember= republicanMember +1
                    for k in range(len(line)): #loop to check each line for Yea/Aye or No/Nay
                        if line[k:k+16]=='<vote>Yea</vote>' or line[k:k+16]=='<vote>Aye</vote>':
                            republicanSayYes=republicanSayYes+1
                        if line[k:k+16]=='<vote>Nay</vote>' or line[k:k+15]=='<vote>No</vote>':
                           republicanSayNo=republicanSayNo+1
                        
                if line[i:i+9]=='party="D"':
                    democraticMember= democraticMember +1
                    for k in range(len(line)):
                        if line[k:k+16]=='<vote>Yea</vote>' or line[k:k+16]=='<vote>Aye</vote>':
                            democraticSayYes=democraticSayYes+1
                        if line[k:k+16]=='<vote>Nay</vote>' or line[k:k+15]=='<vote>No</vote>':
                            democraticSayNo=democraticSayNo+1
                                               #if statement to check whether its a party line vote                                               
    if (democraticMember/2)<=democraticSayYes and (republicanMember/2)<=republicanSayNo\
       or (democraticMember/2)<=democraticSayNo and (republicanMember/2)<=republicanSayYes:
        return True
    return False
       
    webpage.close()

def countPartyLine(year, maxNumber):
    """ Returns the fraction of votes that were party line votes during a given year.

     parameters:
          year: Year of vote
          maxNumber: Number of the last roll call vote of the year
     Return value:
          The fraction of votes that were party line votes
    """
 
    partyLineVotes = 0
    for i in range(1, maxNumber + 1):     #calling the function partyLine and counting the partyLineVotes
        if partyLine(year, i):
            partyLineVotes = partyLineVotes + 1
    return partyLineVotes/maxNumber



def plotPartyLine():
    """Plots the fraction of party line votes for the last 20 years

     parameters:
          None
     Return value:
          None
    """
 
    fractionOfPartyLine = []
    fpl = 0                                 #variable to append values to fraction of party line votes 
    number = [640, 547, 611, 603,512,484,677,544,671,543,1186,690,991,664,949,659,641,564,705,574]
    years = []
    y = 1997                               #variable to append values to years
    for i in number:                        #loop to find the fraction of party line votes
        fpl = countPartyLine(y, i)
        fractionOfPartyLine.append(fpl)
        years.append(y)
        y = y + 1
                                            #code to plot the graph of the fractions of party line votes
    pyplot.plot(years, fractionOfPartyLine, label = 'Fraction Of Party Line')
    pyplot.legend(loc = 'upper left')
    pyplot.xlabel('Years')
    pyplot.ylabel('Fraction Of Party Line Votes')
    pyplot.show()




def stateDivide(state):
    """Plots the number of Democratic and Republican representatives for the given state every year for the last 20 years

     parameters:
          state: name of the state
     Return value:
          none
    """
 
    year=1997
    years=[]
    republicanMember=[]
    rm=0                                    #number of republican members
    democraticMember=[]
    dm=0                                    #number of democratic members
    for k in range(20):                     #loop runing the whole code 20 times
        url='http://clerk.house.gov/evs/'+str(year)+'/roll'+str(194)+'.xml'
        webpage= web.urlopen(url)
        for line in webpage:                #loop looking for <recorded-vote>
            line= line.decode('utf-8')
            if line[:15]=='<recorded-vote>':
                for i in range(len(line)):  #loop looking for state
                    if line[i:i+10]==state:
                        for j in range(len(line)): #loop looking for republican and democratic members
                            if line[j:j+9]=='party="R"':
                                rm= rm +1
                            if line[j:j+9]=='party="D"':
                                dm= dm +1
        republicanMember.append(rm)
        democraticMember.append(dm)
        rm=0
        dm=0
        years.append(year)
        year =year +1
                                            #code used to plot the graphs
    pyplot.plot(years, republicanMember, label='Republicians in '+state)
    pyplot.plot(years, democraticMember, label= 'Democratics in '+state)
    pyplot.legend(loc='center right')
    pyplot.xlabel('years')
    pyplot.ylabel('Number of members')
    pyplot.show()


   
def main():
    """Calls functions
        parameters:
             none
        Return value:
             none
    """
    
    x1=partyLine(2010,194)
    print(x1)
    x2=partyLine(2010,200)
    print(x1)
    stateDivide('state="OH"')
    stateDivide('state="FL"')
    stateDivide('state="PA"')
    stateDivide('state="CA"')
    stateDivide('state="NY"')
    plotPartyLine()

main()

    


