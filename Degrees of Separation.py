"""
Purpose: Analyze the data on IMDb and determine if it is a scale-free network.
Create a function that allows someone to play the oracle of Bacon game
Authors: Ishaan Gupta
Date: December 9, 2016
CS 112, Fall 2016
"""
import matplotlib.pyplot as pyplot

def createNetwork(filename):
    """
    Purpose: Creates 2 network in the form of dictionaries. The first dictionary takes every actor
             as keys and all of the actors they have been in a movie with are the values. The second
             dictionary has movie titles as the keys and every actor in the movie as the values.

    Parameters:
             filename: the name of data file you want to create a dictionary for

    Return Value:
             The actor and movie dictionaries explained above
    """


    textfile = open(filename, 'r', encoding='utf-8')
    actorDictionary={}
    movie={}
    for line in textfile:
        line=line.rstrip('\n')                              #takes away the new line character from each line
        list1=line.split('\t')                              #creates a list that splits the line everywhere a tab appears
        movie[list1[0]]=[]
        for item1 in list1[1:]:
            movie[list1[0]]=movie[list1[0]]+[item1]         #appends the values of the movie dictionary with the item          
        for actor in list1[1:]:                             #Iterates over the actor names in the line
            if actor not in actorDictionary:               
                actorDictionary[actor]=[]                   #creates a key using the new actor and adds it to the dictionary                                      
            for actor1 in list1[1:]:                        #Iterates over the actor names in the line
                if actor1 not in actorDictionary[actor] and actor1!=actor: #appends the new actor to the list of actors that appeared in a movie with the actor who is the key                                      
                    actorDictionary[actor]=actorDictionary[actor] + [actor1]

    return actorDictionary,movie

def degreeDistribution(actorDictionary):
    """
    Purpose: Creates a degree distribution histogram using the actor dictionary from the previous function
             in order to determine if it is a scale-free network.

    Parameters:
             actorDictionary: dictionary with actors as keys and values of lists of other actors they have acted with

    Return Value:
             None
    """

    degree = []
    fraction = []
    maxDegree = 0
    for item in actorDictionary:
        degree = degree + [len(actorDictionary[item])]
    pyplot.hist(degree,100) #range up to max degree pyplot.hist buckets same as degrees
    pyplot.xlabel('degree')
    pyplot.ylabel('No. of actors')
    pyplot.show()

    


def bfs(network, source,dest):
    """
    Purpose: Finds the shortest path between 2 items in a network. 

    Parameters:
             network: a dictionary
             source: the first actor
             dest: the actor you would like to connect to the first actor

    Return Value:
             Returns the distance and predecessor dictionaries
    """

    distance = {}                      
    visited = {}
    predecessor = {}
    for node in network:                                    #sets the values of the dictionaries distance, visited, predecessor to false, infinity and none
        visited[node] = False
        distance[node] = float('inf')
        predecessor[node] = None
        
    visited[source] = True                                  #makes source visited true
    distance[source] = 0                                    #distance to source is 0 
    queue = [source]                                        #creates queue containing the source
    front=''
    while queue != [] and front!=dest:                      #create a while loop that runs while there is a queue and you have not reached the destination
        front = queue.pop(0)                                #removes the front of queue and sets it equal to front
        for neighbor in network[front]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[front] + 1    #increments the distance of the actor from the source
                predecessor[neighbor] = front               #sets the predecessor equal to front
                queue.append(neighbor)                      #appends neighbor to the queue
    return distance,predecessor



def oracle(network):
    """
    Purpose: When 2 actors are input, it states the distance between them.

    Parameters:
            network: a dictionary 
             

    Return Value:
             None
    """
    
    actor1 = input('who is actor 1? ')
    actor2 = input('who is actor 2? ')
    while actor1 != 'Stop' and actor2 != 'Stop':            #While loop to stop asking user name of actors
        distance,predecessor=bfs(network, actor1, actor2)
        print("distance between",actor1,"and",actor2,"is", distance[actor2])
        actor1 = input('who is actor 1? ')
        actor2 = input('who is actor 2? ')
       

def baconNumbers(network):
    """
    Purpose: Create a table that shows the frequency of people qith different Bacon numbers.

    Parameters:
            network: a dictionary
             

    Return Value:
             None
    """
    distance,c=bfs(network,'Kevin Bacon',None)              #uses bfs with Kevin Bacon as source
    frequency={}
    for item in distance:
        if distance[item] not in frequency:
            frequency[distance[item]]=1                     #sets distance equal to one
        else:
            frequency[distance[item]]=frequency[distance[item]]+1 #adds one to distance for each loop
    print("{0:^15}{1:^15}".format('Bacon Number','Frequency'))    #code to print the formatted table
    print('-'*15,'-'*15)
    count=-1
    for key in frequency.keys():
        count=count+1
        if key==float('inf'):
            print('{0:^15} {1:^15}'.format(count,0))
            print('{0:^15} {1:^15}'.format(count+1,0))
            print('{0:^15} {1:^15}'.format(key,frequency[key]))
        else:
            print('{0:^15} {1:^15}'.format(key,frequency[key]))
           
            
def extraChallenge(network, movie):
    """
    Purpose: When 2 actors are input, it states the distance between them and states the movies that link the actors

    Parameters:
            network: a dictionary with actors as keys
            movie: a dictionary with movies as keys
             

    Return Value:
             None
    """
    
    actor1 = input('who is actor 1? ')
    actor2 = input('who is actor 2? ')
    while actor1 != 'Stop' and actor2 != 'Stop':
        distance,predecessor=bfs(network, actor1, actor2)                              #use bfs to get distance and predecessor dictionaries
        print("distance between",actor1,"and",actor2,"is", distance[actor2])
        count=0
        path = findPath(actor2,predecessor)                                            #uses the findPath function to determine the path between 2 actors
        for index in range(len(path[:-1])):
            for item1 in movie:
                if (path[index] in movie[item1]) and (path[index +1] in movie[item1]): #if 2 people are in the same movie, it adds 1 to the count
                    count=count+1
                    print(str(count)+".",path[index]," was in ", item1, "with", path[index+1])
        actor1 = input('who is actor 1? ')
        actor2 = input('who is actor 2? ')
    


def findPath(dest, predecessor):
    """
    Purpose: Finds the path between 2 actors

    Parameters:
            dest: the actor you would like to connect to the first actor
            predecessor: the dictionary that lists what actor comes before another actor
             
    Return Value:
             Path
    """

    
    path = [dest]
    
    while dest != None:
            predNode = predecessor[dest]                                                #sets predNode equal to the predecessor of the destination
            if predNode != None:
                    path.insert(0, predNode)                                            #add predNode to the path
            dest = predNode                                                             #sets destination equal to predNode
            
    return path


def maxDegree(actorDictionary):
    """
    Purpose: Finds the actors having maximum degree

    Parameters:
            actorDictionary: network of actors as keys and values as the actors with whom they have played a role with
             
    Return Value:
             None
    """
    degree = []
    fraction = []
    maxDegree = 0
    for item in actorDictionary:                                                    #Loop to find out the degree of each actor
        degree = degree + [(len(actorDictionary[item]),actorDictionary[item])]                              
    
    degree.sort()                                                                   #Sorts the degree list
    print(degree[-10:])
                
        

def main():
    
    network,movie=createNetwork('movies_mpaa.txt')
    maxDegree(network)
    degreeDistribution(network)
    oracle(network)
    baconNumbers(network)
    extraChallenge(network, movie)
main()




    

