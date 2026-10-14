# GIL threading - Mutex Locking

import threading
import time
count = 0
def brew_chai():
    global count
    print(f"{threading.current_thread().name} started the brewing process")
    
    for _ in range(100_000_000):
        count+=1
    print(f"{threading.current_thread().name} finished the brewing process")

thread1 = threading.Thread(target=brew_chai,name="Dhaga-1")
    
thread2 = threading.Thread(target=brew_chai,name="Dhaga-2")

start = time.time()

thread1.start()
thread2.start()
thread1.join()
thread2.join()

end = time.time()

print(f"Total time taken : {end - start:.2f} seconds")
