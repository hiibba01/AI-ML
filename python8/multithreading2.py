### Multithreading with thread poool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_num(number):
    time.sleep(1)
    print(f"Number: {number}")

    ###due to multithreading even though the function calls sleep but still number gets printed faster than the time taken to sleep because of multithreading.

numbers = [1, 2, 3, 4, 5, 6, 7 , 8 , 9, 10, 1 ,2, 3]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_num, numbers)

for result in results:
    print(result)        

   
 