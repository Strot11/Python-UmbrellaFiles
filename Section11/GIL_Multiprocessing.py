# Solved GIL Bottleneck using Multiprocessing


from multiprocessing import Process,current_process
import time
count = 0
def crunch_numbers():
    print(f"{current_process().name} started the crunching process")
    global count
    for _ in range(100_000_000):
        count += 1
    print(f"{current_process().name} finished the crunching process") 

if __name__ == "__main__":
    start = time.time()

    process1 = Process(target=crunch_numbers,name="Process-1")
    process2 = Process(target=crunch_numbers,name="Process-2")
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")

#Threading: A thread runs a function inside the same process, sharing its memory and
#  interpreter.
#Multiprocessing: A new child process gets its own memory space and Python interpreter,
#  so on Windows it imports the main file during startup.