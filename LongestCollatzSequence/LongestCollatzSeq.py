# File: LongestCollatzSeq.py
# Description: determines what starting number, under one million, produces
#              the longest Collatz sequence

def printList(sampleList):
    print '[%s]' % ', '.join(map(str, sampleList))

def addToSeq(num, collatzSeq):
    collatzSeq.append(num)
    if num == 1:
        return
    elif num % 2 == 0:
        addToSeq((num/2), collatzSeq)
    else:
        addToSeq(((3*num) + 1), collatzSeq)

def produceCollatzSeq(num):
    collatzSeq = []
    collatzSeq.append(num)
    addToSeq(num, collatzSeq)
    # printList(collatzSeq)
    return collatzSeq

def main():
    listOfLengths = []
    for num in xrange(500001, 1000000, 2):
        collatzSeq = produceCollatzSeq(num)
        listOfLengths.append(len(collatzSeq))
        # percent = num / 1000000.0
        # print 'percent: %f' % percent
    print 'maximum length with starting number: %d' % ((listOfLengths.index(max(listOfLengths))*2) + 500001)

if __name__ == "__main__":
    main()
