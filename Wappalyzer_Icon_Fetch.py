import glob
import json
import urllib.request

print('\nInitiating Icon Collection from Wappalyzer......')
files = []
for name in glob.glob('C:/Users/IS Lab/Desktop/WASET/technologies/**/*.json', recursive=True):
    files.append(name)
size_of_files = len(files)
print('\nTotal Number of Files to parse\n')
print(size_of_files, 'Total Number of files\n')
print('FILE PATHS', files)
print('******************************\n')

counter = 0
icons_list = []
for doc in files:
    with open(files[counter], 'r', encoding="utf8") as f:
        data = json.load(f)
        key_list = list(data)
        total_keys_in_file = len(key_list) - 1
        for count in range(total_keys_in_file):
            try:
                icons_list.append(data[key_list[count]]['icon'])
                count = count + 1
            except:
                continue
        counter = counter + 1
print(icons_list)
print(len(icons_list))

base_url = 'https://www.wappalyzer.com/images/icons/'
for x in range(len(icons_list)):
    url = base_url + icons_list[x]
    print(url)
    url = url.replace(" ", "%20")
    filename = 'new-ions/' + str(icons_list[x])
    print(filename)
    urllib.request.urlretrieve(url, filename)
