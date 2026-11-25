# PROGRAM 6
# Dining Philosophers Problem using Semaphores

def program6():
    N = 5
    forks = [threading.Semaphore(1) for _ in range(N)]
    room = threading.Semaphore(N - 1)  # at most N-1 philosophers try to eat
    lock = threading.Lock()            # keeps print lines from mixing

    def philosopher(pid):
        left = pid
        right = (pid + 1) % N

        for _ in range(2):
            with lock:
                print(f"Philosopher {pid} is thinking")
            time.sleep(0.1)

            room.acquire()          # enter the "room" - avoids deadlock
            forks[left].acquire()   # pick up left fork
            forks[right].acquire()  # pick up right fork

            with lock:
                print(f"Philosopher {pid} is eating (fork {left} and fork {right})")
            time.sleep(0.15)

            forks[right].release()
            forks[left].release()
            room.release()

            with lock:
                print(f"Philosopher {pid} finished eating and put down forks")

    philo = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
    for t in philo:
        t.start()
    for t in philo:
        t.join()

