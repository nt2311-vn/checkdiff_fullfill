import time
from engine.verify_files import verify_files
from engine.calculate_differences import calculate_differences
from engine.write_result import write_result
from repl.start_repl import start_repl


def main():
    while True:
        start_repl()

    try:
        verify_files()

        print("Start analyzing your data ......")

        reconcile_data, result_data = calculate_differences()

        print(
            "Analyze data complete, hold result of reconcile data and result differences data...."
        )
        keys = list(result_data.keys())
        print(f"There are {len(keys)} day(s) with differences in fulfillment")
        print("Writing result to result folder")

        time.sleep(0.5)
        write_result(reconcile_data, result_data)

        time.sleep(1)
        print("Writing reconcile data complete")

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")


if __name__ == "__main__":
    main()
