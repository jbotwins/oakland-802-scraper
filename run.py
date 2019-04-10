import os
import readline
import re
import json
from bs4 import BeautifulSoup

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(raw_html))
    return cleantext

directory = "www.oaklandnet.com/temp/"

file_list = os.listdir("www.oaklandnet.com/temp")
for filename in file_list:
    if filename.startswith('Default.asp?id'):
        print(filename)
        path = directory + filename
        content = open(path, encoding="ISO-8859-1").read()
        soup = BeautifulSoup(content, 'html.parser')
        divs = soup.select(".w200,.w550")
        better_divs = []
        for div in divs:
            # print(div)
            better = cleanhtml(div)
            better_divs.append(better)
        b = {better_divs[i]: better_divs[i+1]
             for i in range(0, len(better_divs), 2)}
        existing_data = None
        with open("output.json") as data_file:
            existing_data = json.load(data_file)
            existing_data["Entries"].append(b)
        open('output.json', 'w+').write(json.dumps(existing_data))
