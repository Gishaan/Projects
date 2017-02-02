"""
Purpose: To write a program that simulates the adoption of a new product in a market over time 
Author : Ishaan Gupta, Austin McManus
Date   : October 7, 2016
Project 2
CS 112, Fall 2016
"""
import matplotlib.pyplot as pyplot

def productDiffusion(chanceAdoption, socialContagion, weeks, dt):
   """ Plots a graph of fraction of population adopting the product

    parameters:
          chanceAdoption: Adoption rate by chance alone
          dt: fraction of a week
          weeks: number of weeks to simulate
          socialContagion: Adoption rate by word of mouth alone
    Return value:
          none
   """
   FoP=0                                #fraction of populaiton variable whose value is appended to fractionOfPopulation
   rateOfChange=[0]
   r= chanceAdoption
   s= socialContagion
   timeList=[0]
   fractionOfPopulation=[0]
   roc=0                                #rate of change whose value will be appended to rateOfChange
   for i in range(1,int(weeks/dt)+1):   #loop to calculate fraction of population adopting the product
  
      initialFoP=FoP                    
      FoP= FoP+r*(1- FoP)*dt+s* FoP*(1- FoP)*dt
                                        #difference equation to calculate fraction of population adopting the product
      roc= (FoP-initialFoP)/dt          #calculate rate of change
      timeList.append(i*dt)
      fractionOfPopulation.append(FoP)
      rateOfChange.append(roc)
                                        #code to plot the graph
   pyplot.plot(timeList,fractionOfPopulation,label= 'Fraction Of adoption')
   pyplot.plot(timeList,rateOfChange,label= 'Rate of change')
   pyplot.legend(loc= 'center right')
   pyplot.xlabel('Time (weeks)')
   pyplot.ylabel('Proportion of Adopters')
   pyplot.show()
    

def productDiffusion2(inSize, imSize, rIn, sIn, rIm, sIm, weight, weeks, dt):
   """ Plots 2 graphs. First plots the rate of change of new adoptions of influentials, imitators and total population.
       Second plots the number of adoptions for each group and the total adoptions

    parameters:
          inSize: Size of influential population
          imSize: Size of imitator population
          rIn: Chance adoption rate for influential population
          sIn: Social contagion rate for influential population
          rIm: Chance adoption rate for imitator population
          sIm: Social contagion rate for imitator population
          weight: Fraction of population of imitators who value influentials more than other imitators        
          weeks: Number of weeks in which product launch is simulated
          dt: fraction of a week
    Return value:
          none
   """
   
                                       #roc-> Rate of change

   rocOfinfluentialPopulation = [0]    
   rocOfimitatorPopulation = [0]    
   rocOftotalAdopters = [0]
   rocOfinfpop=0                       #Variable whose value is appended to rocOfinfluentialPopulation
   rocOfimipop=0                       #Variable whose value is appended to rocOfimitatorPopulation
   rocOftapop=0                        #Variable whose value is appended to rocOftotalAdopters
   infpop= 0                           #influential population variable whose value will be appended to influentialPopulation 
   imipop=0                            #imitator population variable whose value will be appended to imitatorPopulation 
   ta=0                                #total population variable whose value will be appended to totalAdopters 
   influentialPopulation = [0]
   imitatorPopulation=[0]
   totalAdopters=[0]
   timeList=[0]

   for i in range(1, int(weeks/dt)+1):#loop to calcuate values for influential, imitator, and total population adopting the product
       initialinfpop = infpop         
       initialimipop = imipop         
       initialta = ta                 
       infpop = infpop + rIn*(1-infpop)*dt + infpop*(1-infpop)*sIn*dt
                                      #difference equation to calculate fraction of influential population adopting the product
       imipop = imipop + rIm*(1-imipop)*dt + weight*sIm*(1-imipop)*(infpop)*dt + (1-weight)*sIm*imipop*(1-imipop)*dt
                                      #difference equation to calculate fraction of imitator population adopting the product
       ta = imipop + infpop           #total population adopting the product in this step
       rocOfinfpop = (infpop - initialinfpop)/dt
                                      #calculates rate of change of influential population
       rocOfimipop = (imipop - initialimipop)/dt
                                      #calculates rate of change of imitator population
       rocOfta = (ta - initialta)/dt
                                      #calculates rate of change of total population
       timeList.append(i*dt)
       influentialPopulation.append(infpop*inSize)
       imitatorPopulation.append(imipop*imSize)
       totalAdopters.append(imipop*imSize + infpop*inSize)

       rocOfinfluentialPopulation.append(rocOfinfpop)
       rocOfimitatorPopulation.append(rocOfimipop)
       rocOftotalAdopters.append(rocOfta)





                                      #Plots a graph for rate of change of total population and population of each group
   pyplot.plot(timeList, rocOfinfluentialPopulation, label = 'roc Of influential Population')
   pyplot.plot(timeList, rocOfimitatorPopulation, label = 'roc Of imitator Population')
   pyplot.plot(timeList, rocOftotalAdopters, label = 'roc Of total Adopters')
   pyplot.legend(loc= 'upper right')
   pyplot.xlabel('time (weeks)')
   pyplot.ylabel('portion of population')
   pyplot.show()

 
                           
                                      #Plots a graph for total number of adopters and adopters in each group
   pyplot.plot(timeList, influentialPopulation, label = 'influential Population')
   pyplot.plot(timeList, imitatorPopulation, label = 'imitator Population')
   pyplot.plot(timeList, totalAdopters, label = 'total Adopters')
   pyplot.legend(loc= 'upper left')
   pyplot.xlabel('time (weeks)')
   pyplot.ylabel('number of population')
   pyplot.show()
           
   
            
              


def main():
    """Calls function profitplot

        parameters:
        none
        Return value:
        none
    """
    productDiffusion(0.001,1.03 , 15, 0.01)
    productDiffusion2(600, 400, .002, 1.03, 0, .8, .6, 15, .01)


main()
