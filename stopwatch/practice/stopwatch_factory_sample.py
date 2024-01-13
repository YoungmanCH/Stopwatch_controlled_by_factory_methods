import abc

# Factory Class
class StopwatchFactory(abc.ABC):
    def __init__(self, stopwatch_cls):
        self.stopwatch = None
        if self.stopwatch_factory_init_rules(stopwatch_cls):
            self.stopwatch = self.general_configs(stopwatch_cls)
        else:
            raise Exception('Error')

    def stopwatch_factory_init_rules(self, stopwatch_cls) -> bool:
        required_methods = {'start', 'stop', 'reset'}
        cls_methods = set(dir(stopwatch_cls))
        return required_methods.issubset(cls_methods)

    # Template method.
    def general_configs(self, stopwatch_cls):
        stopwatch = stopwatch_cls()
        stopwatch.runtime()
        stopwatch.available_user()
        return stopwatch

    # Abstract method.
    def each_configs(self):
        pass


class Stopwatch:
    # Abstract method
    def runtime(self):
        print('No regulations')

    # Abstract method
    def available_user(self):
        print('No user')


# Expanded StopwatchFactory Class
class ConsoleStopwatchFactory(StopwatchFactory):
    def each_configs(self):
        return ConsoleStopwatch()

# #Expanded StopwatchFactory Class
# class WidgetStopwatchFactory(StopwatchFactory):
#     def each_configs(self):
#         return WidgetStopwatch()


class ConsoleStopwatch(Stopwatch):
    def __init__(self):
        self.runtime()
        self.available_user()

    def runtime(self):
        super().runtime()

    def available_user(self):
        return print('Youngman')


if __name__ == '__main__':
    ConsoleStopwatch()
