import os
from datetime import datetime


def command_checkdata():
    num_files = [f for f in os.listdir("./data/") if f not in [".gitkeep"]]

    if len(num_files) != 2:
        raise Exception("Required exactly two files: IF and WO in the files folder")

    list_filetypes = []
    list_file_created_date = []

    for file in num_files:
        list_filetypes.append(file.split(".")[1])
        timestamp = os.path.getmtime(f"./data/{file}")
        date_time = datetime.fromtimestamp(timestamp)

        list_file_created_date.append(date_time.strftime("%d/%m/%Y %H:%M:%S"))

    if not all([filetype == "csv" for filetype in list_filetypes]):
        raise Exception("Your input in the data folder must be in csv format")

    print("Your data is good to go, type start to begin analyzing data")

    min_date = min(list_file_created_date)
    print(f"Once of your data was downloaded at {min_date}")
    print("")
