import abc
from stopwatch import ConsoleStopwatch


# Factory Class
class StopwatchFactory():
    def __init__(self):
        self.stopwatch = self.settings()
        self.general_functions()

    # Template method.
    def general_functions(self):
        self.stopwatch.runtime()
        self.stopwatch.available_user()

    @abc.abstractmethod
    def settings(self):
        pass

    @abc.abstractmethod
    def run_stopwatch(self):
        pass

    @staticmethod
    def get_stopwatch(category: str):
        match category:
            case 'ConsoleStopwatchFactory':
                return ConsoleStopwatchFactory()
            case _:
                raise Exception('Error: missing stopwatch.')
        
        


# Expanded StopwatchFactory Class
class ConsoleStopwatchFactory(StopwatchFactory):
    def settings(self):
        return ConsoleStopwatchSettings()


# Abstract class
class StopwatchGeneralFunctions:
    @abc.abstractmethod
    def runtime(self):
        print("Console stopwatch is running")

    @abc.abstractmethod
    def available_user(self):
        print('No user')


class ConsoleStopwatchSettings(StopwatchGeneralFunctions):
    def runtime(self):
        super().runtime()

    def available_user(self):
        print('user: Youngman')


class ConsoleStopwatchController:
    def run_stopwatch(self):
        ConsoleStopwatch()
        

def main():
    stopwatch_category = 'ConsoleStopwatchFactory'
    StopwatchFactory.get_stopwatch(stopwatch_category)
    ConsoleStopwatchController().run_stopwatch()


if __name__ == '__main__':
    main()
