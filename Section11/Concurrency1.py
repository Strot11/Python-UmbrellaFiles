import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(1)

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for order #{i}")
        time.sleep(2)

# Create Threads
order_thread = threading.Thread(target=take_orders)
chai_thread = threading.Thread(target=brew_chai)

order_thread.start()
chai_thread.start()

# wait for both to finsish
order_thread.join()  # Joins says wait until the thread terminates
chai_thread.join()   # Joins says wait until the thread terminates
# join() method is used to make sure that the main thread waits for the completion
#  of the threads before proceeding further.

print(f"All orders taken and chai brewed. Enjoy your chai!")
# This is concurrency not parallelism its multithreading not multiprocessing.


