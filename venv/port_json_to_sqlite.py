import sqlite3
from color_selections import DMC
import json

conn = sqlite3.connect('dmc.db')
c = conn.cursor()

with open('dmc_json.json') as json_file:
    data = json.load(json_file)

    for entry in data:

        dmc_code = entry['dmc_code']
        name = entry['name']
        red = int(entry['red'])
        green = int(entry['green'])
        blue = int(entry['blue'])
        rgb = entry['rgb']

        query = "INSERT OR IGNORE INTO threads VALUES ('{dmc_code}','{name}',{red},{green},{blue},'{rgb}')".format(dmc_code=dmc_code,name=name,red=red,green=green,blue=blue,rgb=rgb)

        c.execute(query)

        conn.commit()



conn.close()