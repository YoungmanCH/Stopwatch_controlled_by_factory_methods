class ConsoleStopwatchConsoleMessages:
    def __init__(self):
        self.start_message()
        self.exit_message()
    
    def start_message(self):
        print('To run the stopwatch, enter "start".')

    def stop_message(self):
        print('To stop the stopwatch, enter "stop".')

    def reset_message(self):
        print('To reset the stopwatch, enter "reset".')
    
    def exit_message(self):
        print('To exit the stopwatch, enter "exit".')

    def exception_message(self):
        print('Please to enter another command.')