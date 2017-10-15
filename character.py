import requests
import json
import sys


char_info_call = requests.get('https://api.xivdb.com/character/' + str(sys.argv[1]))
char_info = char_info_call.json()

print(char_info.keys())
print(str('Name: ') + char_info['name'])
print(str('Server: ') + char_info['server'])
print(str('Last Active: ') + char_info['last_active'])

char_data = char_info['data']

print(char_data.keys())
