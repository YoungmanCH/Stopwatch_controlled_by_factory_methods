from actions import ConsoleStopwatchActions


class ConsoleStopwatch:
    def __init__(self):
        actiions = ConsoleStopwatchActions()
        while True:
            command = input("Enter command: ")
            if self.validation(command):
                if self.action_regulations(actiions):
                    actiions.run_stopwatch(command)
                    break

    def validation(self, command):
        valid_commands = ["start", "stop", "reset", "exit"]
        if command not in valid_commands:
            print("Invalid command.")
            return False
        return True

    def action_regulations(self, actions):
        required_methods = {'start', 'stop', 'reset'}
        class_methods = set(dir(actions))
        return required_methods.issubset(class_methods)


def main():
    ConsoleStopwatch()


if __name__ == '__main__':
    main()
