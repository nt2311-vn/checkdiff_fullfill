from engine.calculate_differences import calculate_differences
from engine.write_result import write_result
from repl.command_checkdata import command_checkdata


def command_start():
    if not command_checkdata():
        return

    reconcile_table, result_table = calculate_differences()
    write_result(reconcile_table, result_table)

    print("Analyzing completed. Please check the resulls in the result folder.")
    print("Type exit or press Ctrl+C to exit the program.")
    print("")
