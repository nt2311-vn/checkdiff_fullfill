from repl.cli_command import CliCommand
from repl.command_exit import command_exit


def command_help():
    available_commands = getCommands()

    for command in available_commands:
        print(f"    {command} - {available_commands[command].description}")

    print("")


def getCommands():
    return {
        "help": CliCommand("Get the list of all available commands", command_help),
        "checkdata": CliCommand("checkdata", command_checkdata),
        "exit": CliCommand("Exit the program", command_exit),
    }
