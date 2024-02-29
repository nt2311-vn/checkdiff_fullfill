from repl.cli_command import CliCommand
from repl.command_exit import command_exit
from repl.command_checkdata import command_checkdata
from repl.command_start import command_start


def command_help():
    available_commands = getCommands()

    for command in available_commands:
        print(f"    {command} - {available_commands[command].description}")

    print("")


def getCommands():
    return {
        "help": CliCommand("Get the list of all available commands", command_help),
        "checkdata": CliCommand(
            "Check the status of your data in data folder", command_checkdata
        ),
        "start": CliCommand("Start the program to analyze the data", command_start),
        "exit": CliCommand("Exit the program", command_exit),
    }
