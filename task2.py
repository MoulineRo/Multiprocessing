import time
from threading import Thread
from multiprocessing import Process


def example(i):
    summ = i + 100 * 150
    time.sleep(2)
    print(summ)


if __name__ == "__main__":
    t = Thread(target=example, args=[2])
    t1 = Process(target=example, args=[2])
    t.start()
    t1.start()
    t.join()
    t1.join()