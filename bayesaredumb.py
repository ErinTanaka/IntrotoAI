from __future__ import division
from math import log

def buildVocabulary(vocabarray, filename):
    print "building vocabulary"
    fp=open(filename, 'r')
    line=fp.readline
    while line:
        tmp=line.translate(None, '&$*().,;:?!')
        tmp=tmp.translate(None, "'")
        tmp=tmp.translate(None, '"')
        tmp=tmp.lower()
        tmplist=tmp.split()
        addToVocab(vocab, tmplist)
        line=fp.readline()
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
    print "making feature set"
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

def preProcessedToTxt():
    print "preprecesed to txt stuf"
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
def trainingPhase():
    print "training phase"
def testingPhase():
    print "testing phase"
def calculateAccuracy():
    print "calculating accuracy"
#M A I N
trainingFilename="trainingSet.txt"
testFilename="trainingSet.txt"
vocab = []
buildVocabulary(vocab, trainingFilename)
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
