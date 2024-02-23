# Checking Differences between Fulfillment and Work order creation for each item code in each day

## Important Information:
The package it self is a tool help you quickly check differences between quantity fulfill with quantity in work order creation.
But it **is your responsibilities** to download and provide data **CORRECTLY**

Below are two links, already set up in Netsuite, for the data set of workorder and fulfillment. I suggest using my dataset if you don't have a well set up one:
- **IF**: [Item fullfilment dataset](https://5574610.app.netsuite.com/app/common/search/searchresults.nl?searchid=2243&whence=)
- **WO**: [Work order dataset](https://5574610.app.netsuite.com/app/common/search/searchresults.nl?searchid=2637&whence=)

### Required installs
To use this package, you need to install the following:


1. **Git**
    1. **Download the Git Installer**:
        - Go to the [Git website](https://git-scm.com/download/win) to download the Git installer for Windows.

    2. **Run the Installer**:
        - Execute the downloaded `.exe` file and follow the installation wizard. Accept the default settings or customize as per your preferences.

    3. **Verify Installation**:
        - Open Command Prompt and type `git --version` to verify the installation. You should see the installed Git version displayed.


1. **Python** (Version 3.8+ is recommended):
    1. **Visit the Python Download Page**:
        - Go to the [official Python website](https://www.python.org/downloads/) and download the installer for Python 3.8 or later.

    2. **Run the Python Installer**:
        - Open the downloaded file. Ensure you check the box **"Add Python 3.x to PATH"** before clicking on the "Install Now" button.

    3. **Verify Python Installation**:
        - Open Command Prompt or Terminal and type `python --version`. You should see the version of Python you installed.

    #### Installing Dependencies:
    After installing Python, install the required packages using pip:

 - **Dependencies**:
    - **pandas**:
    ```sh
        pip install pandas
    ```
    - **pyarrow**:
    ```sh
        pip install pyarrow
    ```
### Usage guides
1. Clone the repositories to your local machine
    ```sh
    git clone git@github.com:nt2311-vn/checkdiff_fullfill.git
    ```

1. Export two dataset as csv and named IF.csv, WO.csv as their nature. Move to folder **data**

1. Use and command line (cmd) or terminal, make sure your terminal or cmd is at this folder.

Run this command to start the program:

**For Windows**
```sh
python main.py
```

**For MacOS and Linux**
```sh
python3 main.py
```

1. Your result will be in result folder:
    - result_reconcile: Is the total check item differences between fulfill and work order in each date
    - result_diff: Is the work order id need to close for matching between fullfil quantity and work order quantity.
