from time import sleep
from unittest.mock import patch
import requests
import pywhatkit
PATCH = '7.31'
res = requests.get(
    'https://www.dota2.com/datafeed/patchnotes?version='+PATCH).json()
while (res['success'] == False):
    res = requests.get(
        'https://www.dota2.com/datafeed/patchnotes?version='+PATCH).json()
    print(res)
    sleep(5)
if (res['success'] == False):
    pywhatkit.playonyt('crab rave')
