from __future__ import division
from math import log
#making vocabulary
def buildVocabulary(vocab):
    with open('allpos.txt') as fp:
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
            #print "things"
            #print features[j][i]
            #print features[j][len(features)]
            if features[j][i]==0:
                #label flase
                if features[j][len(features)]==0:
                    #print "falsefalse"
                    falsefalse=falsefalse+1
                    #print falsefalse
                    labelfalse+=1
                #label true
                elif features[j][len(features)]==1:
                    #print "falsetrue"
                    falsetrue+=1
                    #print falsetrue
                    labeltrue+=1
                # labelfalse+=1
                # print "results:"+str(falsefalse)+","+str(labelfalse)
            # if features[j][i]==0 and features[j][len(features)]==1:
            #     print "falsetrue"
            #     falsetrue+=1
            #     labeltrue+=1
            #     print "results:"+str(falsetrue)+","+str(labeltrue)
            if features[j][i]==1:
                if features[j][len(features)]==0:
                    truefalse+=1
                    labelfalse+=1
                elif features[j][len(features)]==1:
                    truetrue+=1
                    labeltrue+=1
            # if features[j][i]==1 and features[j][len(features)]==0:
            #     #print truefalse
            #     truefalse+=1
            #     labelfalse+=1
            #     #print "results:"+str(truefalse)+","+str(labelfalse)
            # if features[j][i]==1 and features[j][len(features)]==1:
            #     #print "truetrue"
            #     truetrue+=1
            #     labeltrue+=1
                #print "results:"+str(truetrue)+","+str(labeltrue)
        #print "parameters entries???"
            # print "word"+str(j)
            # print "false false"+str(falsefalse)
            # print "true false"+str(truefalse)
            # print "false true"+str(falsetrue)
            # print "true true"+str(truetrue)
            # print "classlabel true"+str(labeltrue)
            # print "classlabel false"+str(labelfalse)
        parameters[i][0]=(falsefalse+1)/(labelfalse/(labelfalse+labeltrue)+2)
        parameters[i][1]=(falsetrue+1)/(labeltrue/(labelfalse+labeltrue)+2)
        #print (falsetrue+1)/(labeltrue+2)
        parameters[i][2]=(truefalse+1)/(labelfalse/(labelfalse+labeltrue)+2)
        #print(float((truefalse+1)/(labelfalse+2)))
        parameters[i][3]=(truetrue+1)/(labeltrue/(labelfalse+labeltrue)+2)
        #print(float((truefalse+1)/(labelfalse+2)))
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
    #predictions=[]
    pclt=0
    pclf=0
    print "length of training features: "+str(len(trainingFeatures))

    for i in range(0, len(trainingfeatures)):
        if trainingfeatures[i][len(trainingfeatures[0])-1]==1:
            pclt+=1
        else:
            pclf+=1
    pclt=pclt/len(trainingfeatures)
    pclf=pclf/len(trainingfeatures)
    print "before log pclt: "+str(pclt)
    print "before log pclf: "+str(pclf)

    probTrue=0
    probFalse=0
    for i in range(0, len(testFeatures)): #itr through sentences
    # for i in range(0, 2): #itr through sentences
        #print "fuck"
        probTrue=1
        probFalse=1
        for j in range(0, len(trainingfeatures[0])-1): #this might need to be a 2
            if testFeatures[i][j]==1:
                probTrue = probTrue+log(trainingParameters[j][3])
                print "trainingParameters[j][3]: "+str(trainingParameters[j][3])
                probFalse = probFalse+log(trainingParameters[j][2])
                print "probfalse 1: "+str(probFalse)
                print "probtrue 1: "+str(probTrue)
            elif testFeatures[i][j]==0:
                probTrue = probTrue+log(trainingParameters[j][1])
                probFalse = probFalse+log(trainingParameters[j][0])
                print "probfalse 0: "+str(probFalse)
                print "probtrue 0: "+str(probTrue)
            # if testFeatures[i][j]==0:
            #     probFalse+= log(trainingParameters[j][0])
            # else:
            #     probFalse+= log(trainingParameters[j][2])
        probFalse = probFalse+log(pclf)
        probTrue = probTrue+log(pclt)
        print "pclt: "+str(pclt)
        print "pclf: "+str(pclf)
        print "making a fucking conclusion???"
        print "probfalse: "+str(probFalse)
        print "probtrue: "+str(probTrue)
        if probTrue>probFalse:
            # print "I think its pos"
            predictions.append(1)
        else:
            # print "I think its neg"
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
makeFeaturesSet('allpos.txt', vocab, trainingFeatures)
preProcessedToTxt('preprocessed_train.txt', trainingFeatures, vocab)

testFeatures=[]
makeFeaturesSet('allpos.txt', vocab, testFeatures)
preProcessedToTxt('preprocessed_test.txt', testFeatures, vocab)
trainingParameters=[]
#training phase
trainingPhase(trainingParameters, trainingFeatures)
predictions=[]
testingPhase(trainingParameters, testFeatures, trainingFeatures, vocab, predictions)

calculateAccuracy(testFeatures, predictions)
