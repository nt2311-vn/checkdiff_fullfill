import os


def verify_files():
    num_files = [f for f in os.listdir("./data/") if f not in [".gitkeep"]]

    if len(num_files) != 2:
        raise Exception("Required exactly two files: IF and WO in the files folder")

    for file in num_files:
        file_type = file.split(".")[-1]
        file_name = file.split(".")[0]

        if file_name.upper() != "IF" and file_name.upper() != "WO":
            raise Exception(
                "File name convention error, you must named the file IF and WO respectively for the fulfill and workorder data"
            )

        if file_type != "csv":
            raise Exception("File must be in format csv")
