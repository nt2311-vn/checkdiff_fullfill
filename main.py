from verify_files import verify_files
from calculate_differences import calculate_differences


def main():
    try:
        verify_files()

        print("Start analyzing your data ......")

        result_table = calculate_differences()[1]

        print(
            "Analyze data complete, hold result of reconcile data and result differences data...."
        )

        keys = list(result_table.keys())
        print(f"There are {len(keys)} day(s) with difference in fulfill data as below")
        print(result_table)

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")


if __name__ == "__main__":
    main()
