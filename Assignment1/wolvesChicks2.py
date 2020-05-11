import sys
import Queue
import copy

global frontierIDDFS
global visitedHash
global counter
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

def oneC(currentState, myList, check):
    temp = copy.deepcopy(currentState)
    if(check):
        temp[0]=temp[0]-1
        temp[3]=temp[3]+1
    else:
        temp[0]=temp[0]+1
        temp[3]=temp[3]-1
    if(isValidState(temp)):
        myList.append(temp)

    return myList

def twoC(currentState, myList, check):
    temp = copy.deepcopy(currentState)
    if(check):
        temp[0]=temp[0]-2
        temp[3]=temp[3]+2
    else:
        temp[0]=temp[0]+2
        temp[3]=temp[3]-2
    if(isValidState(temp)):
        myList.append(temp)

    return myList

def oneW(currentState, myList, check):
    temp = copy.deepcopy(currentState)
    if(check):
        temp[1]=temp[1]-1
        temp[4]=temp[4]+1
    else:
        temp[1]=temp[1]+1
        temp[4]=temp[4]-1
    if(isValidState(temp)):
        myList.append(temp)

    return myList

def twoW(currentState, myList, check):
    temp = copy.deepcopy(currentState)
    if(check):
        temp[1]=temp[1]-2
        temp[4]=temp[4]+2
    else:
        temp[1]=temp[1]+2
        temp[4]=temp[4]-2
    if(isValidState(temp)):
        myList.append(temp)

    return myList

def oneWoneC(currentState, myList, check):
    temp = copy.deepcopy(currentState)
    if(check):
        temp[1]=temp[1]-1
        temp[4]=temp[4]+1
        temp[0]=temp[0]-1
        temp[3]=temp[3]+1
    else:
        temp[1]=temp[1]+1
        temp[4]=temp[4]-1
        temp[0]=temp[0]+1
        temp[3]=temp[3]-1
    if(isValidState(temp)):
        myList.append(temp)

    return myList

def generateSuccessorList(currentState):
    myState=copy.deepcopy(currentState)
    print "in generate successor list"
    myList=[[]]
    check = True
    if (myState[2]==1):
        # change boat bit
        check = True
        myState[2]=0
        myState[5]=1
        #print myState
    else:
        check = False
        myState[2]=1
        myState[5]=0
        #print myState

    # move one chickens
    myList = oneC(myState, myList, check)
    #print myList
    #print myState

    #move 2 chickens
    myList = twoC(myState, myList, check)
    #print myList
    #print myState

    # move one w
    myList = oneW(myState, myList, check)
    #print myList
    #print myState

    # move 1 each
    myList = oneWoneC(myState, myList, check)
    #print myList
    #print myState

    # move 2w
    myList = twoW(myState, myList, check)
    #print myList
    #print myState

    return myList

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
def hasBeenVisited(currStr, hash):
    for key in hash:
        if (hash[key][0]==stringToArray(currStr)):
            return True
    return False
def stringToArray(mystr):

    myArray=[0,0,0,0,0,0]
    myArray[0]=int(mystr[0])
    #print myArray
    myArray[1]=int(mystr[2])
    #print myArray
    myArray[2]=int(mystr[4])
    #print myArray
    myArray[3]=int(mystr[6])
    #print myArray
    myArray[4]=int(mystr[8])
    #print myArray
    myArray[5]=int(mystr[10])
    #print myArray
    return myArray
def arrayToString(myArray):
  myStr=','.join(str(x) for x in myArray)
  return myStr
