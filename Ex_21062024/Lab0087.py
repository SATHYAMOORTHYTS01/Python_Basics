import time  # Import the time module to measure execution time


def note_time_decorator(func):  # Define a decorator function
    def wrapper():  # Define a wrapper function
        start_time = time.time()  # Record the start time
        func()  # Call the original function
        end_time = time.time()  # Record the end time
        print("Time Taken - " + str(end_time - start_time))

    return wrapper()  # Return the wrapper function

@ note_time_decorator
def logs_function():
    time.sleep(5)
    print("print the logs of time taken")
    #########

@ note_time_decorator
def reporting_func():
    time.sleep(2)
    print("print the logs of time taken")

