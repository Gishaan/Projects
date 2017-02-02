"""
Purpose: To write a program that investigates the accuracy of polls from a random sample
Author : Ishaan Gupta
Date   : October 19, 2016
Project 3
CS 112, Fall 2016
"""
import matplotlib.pyplot as pyplot
import random

def poll(percentage, pollSize):
   """Simulates the polling of a pollSize with the given percentage of people
      who will respond yes.

    parameters:
          percentage: Percentage of population who will agree with the statement
          pollSize: Number of people who will be polled.
    Return value:
          percentageOfYes = returns percentage of people who responded yes
   """
   peopleWhoAgree=0                            
   for i in range(pollSize):        #Loop to calculate number of people who agree 
       r = random.random()          #r is a random number between [0,1)
       if r*100<=percentage:        #multiplyig r by 100 to get a 2 digit number
           peopleWhoAgree = peopleWhoAgree + 1
   percentageOfYes= (peopleWhoAgree/pollSize)*100
                                    #equation to find out percentage of people who agree
   return percentageOfYes
   

def pollExtremes(percentage, pollSize, trials):   
   """Find minimum and maximum percentage of people who agree

    parameters:
          percentage: Percentage of population who will agree with the statement
          pollSize: Number of people who will be polled.
          trials: number of times the polling is done
    Return value:
          Minimum and maximum percentages in the list
   """
   pollResults= []                 #list to append the values of percentage of people who agree
   for i in range(trials):         #loop to find different percentage of values who agree
      pollValue = poll(percentage, pollSize)
      pollResults.append(pollValue)
   return min(pollResults),max(pollResults) 

def plotResults(percentage, minPollSize, maxPollSize, step, trials):
   """PLots graph for maximum and minimum percentage

    parameters:
          percentage: Percentage of population who will agree with the statement
          maxPollSize: Maximum number of people who will be polled.
          minPollSize: Minimum number of people who will be polled.
          trials: number of times the polling is done
          step: number to increment from minPollSize to maxPollSize
    Return value:
          returns margin error
   """
   lowList = []                   #List containg minimum percentage who agree in a given population
   highList = []                  #List containg maximum percentage who agree in a given population
   population = []                #list containing total population being evaluated 

   while minPollSize<=maxPollSize:#loop to increment poll size and find percentage of people agreeing for different population
      low,high = pollExtremes(percentage, minPollSize, trials)
      lowList.append(low)
      highList.append(high)
      population.append(minPollSize)
      minPollSize = minPollSize + step
                                  #incrementing population size

                                  # plotting graphs for curves of minimum and maximum percentage of agreement 
   pyplot.plot(population, lowList, label = 'Min. Percentage of agreement')
   pyplot.plot(population, highList, label = 'Max. Percentage of agreement')
   pyplot.legend(loc='upper right')
   pyplot.xlabel('Poll Size')
   pyplot.ylabel('Percentage')
   pyplot.show()
   low1,high1 = pollExtremes(percentage, maxPollSize, trials)
   moe = (high-low)/2             #finds out margin of error(moe)
   return moe


def plotErrors(pollSize, minPercentage, maxPercentage, step, trials):
   """PLots graph for margin of error

    parameters:
          minPercentage: minimum percentage of population who will agree with the statement
          maxPercentage: maximum percentage of population who will agree with the statement
          pollSize: Number of people who will be polled.
          trials: number of times the polling is done
          step: number to increment from minPollSize to maxPollSize         
    Return value:
          none
   """
   marginOfError = []
   pollPercentageList = []
   while minPercentage<=maxPercentage:#Loop to calculate margin of error
      low, high = pollExtremes(minPercentage, pollSize, trials)
      moe = (high-low)/2           #Calcualtes margin of error
      marginOfError.append(moe)
      pollPercentageList.append(minPercentage)
      minPercentage = minPercentage + step
   pyplot.plot(pollPercentageList, marginOfError, label='margin of error')
   pyplot.legend(loc='upper right')
   pyplot.xlabel('Percentage')
   pyplot.ylabel('Margin of error')
   pyplot.show()
  

def main():
    """Calls function poll, pollExtremes, pollResults, plotErrors

        parameters:
        none
        Return value:
        none
    """
    
    percentageOfYes = poll(30,1000)
    print(percentageOfYes)
    
    low, high = pollExtremes(30,1000,5)
    print(low,high)
    
    marginOfError = plotResults(30,10,1000,10,100)
    print(marginOfError)

    plotErrors(1500,10,80,1,100)

main()
