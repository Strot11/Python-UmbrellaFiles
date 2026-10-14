# Multiprocessing example

from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start {name} chai ordered")
    time.sleep(3)
    print(f"End {name} chai brewed")

print(__name__)

if __name__ == "__main__":
    chai_makers =[
        Process(target=brew_chai,args=(f"Chai Maker #{i+1}", ))
        for i in range(3)
    ]

# Start all process
    for p in chai_makers:
        p.start()

# wait for all to complete
    for p in chai_makers:
        p.join()

    print("All chai brewed Enjoy!!")