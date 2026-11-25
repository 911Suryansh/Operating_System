# PROGRAM 5
# Process Synchronization - Readers-Writers Problem using Semaphores

def program5():
    mutex = threading.Semaphore(1)
    wrt = threading.Semaphore(1)
    shared = {"read_count": 0, "data": 0}
    lock = threading.Lock()  # keeps print lines from mixing

    def reader(rid):
        mutex.acquire()
        shared["read_count"] += 1
        if shared["read_count"] == 1:
            wrt.acquire()  # first reader locks the resource
        mutex.release()

        with lock:
            print(f"Reader {rid}: read shared_data = {shared['data']}")
        time.sleep(0.2)

        mutex.acquire()
        shared["read_count"] -= 1
        if shared["read_count"] == 0:
            wrt.release()  # last reader unlocks the resource
        mutex.release()

    def writer(wid):
        wrt.acquire()
        shared["data"] += 1
        with lock:
            print(f"Writer {wid}: wrote shared_data = {shared['data']}")
        time.sleep(0.3)
        wrt.release()

    w = [None, None]
    r = [None] * 5

    w[0] = threading.Thread(target=writer, args=(1,))
    w[0].start()
    for i in range(5):
        r[i] = threading.Thread(target=reader, args=(i + 1,))
        r[i].start()
    w[1] = threading.Thread(target=writer, args=(2,))
    w[1].start()

    for t in r:
        t.join()
    w[0].join()
    w[1].join()
