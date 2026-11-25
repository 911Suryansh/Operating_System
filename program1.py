# PROGRAM 1
# Introduction to Linux System Calls, Process Creation using
# fork(), exec() and wait()
def program1():
    print("Parent process: PID =", os.getpid())
    sys.stdout.flush()  # flush before fork so output is not duplicated

    try:
        pid = os.fork()
    except OSError as e:
        print("fork failed:", e)
        return

    if pid == 0:
        # Child process
        print(f"Child process: PID = {os.getpid()}, Parent PID = {os.getppid()}")
        print("Child is about to exec 'ls -l'")
        sys.stdout.flush()
        try:
            os.execvp("ls", ["ls", "-l"])
        except OSError as e:
            # exec only returns on error
            print("exec failed:", e)
            os._exit(1)
    else:
        # Parent process
        print(f"Parent waiting for child (PID = {pid}) to finish...")
        sys.stdout.flush()
        _, status = os.wait()
        if os.WIFEXITED(status):
            print("Child exited with status", os.WEXITSTATUS(status))
        print("Parent process resumes and exits.")
