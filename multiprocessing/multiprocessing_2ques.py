# Queues are thread and process safe

# communicate between processes with the multiprocessing Queue

# import Lock

# import Queue from multiprocessing Manager

#three workers are running
#Suppose third process is very slow. Then first two process are ran very fast
#Two ques are used to share data between each other

from multiprocessing import Lock

from multiprocessing import Process  #, Queue
from multiprocessing import Manager
import time

def main_iteration(numbers, queue, lock):
    for i in numbers:
        with lock:
           print("main_iteration", i)
        queue.put(str(i))


def sub_iteration(q, lock, q2):
    while not q.empty():
        init_val = q.get()
        q2.put(str(init_val))
        for i in range(1,101):
            sub_str = str(init_val) + "." + str(i)
            with lock:
                print("sub :", sub_str)
            q2.put(sub_str)

#Third process is ran here which is very slow

def another_worker(q2, lock):
    while not q2.empty():
        focus_value = q2.get()
        time.sleep(0.5)
        with lock:
            print("Third worker is runing", focus_value)




if __name__ == "__main__":

    start_time = time.time()
    manager = Manager()

    # create a lock
    lock = Lock()

    numbers = range(1, 601)
    q = manager.Queue()
    q2 = manager.Queue()


    p1 = Process(target=main_iteration, args=(numbers, q, lock))
    p2 = Process(target=sub_iteration, args=(q, lock, q2))
    p3 = Process(target=another_worker, args=(q2, lock))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    # order might not be sequential


    print('end main')

    end_time = time.time()
    print("time taken:", end_time - start_time)