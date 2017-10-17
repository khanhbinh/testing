def mymax(x, y):
    '''
    Return the max of two parameters
    '''
    return listmax([x, y])

def listmax(l):
    lmax = 0
    for i in l:
        if i > lmax:
            lmax = i
    return lmax


#if __name__ == "__main__":
#    import sys
#    mylist = [int(arg) for arg in sys.argv[1:]]
#    print(listmax(mylist))

#print(__name__)
if __name__ == "__main__":
    import sys
    print(sys.argv)
    myList = []
    for arg in sys.argv[1:]:
        myList.append(int(arg))
    print(myList)
    print(listmax(myList))

            


