import os


class CliCommand(object):
    def __init__(self, name, description, callback):
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
        else:
            os._exit(0)


def getCommands():
    return {
        "help": CliCommand(
            "help", "Get the list of all available commands", command_help
        )
    }
