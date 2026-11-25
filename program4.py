# PROGRAM 4
# Process Synchronization - Producer-Consumer Problem using Semaphores

def program4():
    BUFFER_SIZE = 5
    ITEMS = 10

    buffer = [0] * BUFFER_SIZE
    state = {"in": 0, "out": 0}

    empty = threading.Semaphore(BUFFER_SIZE)
    full = threading.Semaphore(0)
    mutex = threading.Semaphore(1)

    def producer():
        for i in range(1, ITEMS + 1):
            empty.acquire()
            mutex.acquire()

            buffer[state["in"]] = i
            print(f"Producer produced item {i} at slot {state['in']}")
            state["in"] = (state["in"] + 1) % BUFFER_SIZE

            mutex.release()
            full.release()
            time.sleep(0.1)

    def consumer():
        for _ in range(ITEMS):
            full.acquire()
            mutex.acquire()

            item = buffer[state["out"]]
            print(f"\t\tConsumer consumed item {item} from slot {state['out']}")
            state["out"] = (state["out"] + 1) % BUFFER_SIZE

            mutex.release()
            empty.release()
            time.sleep(0.15)

    # print() here is already protected by the 'mutex' semaphore,
    # so lines from producer and consumer never mix.
    prod = threading.Thread(target=producer)
    cons = threading.Thread(target=consumer)
    prod.start()
    cons.start()
    prod.join()
    cons.join()
    print("All items produced and consumed.")