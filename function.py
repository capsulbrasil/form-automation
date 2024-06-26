# lib imports
import time

def stopwatch():
    starTime = time.time()
    while True:
        elapsedTime = time.time() - starTime
        formattedTime = time.strftime("%H:%M:%S", time.gmtime(elapsedTime))
        print(f"\r{formattedTime}", end="")
        time.sleep(1)