from engine.calculate_differences import calculate_differences
from engine.write_result import write_result


def command_start():
    try:
        reconcile_table, result_table = calculate_differences()
        write_result(reconcile_table, result_table)

        print("Analyzing completed. Please check the resulls in the result folder.")
        print("Type exit or press Ctrl+C to exit the program.")
        print("")

    except Exception as e:
        print(f"Error at start program {e}")
        print("Type exit or press Ctrl+C to exit the program.")
