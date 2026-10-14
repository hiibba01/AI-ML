### Multiprocessing with processPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time


def square(number):
    time.sleep(1)
    print(f"Square: {number*number}")

numbers = [1,2,3,4,5,6,7,8,9,0,10,4,6,4,5,6,4,3,54,5,5,35,3]

if __name__=="__main__": #use this when it demands entry point for the program to avoid recursive spawning of subprocesses

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)

    for result in results:
        print(result)

