## allows to create processes that runs in parallel
#when to use it?
#1- CPU-Bound Tasks -> Tasks that are heavy on CPU usage (Ex- mathematical computations, data processing)
#2- parallel execution -> Multiple cores of the CPU

import multiprocessing

import time

def sq_num():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_num():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}") 

#every process has a separate memory


if __name__=="__main__":
    #create two processes
    p1 = multiprocessing.Process(target=sq_num)
    p2 = multiprocessing.Process(target=cube_num)

    t=time.time()

    #start the process
    p1.start()
    p2.start()

    #wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(finished_time)


