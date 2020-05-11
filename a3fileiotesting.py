import numpy
def inVocab(vocab, temp):
     print "in the inVocab function"
     for x in xrange(len(temp)-1):
          print len(temp)
          print "temp at x"
          print temp[x]
          present = False
          for y in xrange(len(vocab)):
               print "vocab at y"
               print vocab[y]
               if temp[x] == vocab[y]:
                    present = True
          if present == False:
               print  "in the word is not in vocab"
               vocab.append(temp[x])
               vocab.sort()
               print "Vocab after append and sort:"
               print vocab
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
    print "table entry:"
    print temp
    table.append(temp)

# print "\n\nsecond attempt, using a while loop"
mylist2=[]
vocab = []
count=0
with open('fourline.txt') as fp:
    line=fp.readline()
    while line:
         tmp2=line.translate(None, '&$*().,;:?!')
         tmp2=tmp2.translate(None, "'")
         tmp2=tmp2.translate(None, '"')
         tmp2=tmp2.lower()
         tmplist2=tmp2.split()
         inVocab(vocab, tmplist2)
         line=fp.readline()
         count+=1
fp.close()

print "after all adding:"
print vocab

#open to get number of lines
counter=0
with open('fourline.txt') as toCount:
     line=toCount.readline()
     while line:
          counter+=1
          line=toCount.readline()
toCount.close()

print "length of vocab and counter"
print len(vocab)
print counter

#building the giant table
table=[]
with open('fourline.txt') as fp:
    line=fp.readline()
    while line:
         tmp2=line.translate(None, '&$*().,;:?!')
         tmp2=tmp2.translate(None, "'")
         tmp2=tmp2.translate(None, '"')
         tmp2=tmp2.lower()
         tmplist2=tmp2.split()
         addSentenceToTable(tmplist2, table, vocab)

         line=fp.readline()
         count+=1
fp.close()
print "table built"
