import requests
import json
import sys


char_info_call = requests.get('https://api.xivdb.com/character/' + str(sys.argv[1]))
char_info = char_info_call.json()

#char_json = char_info.json()
print(char_info.keys())
print(char_info('name'))
