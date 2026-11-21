
import threading 
import time 

def background_task():
    print("Daemon thread started")
    time.sleep(5)
    print("Daemon thread is completed")


thread = threading.Thread(
    target=background_task,
    daemon=True
)

thread.start()

time.sleep(1)

print("Main thread finished")
