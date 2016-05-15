#需求：返回随机整数的fabnacci数列
import time
import random
def time_cost(f):
    def _f(*arg, **kwarg):
        start = time.clock()
        a=f(*arg,**kwarg)
        end = time.clock()
        print(f.__name__,"run cost time is ",end-start)
        return a
    return _f

def fib_iter():
	a,b = 0,1
	while True:
		yield b
		a,b = b,a+b
def fib_opt(n):
	a,b,i=0,1,0
	
	while i<n:
		a,b=b,a+b
		i+=1
	else:
		return b

def haha():

    randList = [random.randint(1,50) for i in range(100)]

#A = fib_iter()
#print(time_cost(fib_iter)())
#print([A.__next__() for i in randList])
    print([fib_opt(n) for n in randList])

if __name__=='main':
    haha()
    
