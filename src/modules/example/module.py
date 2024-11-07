# builtin

# external

# internal
from src.globals.environment import Environment


class ExampleModule:
    def __init__(self, environment: Environment):
        self.environment = environment

    def example_function(self):
        return "Hello, World!"
