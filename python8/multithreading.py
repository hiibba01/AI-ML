###Multithreading
#When to use multithreading?
#1- I/O bound tasks: Tasks that spend more time waiting for I/O operations (eg-file operation, network nequests).
#2- Concurrent execution: When u want to improve the throughput of your application by performing multiple operations concurrently. 

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

#creating two threads so that we can save time
t1 = threading.Thread(target=print_numbers) #responsible in executing the first function
t2 = threading.Thread(target=print_letter)  #responsible in executing the second function

t = time.time()
# print_numbers()        
# print_letter()


#start the thread
t1.start()
t2.start()  #in this during the sleep of fierst function my sec thread will start executing and vice versa


#wait for the threads to complete
t1.join()
t2.join()
finished_time = time.time()-t
print(finished_time)

#here time is reduced to half due to multithreading