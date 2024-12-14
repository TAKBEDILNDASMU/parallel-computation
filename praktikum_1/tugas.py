import threading
import time
import queue

# Class representing a registration system
class Registration(threading.Thread):
    def __init__(self, name, task_queue):
        super().__init__()
        self.name = name
        self.task_queue = task_queue

    def run(self):
        while not self.task_queue.empty():
            customer = self.task_queue.get()
            print(f"{self.name} is registering customer {customer}")
            time.sleep(2)  # Simulate registration process
            self.task_queue.task_done()

# Class representing a queue system for serving customers
class QueueSystem(threading.Thread):
    def __init__(self, name, task_queue):
        super().__init__()
        self.name = name
        self.task_queue = task_queue

    def run(self):
        while not self.task_queue.empty():
            customer = self.task_queue.get()
            print(f"{self.name} is serving customer {customer}")
            time.sleep(3)  # Simulate serving process
            self.task_queue.task_done()

if __name__ == "__main__":
    # Create a queue of customers
    customer_queue = queue.Queue()
    for i in range(1, 6):
        customer_queue.put(f"Customer-{i}")

    # Create and start the registration and queue system threads
    registration = Registration(name="RegistrationDesk", task_queue=customer_queue)
    queue_system = QueueSystem(name="QueueSystemDesk", task_queue=customer_queue)

    registration.start()
    queue_system.start()

    # Wait for threads to complete
    registration.join()
    queue_system.join()

    print("All customers have been registered and served.")
