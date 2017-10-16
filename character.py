import requests
import json
import sys

char_info_call = requests.get('https://api.xivdb.com/character/' + str(sys.argv[1]))
char_info = char_info_call.json()

#print(char_info.keys())
print(str('Name: ') + char_info['name'])
print(str('Server: ') + char_info['server'])
print(str('Last Active: ') + char_info['last_active'])

char_data = char_info['data']

#print(char_data.keys())
char_gearsets_request = requests.get('https://api.xivdb.com/character/' + str(sys.argv[1]) + str('?data=gearsets'))

char_gearsets = char_gearsets_request.json()
gearset_dic = char_gearsets[0]
print(str('Item Level Avg: ') + str(gearset_dic['item_level_avg']))
gear_gear = (gearset_dic['gear'])

#turn this into a for loop to search for gear_gear['slot_*']
for key in gear_gear:
    if 'slot_' in key:
        print(key + str(': ') + gear_gear[key]['data']['name'] + str(', ') + str(gear_gear[key]['data']['level_item']))
    else:
        break
