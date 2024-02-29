from repl.command_help import getCommands


def start_repl():
    print(
        """
(c) Copy right nt2311-vn
    All right reserved.
    Welcome to the check diff fulfillment program. Type help to list commands"""
    )
    while True:
        user_input = input("> ")

        if not user_input:
            continue

        available_commands = getCommands()

        command = cleanInput(user_input)[0]

        if command not in available_commands:
            print(
                f"{command} is an invalid command, type help to see the availale lists"
            )
            continue

        available_commands[command].callback()


def cleanInput(input: str) -> list[str]:
    words = input.lower().split(" ")
    return words
