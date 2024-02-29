import os
from typing import Callable


class CliCommand:
    def __init__(self, name: str, description: str, callback: Callable[[], None]):
        self.name = name
        self.description = description
        self.callback = callback


def start_repl():
    print(
        """
(c) Copy right nt2311-vn
    All right reserved.
    Welcome to the check diff fulfillment program. Type ? or help to list commands"""
    )
    while True:
        user_input = input("> ")

        if not user_input:
            continue

        command = cleanInput(user_input)[0]


def getCommands():
    return {
        "help": CliCommand(
            "help", "Get the list of all available commands", command_help
        ),
        "exit": CliCommand("exit", "Exit the program", command_exit),
    }


def cleanInput(input: str) -> list[str]:
    words = input.lower().split(" ")
    return words


def command_exit():
    os._exit(0)
