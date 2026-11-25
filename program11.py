# PROGRAM 11
# File Allocation Methods - Contiguous, Linked and Indexed Allocation

def program11():
    MAXBLOCKS = 30

    def contiguous_allocation():
        disk = [0] * MAXBLOCKS  # 0 = free, 1 = allocated
        print("\n--- Contiguous Allocation ---")
        nf = int(input("Enter number of files: "))

        for f in range(nf):
            start, length = map(int, input(f"File {f + 1} - starting block, length: ").split())

            ok = True
            for i in range(start, start + length):
                if i >= MAXBLOCKS or disk[i] == 1:
                    ok = False
                    break

            if not ok:
                print("Allocation failed: blocks not free/out of range.")
                continue
            for i in range(start, start + length):
                disk[i] = 1
            print(f"File {f + 1} allocated blocks {start} to {start + length - 1}")

    def linked_allocation():
        disk = [0] * MAXBLOCKS
        print("\n--- Linked Allocation ---")
        nf = int(input("Enter number of files: "))

        for f in range(nf):
            length = int(input(f"File {f + 1} - number of blocks: "))
            blocks = []
            for i in range(MAXBLOCKS):
                if len(blocks) >= length:
                    break
                if disk[i] == 0:
                    disk[i] = 1
                    blocks.append(i)

            print(f"File {f + 1} allocated blocks: " + " -> ".join(map(str, blocks)) + " -> (NULL)")
            if len(blocks) < length:
                print("Warning: disk full, could not allocate all blocks.")

    def indexed_allocation():
        disk = [0] * MAXBLOCKS
        print("\n--- Indexed Allocation ---")
        nf = int(input("Enter number of files: "))

        for f in range(nf):
            length = int(input(f"File {f + 1} - number of data blocks needed: "))

            index_block = -1
            for i in range(MAXBLOCKS):
                if disk[i] == 0:
                    index_block = i
                    disk[i] = 1
                    break

            blocks = []
            for i in range(MAXBLOCKS):
                if len(blocks) >= length:
                    break
                if disk[i] == 0:
                    disk[i] = 1
                    blocks.append(i)

            print(f"File {f + 1} - Index block: {index_block}, Data blocks: "
                  + " ".join(map(str, blocks)))

    # ---- main part of program 11 ----
    print("Menu:\n1. Contiguous Allocation\n2. Linked Allocation")
    choice = int(input("3. Indexed Allocation\nEnter choice: "))

    if choice == 1:
        contiguous_allocation()
    elif choice == 2:
        linked_allocation()
    elif choice == 3:
        indexed_allocation()
    else:
        print("Invalid choice")