# def traceBackSolution(myHash, startState, goalState, currstr):
#     print "this is the trace back function"
#     print myHash
#     solutionList=[goalState]
#     startstr=arrayToString(startState)
#     goalStr=arrayToString(goalState)
#     currentNode=goalState
#     while (currentNode!=startState):
#         preDecStr=""
#         for key in myHash: #iterate through hash codes
#             for i in range(0, len(myHash[key])):#in hash code iterate through possiblesuccessors
#                 if (myHash[key][i]==currentNode):# successor is what I'm looking for
#                     preDecStr=key #predecessor of currentNode is key
#                     break # stop looking through current key
#             if (preDecStr!=""): #predec has been found
#                 break #stop looking through hash tablefor currentNode's predecessor
#         solutionList.append(stringToArray(preDecStr))#add predecessor to solution path
#         currentNode=stringToArray(preDecStr) # set up for next iteration precedesor for this round becomes thing I am lking for a predecessoe for
#         break
#     solutionList.append(currentNode)
#     return solutionList
def tbTwoPointOh(hash, startarray, goalarray, currentstring):
    print "this is hash traceback fn"
    print "this is the hash table"
    keyCount=0
    for key in hash:
        keyCount += 1
    solutionList=[goalarray]
    curr=goalarray
    for i in range(0,keyCount):
        print i
        print hash[str(i)]
    print "\n"
    #for i in range(0,3):
    while(not isGoalState(curr, startarray)):
        print "mywhile lp"
        for i in range(0, keyCount): #iterate through all keys
            #if hash[str(i)][0]==preDec: #this is the predecessor I want
            mybool=False
            for j in range(1, len(hash[str(i)])): #find curr
                if hash[str(i)][j]==curr:
                    curr=hash[str(i)][0] #set curr to be its predecessor
                    solutionList.append(curr) #append this predecessor to the solution list
                    mybool=True
                    break
            if mybool==True:
                break
        if (curr == startarray):
            print "gottee"
            break
    print "this is the solution list"
    solutionList.reverse()
    print solutionList
    printItPretty(solutionList)
    #return solutionList
    exit()

def printItPretty(solutionList):
    print "nodes in solution: "+str(len(solutionList))
    for i in range(0, len(solutionList)):
        buffer1=str(solutionList[i][0])+','+str(solutionList[i][1])+','+str(solutionList[i][2])
        buffer2=str(solutionList[i][3])+','+str(solutionList[i][4])+','+str(solutionList[i][5])
        print buffer1
        print buffer2
        print

#bfs uses FIFO queue
#Breadth-first search is an instance of the general graph-search algorithm (Figure 3.7 pg 77 in textbook) in
#which the shallowest unexpanded node is chosen for expansion.
#goal test is applied to each node when it is generated rather than when it is selected for expansion
#Note also that the algorithm, following the general template for graph search, discards any new path to
#a state already in the frontier or explored set; it is easy to see that any such path must be at
#least as deep as the one already found. Thus, breadth-first search always has the shallowest
#path to every node on the frontier.

#order of operations pseudo currentNode
# put initial state in Queue
# generate successors
# put sucessors on Queue
# add sucessors to hashtable
# pop initial state off of queue



def bfs(initialState, goalState):
    print "this is the function for Breadth first search"
    expansions = 0
    if(isGoalState(initialState, goalState)):
        print "done-skis"
    else:
        frontier=Queue.Queue()
        visitedHash = {}
        print visitedHash
		#currStr=[]
        frontier.put(initialState)
        while True:
            print "beg while loop"
            if (frontier.empty()):
                print "I have failed, no solution"
                break
            currentNode=frontier.get()
            if (isGoalState(currentNode, goalState)):
                #fn to trace back solution
                print "done goal state found"
                print "expansions:"
                print expansions
                print "hell on wheels... gears... whaever is in computers"
                #solList=traceBackSolution(visitedHash, initialState, goalState, currStr)
                solList=tbTwoPointOh(visitedHash, initialState, goalState, currStr)

                print solList
                break
            currStr=','.join(str(x) for x in currentNode)
            print currStr
            if (hasBeenVisited(currStr, visitedHash)):
                print "in hash table already"
            else:
                print "currnt node hasnt been visited"
                key=str(expansions)
                print key
                visitedHash[key]=[currentNode]
                expansions += 1
                succList=generateSuccessorList(currentNode)
                print succList
                for i in range (1,len(succList)):
                    print "forloop"
                    print succList[i]
                    visitedHash[key].append(succList[i])
                    if(isGoalState(succList[i], goalState)):
                        print "hey bfs we found the answer!"
                        print "nodes expanded:" + str(expansions)
                        tbTwoPointOh(visitedHash, initialState, goalState, currStr)
                        #call print hash and exit
                        break
                    frontier.put(succList[i])
                    #visitedHash[key].append(succList[i])
                print ("this is hash table at currStr:"+ str(expansions-1))
                print visitedHash[str(expansions-1)]
            if (isGoalState(currentNode, goalState)):
                #fn to trace back solution
                print "done goal state found"
                print "expansions:"
                print expansions
                print "hell on wheels... gears... whaever is in computers"
                solList=traceBackSolution(visitedHash, initialState, goalState, currStr)
                print solList
                break


