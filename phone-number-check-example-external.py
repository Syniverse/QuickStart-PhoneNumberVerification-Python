# phone-number-example.py
# tested in python 3.8.12
# implements phone number verification in Python

# dependencies
# an account on developer.syniverse.com
# create an application using Applications -> new Applications
# enable phone number verification service ^ Gateway Services for the App in the App Settings Option
# copy the access token for the App below.

import requests
from urllib.parse import quote
from urllib.parse import urljoin

number_list = ['+447860438585',
               '+447513005998',
               '+442079202200',
               '+446543211234',
               '+18136375000']

# this is the base url for the phone number verification service, last element in url is
# replaced with the encoded phone number in international format.
# the + needs to be encoded to %2B

base_url = 'https://api.syniverse.com/numberidentity/v3/numbers/[phonenumber]'

access_token = '{YOUR ACCESS TOKEN HERE}'

headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}

for number in number_list:
    # make the url for the lookup including quoting the + correctly)
    url = urljoin(base_url,quote(number))
    response = requests.get(url, headers=headers)
    print ('status code: ' + str(response.status_code))
    print ('response: ' + response.text)
