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

 - **Dependencies**:
    - pandas<br>
    ```sh
        pip install pandas
    ```
    - pyarrow<br>
    ```sh
        pip install pyarrow
    ```
