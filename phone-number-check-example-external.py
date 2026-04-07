# phone-number-example.py
# tested in python 2.7.12
# New version adpated to work with Python 3
# tested in Python 3.6.1
# implements phone number verification in Python

# dependencies
# an account on developer.syniverse.com
# create an application using Applications -> new Applications
# enable phone number verification service ^ Gateway Services for the App in the App Settings Option
# copy the access token for the App below.

import requests
from urllib.parse import quote
from urllib.parse import urljoin

#Below are MSISDN's samples redacting the last 4 digits 

number_list = ['+1201221XXXX',
               '+1704661XXXX',
               '+1315512XXXX',
               '+1317946XXXX',
               '+1918844XXXX'
			         '+23324469XXXX'
			         '+3579934XXXX'
			         '+3630708XXXX'
			         '+4179643XXXX'
			         '+44748287XXXX']

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
    print ("Response = ", response)
    print ('status code: ' , str(response.status_code))
    print ('response: ' , response.text)
