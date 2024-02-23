# Checking differences between fulfillment and work order creation for each item code in each day

## IMPORTANTS:
The package it self is a tool help you quickly check differences between quantity fulfill with quantity in work order creation.<br>
But it's **YOU** to have responsibilities to download and provide data **CORRECTLY**<br>
Below is two provided link, I already set up in netsuite for the data set of workorder and fulfillment<br>
I suggest using with my dataset if you don't have a well set up search:
- [IF](https://5574610.app.netsuite.com/app/common/search/searchresults.nl?searchid=2243&whence=)
- [WO](https://5574610.app.netsuite.com/app/common/search/searchresults.nl?searchid=2637&whence=)


### Required installs
1. Git
1. Python:
Python with version 3.8+ will be working fine with this package<br>
 *Dependencies:*
 - pandas<br>
 ```sh
    pip install pandas
 ```
 - pyarrow<br>
 ```sh
    pip install pyarrow
 ```
