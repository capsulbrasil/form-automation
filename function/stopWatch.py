import time

def stopWatch():
    '''
    Stopwatch function that displays the execution time.

    The `stopWatch` function starts a stopwatch and displays the elapsed time since the start of the execution.
    The time is displayed in HH:MM:SS format and is updated every second.

    Notes:
    ------
    - The function enters an infinite loop, so it needs to be manually stopped to stop the execution.
    - Use Ctrl+C in the terminal to stop the execution.
    '''
    starTime = time.time()  # Capture the initial time
    while True:
        elapsedTime = time.time() - starTime  # Calculates elapsed time
        formattedTime = time.strftime("%H:%M:%S", time.gmtime(elapsedTime))  # Formats elapsed time
        print(f"\r Runtime {formattedTime}", end="")  # Displays elapsed time in the terminal
        time.sleep(1)  # Wait 1 second before refreshing again
