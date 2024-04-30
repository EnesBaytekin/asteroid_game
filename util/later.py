from _thread import start_new_thread
from time import sleep

def do_it_later(function, args, duration):
    """Call the 'function' with the 'args' after 'duration' seconds."""
    def wait_function():
        sleep(duration)
        function(*args)
    start_new_thread(wait_function, ())