#dfs
#LIFO queue
def dfs(initialState, goalState):
    print "this is the function for depth first search"
    expansions = 0
    currStr=''
    if(isGoalState(initialState, goalState)):
        print "done-skis"
    else:
        frontier=Queue.LifoQueue()
        visitedHash={}
        frontier.put(initialState)
        while True:
            print "beg while loop"
            if (frontier.empty()):
                print "I have failed, no solution"
                break
            currentNode=frontier.get()
            if (isGoalState(currentNode, goalState)):
                #fn to trace back solution
                print "done goal state found"
                print "expansions:"
                print expansions
                tbTwoPointOh(visitedHash,initialState, goalState, currStr)
                break
            currStr=','.join(str(x) for x in currentNode)
            print currStr
            if (hasBeenVisited(currStr, visitedHash)):
                print "in hash table already"
            else:
                print "currnt node hasnt been visited"
                key=str(expansions)
                expansions += 1
                print expansions
                visitedHash[key]=[currentNode]
                succList=generateSuccessorList(currentNode)
                print succList
                for i in range (1,len(succList)):
                    print "forloop"
                    print succList[i]
                    frontier.put(succList[i])
                    visitedHash[key].append(succList[i])
                print visitedHash[key]
            if (isGoalState(currentNode, goalState)):
                #fn to trace back solution
                print "done goal state found"
                print "expansions:"
                print expansions
                break


#what the fuck is up with these indents
def dls(currentState, goalState, limit):
    print currentState
    global counter
    frontierIDDFS=Queue.LifoQueue()
    frontierIDDFS.put(currentState)
    visitedHash={}
    currStr=''
    hashkeyint=0
    if(isGoalState(currentState, goalState)):
        return currentState
        #path from hastable
    else:
        for i in range(1, limit):
          currentNode=frontierIDDFS.get()
          print "dls current node frickfrack"
          print currentNode
          if (isGoalState(currentNode, goalState)):
              #fn to trace back solution
              print "done goal state found"
              print "expansions:"
              print counter
              ##print shit
              print "ohmygod we need less of these catchy thingys"
              print visitedHash
              tbTwoPointOh(visitedHash, currentState, goalState, currStr)


          else:
              currStr=','.join(str(x) for x in currentNode)
              print currStr
              if (hasBeenVisited(currStr, visitedHash)):
                  print "in hash table already"
              else:
                  print "currnt node hasnt been visited"
                  counter += 1
                  print counter
                  print limit
                  key=str(hashkeyint)
                  hashkeyint += 1
                  visitedHash[key]=[currentNode]
                  succList=generateSuccessorList(currentNode)
                  print succList
                  for i in range (1,len(succList)):
                      print "forloop"
                      print succList[i]
                      frontierIDDFS.put(succList[i])
                      visitedHash[key].append(succList[i])
                      print visitedHash[key]
                      if (isGoalState(currentNode, goalState)):
                          #fn to trace back solution
                          print "heres my hash table before calling race back"
                          print visitedHash
                          tbTwoPointOh(visitedHash, currentState, goalState, currStr)
                          print "done goal state found"
                          print "expansions:"
                          print counter
                          return currentNode
                          if(True):
                              return currentNode


