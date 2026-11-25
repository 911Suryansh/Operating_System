# PROGRAM 8
# Contiguous Memory Allocation - First Fit, Best Fit and Worst Fit

def program8():
    def show(title, psize, allocation):
        print(f"\n--- {title} ---")
        print("Process No.\tProcess Size\tBlock No.")
        for i in range(len(psize)):
            line = f"P{i + 1}\t\t{psize[i]}\t\t"
            line += f"B{allocation[i] + 1}" if allocation[i] != -1 else "Not Allocated"
            print(line)

    def first_fit(bsize, psize):
        block = bsize[:]
        allocation = [-1] * len(psize)
        for i in range(len(psize)):
            for j in range(len(block)):
                if block[j] >= psize[i]:
                    allocation[i] = j
                    block[j] -= psize[i]
                    break
        show("First Fit", psize, allocation)

    def best_fit(bsize, psize):
        block = bsize[:]
        allocation = [-1] * len(psize)
        for i in range(len(psize)):
            best_idx = -1
            for j in range(len(block)):
                if block[j] >= psize[i]:
                    if best_idx == -1 or block[j] < block[best_idx]:
                        best_idx = j
            if best_idx != -1:
                allocation[i] = best_idx
                block[best_idx] -= psize[i]
        show("Best Fit", psize, allocation)

    def worst_fit(bsize, psize):
        block = bsize[:]
        allocation = [-1] * len(psize)
        for i in range(len(psize)):
            worst_idx = -1
            for j in range(len(block)):
                if block[j] >= psize[i]:
                    if worst_idx == -1 or block[j] > block[worst_idx]:
                        worst_idx = j
            if worst_idx != -1:
                allocation[i] = worst_idx
                block[worst_idx] -= psize[i]
        show("Worst Fit", psize, allocation)

    # ---- main part of program 8 ----
    bn = int(input("Enter number of memory blocks: "))
    bsize = list(map(int, input("Enter sizes of blocks: ").split()))[:bn]

    pn = int(input("Enter number of processes: "))
    psize = list(map(int, input("Enter sizes of processes: ").split()))[:pn]

    first_fit(bsize, psize)
    best_fit(bsize, psize)
    worst_fit(bsize, psize)
