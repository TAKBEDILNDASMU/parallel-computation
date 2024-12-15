import threading
import time
from random import randint

# Lock Definition
threadLock = threading.Lock()
# store all thread in this array
threads = []

class Registration(threading.Thread):
    def __init__(self, name, duration) -> None:
        super().__init__() 
        self.name = name
        self.duration = duration

    def run(self):
        # acquire lock
        threadLock.acquire()
        print(f"{self.name} thread is being processing...\n")

        # Release the lock before time.sleep() 
        threadLock.release()

        # simulate the real world task with time.sleep
        time.sleep(self.duration)
        print(f"{self.name} thread is finish processing ^_^\n")

class Process(threading.Thread):
    def __init__(self, name, duration) -> None:
        super().__init__() 
        self.name = name
        self.duration = duration

    def run(self):
        # acquire lock
        threadLock.acquire()
        print(f"{self.name} thread is being processing...\n")

        # Release the lock
        threadLock.release()

        # simulate the real world task with time.sleep
        time.sleep(self.duration)
        print(f"{self.name} thread is finish processing ^_^\n")

def main():
    start_time = time.time() # For calculating the time spend for executing all thread

    # 25 thread for registration and 25 thread for process
    for i in range(1, 26):
        threads.append(Registration(name=f"Registration {i}", duration=randint(1, 5)))
    for i in range(1, 26):
        threads.append(Process(name=f"Process {i}", duration=randint(1, 5)))

    # Start the thread and join all together
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print("all thread is comleted")
    print(f"Execution takes up time about {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

