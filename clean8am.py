from __future__ import division
from math import log
#making vocabulary
def buildVocabulary(vocab):
    with open('fourline.txt') as fp:
        line=fp.readline()
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
     for x in xrange(len(temp)-1):
          present = False
          for y in xrange(len(vocab)):
               if temp[x] == vocab[y]:
                    present = True
          if present == False:
               vocab.append(temp[x])
               vocab.sort()
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
    fp.close()
def addSentenceToTable(sentenceArray, table, vocab):
    temp=[]
    bool=False
    for i in range(0, len(vocab)): #itr through sentence
        for j in range(0,len(sentenceArray)):
            if sentenceArray[j]==vocab[i]:
                temp.append(1)
                bool=True
                break
        if bool==False:
            temp.append(0)
        bool=False
    temp.append(int(sentenceArray[len(sentenceArray)-1]))
    table.append(temp)
def preProcessedToTxt(filename, featureset, vocab):
    temp=''
    fp=open(filename, "w")
    vocabstr=""
    for i in range(0,len(vocab)):
        vocabstr=vocabstr+vocab[i]
        vocabstr=vocabstr+','
    vocabstr=vocabstr+'classlabel\n'
    fp.write(vocabstr)
    for i in range(0, len(featureset)):
        for j in range(0, len(vocab)):
            temp=temp+str(featureset[i][j])
            if (j!=len(vocab)-1):
                temp=temp+','
        temp=temp+','
        temp=temp+str(featureset[i][len(vocab)])
        temp=temp+'\n'
        fp.write(temp)
        temp=''
    fp.close()
def trainingPhase(parameters, features):

    count = 0
    for i in range(0, len(features[0])-1):
        parameters.append([5,5,5,5])

    #itr through range of vocab
    for i in range (0, len(features[0])-1):
        #itr through each sentence for val of current vocab word
        falsefalse=0
        falsetrue=0
        truefalse=0
        truetrue=0
        labeltrue=0
        labelfalse=0
        for j in range (0, len(features)):
            count+=1
            if features[j][i]==0:
                if features[j][len(features)]==0:
                    falsefalse=falsefalse+1
                    labelfalse+=1
                elif features[j][len(features)]==1:
                    falsetrue+=1
                    labeltrue+=1
            if features[j][i]==1 and features[j][len(features)]==0:
                truefalse+=1
                labelfalse+=1
            if features[j][i]==1 and features[j][len(features)]==1:
                truetrue+=1
                labeltrue+=1
        parameters[i][0]=(falsefalse+1)/(labelfalse/+2)
        parameters[i][1]=(falsetrue+1)/(labeltrue+2)
        parameters[i][2]=(truefalse+1)/(labelfalse+2)
        parameters[i][3]=(truetrue+1)/(labeltrue+2)
    # print "false false"
    # print falsefalse
    # print "true false"
    # print truefalse
    # print "tfalse true"
    # print falsetrue
    # print "true true"
    # print truetrue
    #
    # print "count:"
    # print count
    # print "label true"
    # print labeltrue
    # print "label false"
    # print labelfals
    # print parameters

def testingPhase(trainingParameters, testFeatures, trainingfeatures, vocab, predictions):
    pclt=0
    pclf=0
    for i in range(0, len(trainingfeatures)):
        if trainingfeatures[i][len(trainingfeatures)]==1:
            pclt+=1
        else:
            pclf+=1
    pclt=pclt/len(trainingfeatures)
    pclf=pclf/len(trainingfeatures)

    probTrue=0
    probFalse=0
    for i in range(0, len(testFeatures)): #itr through sentences
        probTrue=0
        probFalse=0
        for j in range(0, len(trainingfeatures[0])-1): #this might need to be a 2
            if testFeatures[i][j]==1:
                probTrue+= (trainingParameters[j][3])
                probFalse+= (trainingParameters[j][2])
                # print "probfalse: "+str(probFalse)
                # print "probtrue: "+str(probTrue)
            else:
                probTrue+= (trainingParameters[j][1])
                probFalse+= (trainingParameters[j][0])
                # print "probfalse: "+str(probFalse)
                # print "probtrue: "+str(probTrue)
        probFalse+=(pclf)
        probTrue+=(pclt)
        # print
        print "probfalse: "+str(probFalse)
        print "probtrue: "+str(probTrue)
        if probTrue>probFalse:
            print "I think its pos"
            predictions.append(1)
        else:
            print "I think its neg"
            predictions.append(0)

    print predictions
    return predictions
def calculateAccuracy(testfeatures, predictions):
    numSentences=len(testFeatures)
    # numSentences=2
    ind=len(testFeatures[0])
    print ind
    numAccurate=0
    for i in range(0, numSentences):
        if testFeatures[i][len(testFeatures[0])-1]==predictions[i]:
            numAccurate+=1
        else:
            print "sentence: "+str(i+1)
    accuracy=numAccurate/numSentences

    print "Accuracy: "+str(numAccurate)+"/"+str(numSentences)+'='+str(accuracy)
################################################################################
#M A I N
vocab = []
buildVocabulary(vocab)
#print vocab
trainingFeatures=[]
makeFeaturesSet('fourline.txt', vocab, trainingFeatures)
preProcessedToTxt('preprocessed_train.txt', trainingFeatures, vocab)

testFeatures=[]
makeFeaturesSet('fourline.txt', vocab, testFeatures)
preProcessedToTxt('preprocessed_test.txt', testFeatures, vocab)
trainingParameters=[]
#training phase
trainingPhase(trainingParameters, trainingFeatures)
predictions=[]
testingPhase(trainingParameters, testFeatures, trainingFeatures, vocab, predictions)

calculateAccuracy(testFeatures, predictions)
