def fib_loop(n):
    '''
    Returns the nth number in the fibonachi series.
   
    It uses for loop to calculate it.
    '''
    for i in range(n):
	print(i)

    
def fib_recursion(n):
    '''
    Returns the nth number in the fibonachi series.
   
    It uses for loop to calculate it.
    '''

def fib_generator(n):
    '''
    Generator version of fibonacci.
    '''

print(fib_loop(8))
print(fib_recursion(13))
print([i for i in fib_generator(14)])
