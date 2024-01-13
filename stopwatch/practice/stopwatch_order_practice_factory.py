import abc
from console_stopwatch.stopwatch import ConsoleStopwatch

# Factory Class
class StopwatchFactory():
    def __init__(self):
        print('5')
        self.stopwatch = self.settings()
        print('8')
        self.general_functions()

    # Template method.
    def general_functions(self):
        print('9')
        self.stopwatch.runtime()
        self.stopwatch.available_user()

    @abc.abstractmethod
    def settings(self):
        pass

    print('1')


# Expanded StopwatchFactory Class
class ConsoleStopwatchFactory(StopwatchFactory):
    print('2')

    # Return ConsoleStopwatchController() to self.stopwatch()
    def settings(self):
        print('6')
        return ConsoleStopwatchController()


class StopwatchGeneralFunctions:

    def __init__(self):
        print('7')

    @abc.abstractmethod
    def runtime(self):
        print('11')
        print("Console stopwatch is running")

    @abc.abstractmethod
    def available_user(self):
        print('No user')

    print('3')


class ConsoleStopwatchController(StopwatchGeneralFunctions):
    print('4')

    # 5
    def runtime(self):
        print('10')
        super().runtime()

    # 7
    def available_user(self):
        print('12')
        print('user: Youngman')

    # 8
    def run_stopwatch(self):
        ConsoleStopwatch()


if __name__ == '__main__':
    ConsoleStopwatchFactory()
