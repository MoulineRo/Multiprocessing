import time

import requests
from threading import Thread



def net(i):
    x = requests.get(i)
    time.sleep(2)
    file = open("task3_get_net", "a")
    file.write(x.url + "\n")
    file.close()


if __name__ == "__main__":
    t = Thread(target=net, args=['https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2'])
    t1 = Thread(target=net, args=['https://meteo.ua/34/kiev#2023-07-28--15-00'])
    t.start()
    t1.start()
    t.join()
    t1.join()




