from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some number...")
    total = 0;
    for i in range(10**7):
        total += i
    print(f"Done! Result: {total}")

start = time.time()

if __name__ == "__main__":
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    
    [t.start() for t in processes]
    [t.join() for t in processes]

print(f"Time Taken: {time.time() - start:.2f} seconds")