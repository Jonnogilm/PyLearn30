#pip or Preferred installer program is the python default package manager
# numpy is extreamly important for numeric python which is used in finance, machine learning, data science
# it has:
    # a powerful N-dimensional array object
    # sophisticated (broadcasting) functions
    # tools for integrating C/C++ and Fortran code
    # useful linear algebra, Fourier transform, and random number capabilities

# pandas is useful for creating intuitive data structures and data analysis tools

# webbrowser can open URLs
'''import webbrowser

lst_of_urls = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

for url in lst_of_urls:
    webbrowser.open_new_tab(url)'''

# can also uninstall packages using pip-- pip uninstall packagename
# pip show can give you information on a package
# pip show --verbose gives you even more

# pip freeze shows us the packages and their versions used for a specific project
# this is then used alongside a requirements.txt that shows them

# reading from a url or API
# you can read like from a website much like a text file, you just need the correct dependencies
# API - Application programming interface is a means to communicate structured data between two servers typically in the form of json data
# to open the network connection we need a package called requests, help us perform CRUD(create, read, update, delete) operations
import requests
# get(), creates a request obj from the url given
# headers, shows the data in the header 
# status_code, shows the status of the operation
# text, returns text data
# json, returns json data
response = requests.get('https://www.w3.org/International/i18n-drafts/nav/about')
print(response)
print(response.status_code)
print(response.headers)

# a package is a folder with a collection of modules all devided into files, the package gets recognised by the __init__.py
# an empty init.py folder makes all the functions available when the package is imported