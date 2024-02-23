# Checking Differences between Fulfillment and Work order creation for each item code in each day

## Important Information:
The package it self is a tool help you quickly check differences between quantity fulfill with quantity in work order creation.
But it **is your responsibilities** to download and provide data **CORRECTLY**

Below are two links, already set up in Netsuite, for the data set of workorder and fulfillment. I suggest using with my dataset if you don't have a well set up search:
- **IF**: [Item fullfilment dataset](https://5574610.app.netsuite.com/app/common/search/searchresults.nl?searchid=2243&whence=)
- **WO**: [Work order dataset](https://5574610.app.netsuite.com/app/common/search/searchresults.nl?searchid=2637&whence=)

### Required installs
To use this package, you need to install the following:


1. **Git**
1. **Python** (Version 3.8+ is recommended):
 - **Dependencies**:
    - pandas<br>
    ```sh
        pip install pandas
    ```
    - pyarrow<br>
    ```sh
        pip install pyarrow
    ```
