import os
from datetime import datetime
from repl.command_start import command_start


def command_checkdata():
    num_files = [f for f in os.listdir("./data/") if f not in [".gitkeep"]]

    if len(num_files) != 2:
        print("Required exactly two files: IF and WO in the data folder")
        print("Please download the data and type start to begin the program")
        print(
            "For IF: https://5574610.app.netsuite.com/app/common/search/searchresults.nl?searchid=2243&whence="
        )
        print(
            "For WO: https://5574610.app.netsuite.com/app/common/search/searchresults.nl?searchid=2637&whence="
        )
        print("To exit the program. Type exit or press Ctrl + C")
        return

    list_filetypes = []
    list_file_created_date = []
    list_file_name = []

    for file in num_files:
        list_filetypes.append(file.split(".")[1])
        list_file_name.append(file.split(".")[0])
        timestamp = os.path.getmtime(f"./data/{file}")
        date_time = datetime.fromtimestamp(timestamp)

        list_file_created_date.append(date_time)

    if not all([filetype == "csv" for filetype in list_filetypes]):
        print("Your input in the data folder must be in csv format")
        return

    if not all([file_name in ["IF", "WO"] for file_name in list_file_name]):
        print("Your data must be name IF and WO for name convention")
        return

    # If min_date is not to day print to awareness
    min_date = min(list_file_created_date)
    if min_date.strftime("%Y-%m-%d") != datetime.now().strftime("%Y-%m-%d"):
        print(
            f"WARNING: One of your data files was downloaded on {min_date.strftime('%d/%m/%Y %H:%M:%S')}, please download a new one using the link below:"
        )
        print(
            "For IF: https://5574610.app.netsuite.com/app/common/search/searchresults.nl?searchid=2243&whence="
        )
        print(
            "For WO: https://5574610.app.netsuite.com/app/common/search/searchresults.nl?searchid=2637&whence="
        )

        user_input = input("If you want continue with the current data type (Y) Yes: ")

        if user_input.lower() in ["yes", "y"]:
            command_start()

        else:
            return

    else:
        print("Your data is good to go, type start to begin analyzing data")
        user_input = input("Type (Y) to start the program: ")

        if user_input.lower() in ["yes", "y"]:
            command_start()
        else:
            return
