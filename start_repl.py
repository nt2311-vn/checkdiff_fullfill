import os


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
