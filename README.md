# DATAESG
# Dataesg Python
This is the official documentation for Dataesg’s Python Package. This package is compatible with python v3+.
### Installation
To complete the installation of Dataesg’s Python Package, execute either of the following pip commands from terminal:
```sh
$ pip install dataesg
$ pip3 install dataesg
```
### API Configurations
Please use the provided API keys to be able to access our services.
Example API Key: 32e6f6c4-33b1-4156-8ae6-8t92e7ab66cc
### Using Python to retrieve ESG data
```sh
$ import dataesg
$ dataesg.connect(‘32e6f6c4-33b1-4156-8ae6-8t92e7ab66cc’)
$ dataesg.get_sample(metric=[‘Scope_1’,‘Scope_2’],return_type=‘pandas’)
$ dataesg.get_by_ticker(ticker=‘MMM’,return_type=‘pandas’)
$ dataesg.get_by_isin(isin=[‘US88579Y1010’,’SE0000103814’],return_type=‘pandas’)
$ dataesg.get_by_cusip(cusip=‘88579Y101’,return_type=‘numpy’)
$ dataesg.get_by_sedol(sedol=‘2595708’,return_type=‘numpy’)
```
## Parameters
```sh
$ metrics - string or list of strings (default: returns all metrics)
$ return_type - either ‘pandas’ or ’numpy’ (default: ‘pandas’)
$ api_key - If not connected previously
```
## License
----
[MIT License](http://opensource.org/licenses/MIT)
