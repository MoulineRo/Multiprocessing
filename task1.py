import time
from threading import Thread


def even(i):
    if i == 0:
        for y in range(20):
            yy = y % 2
            if not yy:
                print(y)
        time.sleep(5)
    if i == 1:
        for y in range(20):
            yy = y % 2
            if yy:
                print(y)
        time.sleep(5)


if __name__ == "__main__":
    t = Thread(target=even, args=[0])
    t1 = Thread(target=even, args=[1])
    t.start()
    t1.start()
    t.join()
    t1.join()

