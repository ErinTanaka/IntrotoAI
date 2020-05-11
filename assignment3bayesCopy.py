from __future__ import division
from math import log

def buildVocabulary(vocab):
    with open('trainingSet.txt') as fp:
        line=fp.readline()
        while line:
            tmp=line.translate(None, '&$*().,;:?!')
            tmp=tmp.translate(None, "'")
            tmp=tmp.translate(None, '"')
            tmp=tmp.lower()
            tmplist=tmp.split()
            addToVocab(vocab, tmplist)
            line=fp.readline()
            #count+=1
        fp.close()
def addToVocab(vocab, temp):
     #print "in the inVocab function"
     for x in xrange(len(temp)-1):
          #print len(temp)
          #print "temp at x"
          #print temp[x]
          present = False
          for y in xrange(len(vocab)):
               #print "vocab at y"
               #print vocab[y]
               if temp[x] == vocab[y]:
                    present = True
          if present == False:
               #print  "in the word is not in vocab"
               vocab.append(temp[x])
               vocab.sort()
               #print "Vocab after append and sort:"
               #print vocab
def makeFeaturesSet(filename, vocab, featArray):
    with open(filename) as fp:
        line=fp.readline()
        while line:
             tmp=line.translate(None, '&$*().,;:?!')
             tmp=tmp.translate(None, "'")
             tmp=tmp.translate(None, '"')
             tmp=tmp.lower()
             tmplist=tmp.split()
             addSentenceToTable(tmplist, featArray, vocab)
             line=fp.readline()
             #count+=1
    fp.close()
def addSentenceToTable(sentenceArray, table, vocab):
    temp=[]
    bool=False
    for i in range(0, len(vocab)): #itr through vobac words
        for j in range(0,len(sentenceArray)): #itr thriugh sentence
            if sentenceArray[j]==vocab[i]:
                temp.append(1)
                bool=True
                break
        if bool==False:
            temp.append(0)
        bool=False
    temp.append(int(sentenceArray[len(sentenceArray)-1]))
    #print "table entry:"
    #print temp
    table.append(temp)
def preProcessedToTxt(filename, featureset, vocab):
    temp=''
    #open(filename, '+w') as fp:        #filename in '' ?
    fp=open(filename, "w")
    vocabstr=""
    for i in range(0,len(vocab)):
        vocabstr=vocabstr+vocab[i]
        vocabstr=vocabstr+','
    vocabstr=vocabstr+'classlabel\n'
    # print vocabstr
    fp.write(vocabstr)
    for i in range(0, len(featureset)):
        for j in range(0, len(vocab)):
            temp=temp+str(featureset[i][j])
            if (j!=len(vocab)-1):
                temp=temp+','
        #print temp
        temp=temp+','
        temp=temp+str(featureset[i][len(vocab)])
        temp=temp+'\n'
        #print temp
        fp.write(temp)
        temp=''
    fp.close()
def trainingPhase(parameters, features):
    #mk table to store parameters in
    for i in range(0, len(features[0])-1):
        parameters.append([5,5,5,5])
    #itr through vocab word by world
    for word in range(0, len(features[0])-1):
        #places to store prob counts
        ff=0
        ft=0
        tf=0
        tt=0
        lt=0
        lf=0
        for sentence in range(0, len(features)):
            if features[sentence][word]==0 and features[sentence][len(features[0])-1]==0:
                ff+=1
                lf+=1
            elif features[sentence][word]==0 and features[sentence][len(features[0])-1]==1:
                ft+=1
                lt+=1
            elif features[sentence][word]==1 and features[sentence][len(features[0])-1]==0:
                tf+=1
                lf+=1
            elif features[sentence][word]==1 and features[sentence][len(features[0])-1]==1:
                tt+=1
                lt+=1
        #calculate and store prob
        parameters[word][0]= (ff+1)/(lf+2)
        parameters[word][1]= (ft+1)/(lt+2)
        parameters[word][2]= (tf+1)/(lf+2)
        parameters[word][3]= (tt+1)/(lt+2)
        # print parameters[word]

def testingPhase(parameters, testfeat, trainfeat, vocab, predictions):

    pclt = 0
    pclf = 0
    for sentence in range(0, len(trainfeat)):
        if trainfeat[sentence][len(trainfeat[0])-1]==1:
            pclt+=1
        else:
            pclf+=1
    pclt=pclt/len(trainfeat)
    pclf=pclf/len(trainfeat)
    #iterate through each sentence and predict its rank
    for sentence in range(0, len(testfeat)):
        #place to store each probability
        ptrue=0.0
        pfalse=0.0
        print "wow I made these dumb variables that are probably still zero"
        print ptrue
        print pfalse
        #iterate through each word in/no in the sentence and add its prob to the total
        for word in range(0, len(testfeat[0])-1):
            if testfeat[sentence][word]==1:
                print "conditional"
                print log(parameters[word][3])
                print log(parameters[word][2])
                print ptrue
                print pfalse
                ptrue= ptrue+log(parameters[word][3])
                pfalse=pfalse+log(parameters[word][2])
                print "post mltiplicatin?"
                print ptrue
                print pfalse
            elif testfeat[sentence][word]==0:
                ptrue=ptrue+log(parameters[word][1])
                pfalse=pfalse+log(parameters[word][0])
        print ptrue
        print pfalse
        pfalse=pfalse+log(pclf)
        ptrue=ptrue+log(pclt)
        print ptrue
        print pfalse
        print
        print
        if ptrue>pfalse:
            predictions.append(1)
        else:
            predictions.append(0)
    # print predictions
#def trainingTwoPointOh(parameters, testfeat, trainfeat, vocab, predictions):


def calculateAccuracy(testfeatures, predictions):
    numSentences=len(testFeatures)
    # numSentences=2
    ind=len(testFeatures[0])
    # print ind
    numAccurate=0
    for i in range(0, numSentences):
        if testFeatures[i][len(testFeatures[0])-1]==predictions[i]:
            numAccurate+=1
        # else:
        #     print "sentence: "+str(i+1)
    accuracy=numAccurate/numSentences

    print "Accuracy: "+str(numAccurate)+"/"+str(numSentences)+'='+str(accuracy)

#M A I N
vocab = []
buildVocabulary(vocab)
#print vocab
trainingFeatures=[]
makeFeaturesSet('trainingSet.txt', vocab, trainingFeatures)
preProcessedToTxt('preprocessed_train.txt', trainingFeatures, vocab)

testFeatures=[]
makeFeaturesSet('testSet.txt', vocab, testFeatures)
preProcessedToTxt('preprocessed_test.txt', testFeatures, vocab)

parameters=[]
predictions=[]
trainingPhase(parameters, trainingFeatures)
testingPhase(parameters, testFeatures, trainingFeatures, vocab, predictions)
calculateAccuracy(testFeatures, predictions)

print predictions
