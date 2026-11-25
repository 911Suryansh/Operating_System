PROGRAM 2
# Thread Creation and Management using POSIX Threads (pthreads)
# -> Python threading module
def program2():
    NUM_THREADS = 4
    n = 1000000
    chunk = n // NUM_THREADS
    data = [{"start": 0, "end": 0, "sum": 0} for _ in range(NUM_THREADS)]
    lock = threading.Lock()  # keeps print lines from mixing

    def sum_array(p):
        p["sum"] = 0
        for i in range(p["start"], p["end"]):
            p["sum"] += i
        with lock:
            print(f"Thread {threading.get_ident() % 100000}: "
                  f"sum[{p['start']}..{p['end']}) = {p['sum']}")

    threads = []
    for i in range(NUM_THREADS):
        data[i]["start"] = i * chunk
        data[i]["end"] = n if i == NUM_THREADS - 1 else (i + 1) * chunk
        t = threading.Thread(target=sum_array, args=(data[i],))
        threads.append(t)
        t.start()

    total = 0
    for i in range(NUM_THREADS):
        threads[i].join()
        total += data[i]["sum"]

    print(f"Total sum (0 to {n - 1}) computed using {NUM_THREADS} threads = {total}")