#iterative deepening depth first search
def iddfs(currentState, goalState):
    print "this is the function for iterative deepening depth first search"
    print currentState
    global frontierIDDFS
    #expansions = 0
    #frontier=Queue.LifoQueue()
    #visitedHash={}
    frontierIDDFS.put(currentState)
    limit=1
    returned = dls(currentState, goalState, limit)
    while(not isGoalState(returned, goalState)):
        print "iddfs while loop"
        limit += 1
        print "limit"
        print limit
        dls(currentState, goalState, limit)
    print "solution found"
#informed A* search

def aStar(initialState, goalState):
    frontier=Queue.PriorityQueue()
    visitedHash={}
    expansions=0
    print"initial state"+str(initialState)
    currStr=arrayToString(initialState)
    myvar=(0, initialState)
    print myvar
    frontier.put(myvar)
    currStr=''
    while (True):
        currentNode=frontier.get()
        print (currentNode)
        key=str(expansions)
        print "fudge"
        print "expansions: "+str(expansions)
        print currentNode

        #if (hasBeenVisited(arrayToString(currentNode[1]), visitedHash)):
        currStr=','.join(str(x) for x in currentNode[1])
        print currStr
        if (hasBeenVisited(currStr, visitedHash)):
            print "skipit yo"
            print "skip again dog"
        else:
            print "in conditional"
            visitedHash[key]=[currentNode[1]]
            succList=generateSuccessorList(currentNode[1])
            print succList
            expansions+=1
            for i in range(1, len(succList)):
                print succList[i]
                tmp=succList[i]
                visitedHash[key].append(succList[i])
                if (isGoalState(succList[i], goalState)):
                    print "nodes expanded: "+str(expansions)
                    tbTwoPointOh(visitedHash, initialState, goalState, currStr)
                w=heurisiticFunction(succList[i], goalState)
                frontier.put((w, tmp))
                print "printing queue Function"
                tmpQueue=Queue.PriorityQueue()
                while not frontier.empty():
                    tmpState=frontier.get()
                    tmpQueue.put(tmpState)
                    print tmpState
                frontier=tmpQueue


def heurisiticFunction(current, goal):
    print "this is heruistic" + str(current)
    a=goal[3]
    b=current[3]
    c=goal[4]
    d=current[4]
    w=(a-b)+(c-d)
    return w


#driver script
# note: arguments are in following order
# initial state file
# goal state file
# mode
# output file


inititalStateFile=open(sys.argv[1],"r")
startstr=inititalStateFile.read()
inititalStateFile.close()
print startstr
startArray=[int(startstr[0]),int(startstr[2]),int(startstr[4]),int(startstr[6]),int(startstr[8]),int(startstr[10])]
print startArray

goalStateFile=open(sys.argv[2],"r")
goalstr=goalStateFile.read()
goalStateFile.close()
print goalstr
goalArray=[int(goalstr[0]),int(goalstr[2]),int(goalstr[4]),int(goalstr[6]),int(goalstr[8]),int(goalstr[10])]
print goalArray

frontierIDDFS=Queue.LifoQueue()
visitedHash={}
counter = 0

output=sys.argv[4]
sys.stdout = open(output, 'w')

if(sys.argv[3]=="bfs"):
    bfs(startArray, goalArray)
elif(sys.argv[3]=="dfs"):
    dfs(startArray, goalArray)
elif(sys.argv[3]=="iddfs"):
    iddfs(startArray, goalArray)
elif(sys.argv[3]=="astar"):
    aStar(startArray, goalArray)

#aStar([3,3,1,0,0,0],[0,0,0,3,3,1])
#bfs([3,3,1,0,0,0],[0,0,0,3,3,1])
#dfs([3,3,1,0,0,0],[0,0,0,3,3,1])
