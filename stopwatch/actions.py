import time

from messages import ConsoleStopwatchConsoleMessages


class ConsoleStopwatchActions:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.stopJudge = True
        self.stopwatch = ConsoleStopwatchConsoleMessages()

    def start(self):
        if self.stopJudge:
            self.start_time = time.time()
            self.stopJudge = False

    def stop(self):
        if not self.stopJudge:
            self.elapsed_time += time.time() - self.start_time
            self.stopJudge = True
            self.start_time = None

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.stopJudge = True

    def get_elapsed_time(self):
        if self.start_time is None:
            print(f"Elapsed time: {self.elapsed_time} seconds")
            return self.elapsed_time
        else:
            return self.elapsed_time + time.time() - self.start_time

    def run_stopwatch(self, command):
        while True:
            if command == "start":
                self.start()
                self.stopwatch.stop_message()

                command = input("Enter command: ")
            elif command == "stop":
                self.stop()
                self.get_elapsed_time()
                self.stopwatch.start_message()
                self.stopwatch.reset_message()
                self.stopwatch.exit_message()

                command = input("Enter command: ")
            elif command == "reset":
                self.reset()
                self.stopwatch.start_message()

                command = input("Enter command: ")
            elif command == "start":
                self.start()
                self.stopwatch.start_message()

                command = input("Enter command: ")
            elif command == "exit":
                break
            else:
                self.stopwatch.exception_message()
                command = input("Enter command: ")
