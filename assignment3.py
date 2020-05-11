

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
            count+=1
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
             count+=1
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
    with open(filename) as fp:
        for i in range(0, len(featureset)):
            temp=[]
            for j in range(0, len(vocab)):
                temp.append(char(featureset[i][j]))
                temp.append(',')
            temp[len(featureset)]='\r'
            #write "line" to file
################################################################################
#M A I N
vocab = []
buildVocabulary(vocab)
#print vocab
trainingFeatures=[]
makeFeaturesSet('fourline.txt', vocab, trainingFeatures)
preProcessedToTxt('freat.txt', trainingFeatures, vocab)
#testFeatures=[]
#makeFeaturesSet('testSet.txt', vocab, testFeatures)
