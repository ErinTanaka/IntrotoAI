

import sys
import Queue
#take string from start or goal files and convert to int array
def processStr (string):
    myArray=[0,0,0,0,0,0]
    for i in range(0,6):
        myArray[i]=int(string[i*2])
    return myArray
#checks that wolves won't eat chickens
def isValidState (array):
    for i in range(0,6):
        if (array[i]<0):
            return False
    if (array[0]>=array[1] and array[3]>= array[4]):    #must be more >= chickens
        return True
    elif ((array[0]==0) or (array[3]==0)):                 #unless there are no chickens
        return True
    # elif (array[3]==0 and array[4]==3):
    #     return True
    else:
        return False
def generateSuccessorList(currentState):
    mylist = [[]]
    tempSuccessor=currentState

    if (tempSuccessor[2]==1):
        #switch boat indicator
        tempSuccessor[2]=0
        tempSuccessor[5]=1

        #one chicken
        tempSuccessor[0]=tempSuccessor[0]-1
        tempSuccessor[3]=tempSuccessor[3]+1
        #print tempSuccessor
        if (isValidState(tempSuccessor)):
            mylist.append(tempSuccessor)
        #print mylist
        #2 chicken
        tempSuccessor[0]=tempSuccessor[0]-1
        tempSuccessor[3]=tempSuccessor[3]+1
        #print tempSuccessor
        if (isValidState(tempSuccessor)):
            mylist.append(tempSuccessor)
        #print mylist
        #one wolf
        tempSuccessor[0]=tempSuccessor[0]+2
        tempSuccessor[3]=tempSuccessor[3]-2
        tempSuccessor[1]=tempSuccessor[1]-1
        tempSuccessor[4]=tempSuccessor[4]+1
        #print tempSuccessor
        if (isValidState(tempSuccessor)):
            #print "moved one wolf?"
            mylist.append(tempSuccessor)
        #print mylist#one chicken one wolf
        tempSuccessor[0]=tempSuccessor[0]-1
        tempSuccessor[3]=tempSuccessor[3]+1
        #print tempSuccessor
        if (isValidState(tempSuccessor)):
            mylist.append(tempSuccessor)
        #print mylist#two wolves
        tempSuccessor[0]=tempSuccessor[0]+1
        tempSuccessor[3]=tempSuccessor[3]-1
        tempSuccessor[1]=tempSuccessor[1]-1
        tempSuccessor[4]=tempSuccessor[4]+1
        #print tempSuccessor
        if (isValidState(tempSuccessor)):
            mylist.append(tempSuccessor)
        #print mylist
    else:
        #switch boat indicator
        tempSuccessor[2]=1
        tempSuccessor[5]=0
        #one chicken
        tempSuccessor[0]=tempSuccessor[0]+1
        tempSuccessor[3]=tempSuccessor[3]-1
        if (isValidState(tempSuccessor)):
            mylist.append(tempSuccessor)
        #2 chicken
        tempSuccessor[0]=tempSuccessor[0]+1
        tempSuccessor[3]=tempSuccessor[3]-1
        if (isValidState(tempSuccessor)):
            mylist.append(tempSuccessor)
        #one wolf
        tempSuccessor[0]=tempSuccessor[0]-2
        tempSuccessor[3]=tempSuccessor[3]+2
        tempSuccessor[1]=tempSuccessor[1]+1
        tempSuccessor[4]=tempSuccessor[4]-1
        if (isValidState(tempSuccessor)):
            mylist.append(tempSuccessor)
        #one chicken one wolf
        tempSuccessor[0]=tempSuccessor[0]+1
        tempSuccessor[3]=tempSuccessor[3]-1
        if (isValidState(tempSuccessor)):
            mylist.append(tempSuccessor)
        #two wolves
        tempSuccessor[0]=tempSuccessor[0]-1
        tempSuccessor[3]=tempSuccessor[3]+1
        tempSuccessor[1]=tempSuccessor[1]+1
        tempSuccessor[4]=tempSuccessor[4]-1
        if (isValidState(tempSuccessor)):
            mylist.append(tempSuccessor)
    return mylist

def isGoalState(currentState, goalState):
    if (currentState==goalState):
        return True
    else:
        return False
def printQueue(myQueue):
    print "printQueue Function"
    tmpQueue=Queue.Queue()
    for i in range(0, myQueue.qsize()):
        tmpState=myQueue.get()
        tmpQueue.put(tmpState)
        print tmpState
    return tmpQueue
#bfs uses FIFO queue
#Breadth-first search is an instance of the general graph-search algorithm (Figure 3.7 pg 77 in textbook) in
#which the shallowest unexpanded node is chosen for expansion.
#goal test is applied to each node when it is generated rather than when it is selected for expansion
#Note also that the algorithm, following the general template for graph search, discards any new path to
#a state already in the frontier or explored set; it is easy to see that any such path must be at
#least as deep as the one already found. Thus, breadth-first search always has the shallowest
#path to every node on the frontier.
def bfs(initialState, goalState):
    print "this is the function for Breadth first search"
    if(isGoalState(initialState, goalState)):
        print "done-skis"
    else:
        frontier=Queue.Queue()
        frontier.put(initialState)
        print frontier
        printQueue(frontier)
        currentNode=initialState
        #loopy-doop starts here
        sucessors=generateSuccessorList(currentNode)


#dfs
#LIFO queue





#driver script
# note: arguments are in following order
# initial state file
# goal state file
# mode
# output file

#reading in start state and goal state

#testing stuff

bfs([3,3,1,0,0,0],[0,0,0,3,3,1])


print "testing queue print function"

frontier=Queue.Queue()
frontier.put([3,3,1,0,0,0])
frontier.put([3,2,0,0,1,1])
frontier.put([2,2,0,1,1,1])
frontier.put([3,1,0,0,2,1])

frontier=printQueue(frontier)

print "done with function"
for i in range (0, frontier.qsize()):
    print frontier.get()
