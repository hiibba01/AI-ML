'''
Real world ex : Multiprocessing for CPU bound tasks
Scenario : Factorial Calculation , especially for large no
involve sifgnificant computational work. Multiprocessing can be used to 
distribute the work load across multiple CPU cores, improving performance '''


import multiprocessing
import math
import sys
import time

#Increase the max no of digit for integer conversion
sys.set_int_max_str_digits(100000)
##function to compute factorial

def compute_fact(num):
    print(f"Computing factorial of {num}")
    result = math.factorial(num)
    print(f"Factorial of {num} is {result}")
    return result

if __name__=="__main__":   #creating the entry point
    numbers=[5000,6000,9000,2000]

    start_time=time.time()

    #create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_fact,numbers)

    end_time=time.time()    

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
