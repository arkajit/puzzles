def spiral(n):
    # print list of coordinates in clockwise order
    start = 0
    stop = n-1
    while start <= stop:
        spiral_help(start, stop)
        start += 1
        stop -= 1    

def spiral_help(i, j):
    for k in range(i,j+1):
        print "(%d, %d)" % (k,i)
    for k in range(i+1, j+1):
        print "(%d, %d)" % (j, k)
    for k in range(j-1, i-1, -1):
        print "(%d, %d)" % (k, j)
    for k in range(j-1, i+1-1, -1):
        print "(%d, %d)" % (i,k)

spiral(5)
