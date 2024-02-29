from repl.cli_command import getCommands


def command_help():
    available_commands = getCommands()

    for command in available_commands:
        print(f"{command} - {available_commands[command].description}")
