import os


def verify_files():
    num_files = os.listdir("./files/")

    if len(num_files) != 2:
        raise Exception("Required exactly two files: IF and WO in the files folder")

    for file in os.listdir("./files"):
        file_path = os.path.join("./files", file)
        file_type = file_path.split(".")[-1]

        if file_type != "csv":
            raise Exception("File must be in format csv")
