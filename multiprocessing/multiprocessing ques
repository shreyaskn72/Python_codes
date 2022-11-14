# communicate between processes with the multiprocessing Queue
# Queues are thread and process safe
# import Lock

from multiprocessing import Lock

from multiprocessing import Process, Queue


def main_iteration(numbers, queue, lock):
    for i in numbers:
        with lock:
           print("main_iteration", i)
        queue.put(str(i))


def sub_iteration(q, lock):
    while not q.empty():
        init_val = q.get()
        for i in range(1,101):
            with lock:
                sub_str = str(init_val)+ "."+ str(i)
                print("sub :", sub_str)


if __name__ == "__main__":

    # create a lock
    lock = Lock()

    numbers = range(1, 601)

    #create que
    q = Queue()



    p1 = Process(target=main_iteration, args=(numbers, q, lock))
    p2 = Process(target=sub_iteration, args=(q, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # order might not be sequential


    print('end main')
