import Queue

startstate=[3,3,1,0,0,0]
sList=['3,2,0,0,1,1', '2,2,0,1,1,1','3,1,0,0,2,1']
q=Queue.PriorityQueue()
iList=[[3,2,0,0,1,1], [2,2,0,1,1,1],[3,1,0,0,2,1]]

temp=startstate
q.put((0, temp))
q.put((1, '3,2,0,0,1,1'))
q.put((2, [2,2,0,1,1,1]))
q.put(3, sList[2])
tempfromlist=sList[2]
q.put((-4, tempfromlist))

while not q.empty():
    next_item = q.get()
    print(next_item)

print "second half of test for int arrays"
for i in range(0,3):
    state=iList[i]
    prioritynum=i+5
    q.put((prioritynum, state))

while not q.empty():
    next_item = q.get()
    print(next_item)


print "stuff from internet"

d = Queue.PriorityQueue()

d.put((2, 'code'))
d.put((1, 'eat'))
d.put((3, 'sleep'))

while not d.empty():
    next_item = d.get()
    print(next_item)
