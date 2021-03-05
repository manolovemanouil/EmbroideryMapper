import json
import re



class DMC():
    def __init__(self, dmc_code, name, red, green, blue, rgb):
        self.dmc_code = dmc_code
        self.name= name
        self.red = red
        self.green = green
        self.blue = blue
        self.rgb = rgb


def data_to_DMC(rows_str):

    lines = rows_str.split('\n')

    m = re.search('>(.+?)<\/TD>', lines[1])
    dmc_code = 0

    if m:
        dmc_code = m.group(1)

    m = re.search('<a.*>(.*)<\/a>', lines[2])
    name = ''

    if m:
        name = m.group(1)

    m = re.search('>(.+?)<\/TD>', lines[3])
    red = 0

    if m:
        red = m.group(1)

    m = re.search('>(.+?)<\/TD>', lines[4])
    green = 0

    if m:
        green = m.group(1)

    m = re.search('>(.+?)<\/TD>', lines[5])
    blue = 0

    if m:
        blue = m.group(1)

    m = re.search('>(.+?)<\/TD>', lines[6])
    rgb = ''

    if m:
        rgb = m.group(1)

    return DMC(dmc_code, name, red, green, blue, rgb)

dmc_arr = []

f = open('C:\\Users\\manol\\Documents\\DMC_table.txt', 'r')

while True:

    l = f.readline()

    if not l:
        break

    m = re.search('<TR>', l)

    if m:

        block = ''

        for i in range(0,7):
            block = block + f.readline()

        dmc_arr.append(data_to_DMC(block))

f.close()

with open('dmc_json.txt', 'w') as outfile:

    for element in dmc_arr:
        json.dump(element.__dict__, outfile)