import requests
import json
import sys

#Get the character ID from Name
char_search_call = requests.get('https://api.xivdb.com/search?one=characters&string=' + str(sys.argv[1]) + " " + str(sys.argv[2]))
char_search = char_search_call.json()
char_id = char_search['characters']['results'][0]['id']

#Get character info with ID
char_info_call = requests.get('https://api.xivdb.com/character/' + str(char_id))
char_info = char_info_call.json()

print(str('Name: ') + char_info['name'])
print(str('Server: ') + char_info['server'])
print(str('Last Active: ') + char_info['last_active'])

#Parsing out gearsets, declaring vars for use in loop, gathering data
char_data = char_info['data']
char_gearsets_request = requests.get('https://api.xivdb.com/character/' + str(char_id) + str('?data=gearsets'))
char_gearsets = char_gearsets_request.json()
gearset_dic = char_gearsets[0]
num_gearsets = len(char_gearsets)
gear_gear = (gearset_dic['gear'])

# Parses through gearsets to find raid ready sets 
for i in range(0,num_gearsets - 1):
    gearset_dic = char_gearsets[i]
    gear_gear = (gearset_dic['gear'])
    if gearset_dic['item_level_avg'] >= 300:
        print(gear_gear['slot_mainhand']['data']['classjob_category'])
        print(str('Item Level Avg: ') + str(gearset_dic['item_level_avg']))
        for key in gear_gear:
            if 'slot_' in key:
                print(key + str(': ') + gear_gear[key]['data']['name'] + str(', ') + str(gear_gear[key]['data']['level_item']))
            else:
                continue
