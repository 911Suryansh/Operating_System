# PROGRAM 3
# CPU Scheduling Algorithms - FCFS, SJF, Priority and Round Robin

def program3():
    def print_result(p):
        total_wt = 0
        total_tat = 0
        print("\nPID\tAT\tBT\tCT\tTAT\tWT")
        for x in p:
            print(f"{x['pid']}\t{x['at']}\t{x['bt']}\t{x['ct']}\t{x['tat']}\t{x['wt']}")
            total_wt += x["wt"]
            total_tat += x["tat"]
        print(f"Average Waiting Time    = {total_wt / len(p):.2f}")
        print(f"Average Turnaround Time = {total_tat / len(p):.2f}")

    def finish(proc, t):
        proc["ct"] = t
        proc["tat"] = proc["ct"] - proc["at"]
        proc["wt"] = proc["tat"] - proc["bt"]

    def fcfs(p):
        t = 0
        for proc in p:
            if t < proc["at"]:
                t = proc["at"]
            t += proc["bt"]
            finish(proc, t)
        print_result(p)

    def sjf(p):
        n = len(p)
        completed, t = 0, 0
        done = [False] * n
        while completed < n:
            idx, min_bt = -1, 10 ** 9
            for i in range(n):
                if not done[i] and p[i]["at"] <= t and p[i]["bt"] < min_bt:
                    min_bt = p[i]["bt"]
                    idx = i
            if idx == -1:
                t += 1
                continue
            t += p[idx]["bt"]
            finish(p[idx], t)
            done[idx] = True
            completed += 1
        print_result(p)

    def priority_scheduling(p):
        n = len(p)
        completed, t = 0, 0
        done = [False] * n
        while completed < n:
            idx, best = -1, 10 ** 9
            for i in range(n):
                if not done[i] and p[i]["at"] <= t and p[i]["pr"] < best:
                    best = p[i]["pr"]
                    idx = i
            if idx == -1:
                t += 1
                continue
            t += p[idx]["bt"]
            finish(p[idx], t)
            done[idx] = True
            completed += 1
        print_result(p)

    def round_robin(p, quantum):
        n = len(p)
        t, completed = 0, 0
        for proc in p:
            proc["rem"] = proc["bt"]

        queue = []
        in_queue = [False] * n

        # start with process(es) arriving at time 0, in PID order
        for i in range(n):
            if p[i]["at"] <= t:
                queue.append(i)
                in_queue[i] = True

        while completed < n:
            if not queue:
                t += 1
                for i in range(n):
                    if not in_queue[i] and p[i]["rem"] > 0 and p[i]["at"] <= t:
                        queue.append(i)
                        in_queue[i] = True
                continue

            idx = queue.pop(0)
            sl = min(p[idx]["rem"], quantum)
            t += sl
            p[idx]["rem"] -= sl

            for i in range(n):
                if not in_queue[i] and p[i]["rem"] > 0 and p[i]["at"] <= t and i != idx:
                    queue.append(i)
                    in_queue[i] = True

            if p[idx]["rem"] > 0:
                queue.append(idx)
            else:
                finish(p[idx], t)
                completed += 1
                in_queue[idx] = False
        print_result(p)

    # ---- main part of program 3 ----
    n = int(input("Enter number of processes: "))
    p = []
    for i in range(n):
        at, bt, pr = map(int, input(f"Process {i + 1} - Arrival Time, Burst Time, Priority: ").split())
        p.append({"pid": i + 1, "at": at, "bt": bt, "pr": pr,
                  "ct": 0, "tat": 0, "wt": 0, "rem": 0})

    print("\nMenu:\n1. FCFS\n2. SJF (Non-preemptive)")
    print("3. Priority (Non-preemptive)\n4. Round Robin")
    choice = int(input("Enter choice: "))

    if choice == 1:
        fcfs(p)
    elif choice == 2:
        sjf(p)
    elif choice == 3:
        priority_scheduling(p)
    elif choice == 4:
        quantum = int(input("Enter time quantum: "))
        round_robin(p, quantum)
    else:
        print("Invalid choice")
