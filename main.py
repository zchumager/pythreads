import threading
import time

exit_signal = threading.Event()


def send():
    while not exit_signal.is_set():
        print("Thread ONE")
        time.sleep(5)  # sleeps to leave control lock


def recv():
    while not exit_signal.is_set():
        print("Thread TWO")
        time.sleep(5)  # sleeps to leave control lock


if __name__ == "__main__":
    # threads definition
    a = threading.Thread(target=send)
    b = threading.Thread(target=recv)

    # star the threads
    a.start()
    b.start()

    # create loop in main thread
    try:
        while not exit_signal.is_set():
            time.sleep(0.1)  # main thread sleeps to leave control lock
    except KeyboardInterrupt:  # when ctrl c
        print("Interrupting Threads")
        exit_signal.set()  # send signal to all listening threads

    # resuming threads
    a.join()
    b.join()

    # and you're done...
