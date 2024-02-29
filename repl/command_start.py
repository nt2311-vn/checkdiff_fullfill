from engine.calculate_differences import calculate_differences
from engine.write_results import write_results


def command_start():
    reconcile_table, result_table = calculate_differences()
    write_results(reconcile_table, result_table)

    print("Analyzing completed. Please check the resulls in the result folder.")
    print("")
