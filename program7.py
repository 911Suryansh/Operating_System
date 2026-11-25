# PROGRAM 7
# Deadlock Avoidance using Banker's Algorithm

def program7():
    P = 5  # number of processes
    R = 3  # number of resource types

    maximum = [[0] * R for _ in range(P)]
    allocation = [[0] * R for _ in range(P)]
    need = [[0] * R for _ in range(P)]

    def calculate_need():
        for i in range(P):
            for j in range(R):
                need[i][j] = maximum[i][j] - allocation[i][j]

    def is_safe():
        """Returns (True, safe_sequence) or (False, [])."""
        work = available[:]
        finish = [False] * P
        safe_seq = []

        while len(safe_seq) < P:
            found = False
            for i in range(P):
                if not finish[i]:
                    if all(need[i][j] <= work[j] for j in range(R)):
                        for k in range(R):
                            work[k] += allocation[i][k]
                        safe_seq.append(i)
                        finish[i] = True
                        found = True
            if not found:
                return False, []  # no process could proceed: unsafe
        return True, safe_seq

    def request_resources(pid, request):
        for j in range(R):
            if request[j] > need[pid][j]:
                print("Error: process has exceeded its maximum claim.")
                return False
            if request[j] > available[j]:
                print("Request denied: not enough resources available.")
                return False

        # tentatively allocate
        for j in range(R):
            available[j] -= request[j]
            allocation[pid][j] += request[j]
            need[pid][j] -= request[j]

        safe, _ = is_safe()
        if safe:
            print("Request can be granted safely.")
            return True
        else:
            # rollback
            for j in range(R):
                available[j] += request[j]
                allocation[pid][j] -= request[j]
                need[pid][j] += request[j]
            print("Request denied: would lead to an unsafe state.")
            return False

    # ---- main part of program 7 ----
    available = list(map(int, input(f"Enter available resources of each type ({R} types): ").split()))

    print(f"Enter Maximum matrix ({P} processes x {R} resources), one row per line:")
    for i in range(P):
        maximum[i] = list(map(int, input().split()))

    print("Enter Allocation matrix, one row per line:")
    for i in range(P):
        allocation[i] = list(map(int, input().split()))

    calculate_need()

    safe, seq = is_safe()
    if safe:
        print("System is in a SAFE state.\nSafe sequence:", " ".join(f"P{x}" for x in seq))
    else:
        print("System is in an UNSAFE state.")

    pid = int(input("\nEnter process number requesting resources: "))
    request = list(map(int, input(f"Enter request vector ({R} values): ").split()))

    request_resources(pid, request)
