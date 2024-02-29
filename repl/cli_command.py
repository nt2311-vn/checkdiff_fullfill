from typing import Callable
from repl.command_help import command_help
from repl.command_exit import command_exit


class CliCommand:
    def __init__(self, name: str, description: str, callback: Callable[[], None]):
        self.name = name
        self.description = description
        self.callback = callback


def getCommands():
    return {
        "help": CliCommand(
            "help", "Get the list of all available commands", command_help
        ),
        "exit": CliCommand("exit", "Exit the program", command_exit),
    }
