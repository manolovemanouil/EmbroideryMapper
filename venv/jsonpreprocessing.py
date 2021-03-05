with open('dmc_json.txt', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('},{', '},\n{')

with open('dmc_json.txt', 'w') as file:
    file.write(filedata)