
def mymax(x,y):
    if x > y:
        return x
    else:
        return y
    return

i = 2
j = 4

#print ("The maximum of", i, "and", j, "is", mymax(i,j),"\n")
#print ('The maximum of %d and %d is %d' %(i, j, mymax(i,j)))
print ("The maximum of {} and {} is {}".format(i, j, mymax(i,j)))

def listmax(l):
    lmax = 0
    for i in l:
        print (i)
        if i > lmax:
            lmax = i
        return lmax
        #if i > lmax:
        #    lmax = i
        #return lmax
      
#mylist = [2, 2, 6]
#for x in mylist:
#    print (x)

#print (listmax(mylist))

#print (__name__)

#if __name__="__name__":
#    print (listmax(mylist))


        
            



