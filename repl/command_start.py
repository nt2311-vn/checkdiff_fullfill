from engine.calculate_differences import calculate_differences
from engine.write_result import write_result


def command_start():
    reconcile_table, result_table = calculate_differences()
    write_result(reconcile_table, result_table)

    print("Analyzing completed. Please check the resulls in the result folder.")
    print("")