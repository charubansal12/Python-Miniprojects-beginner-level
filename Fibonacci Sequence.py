import os
def fib(n):
    if(n==0):
        print "Error encountered!"
        os._exit(1)
    else:
        fibo=[]*(n+1)
        fibo.append(1)
        fibo.append(1)
        for i in xrange(2,n+1,1):
            fibo.append(fibo[i-1]+fibo[i-2])
            

    print fibo[n-1]


n=input("Enter the index value for which you want to display the fibonnaci number")
fib(n)
    
    
