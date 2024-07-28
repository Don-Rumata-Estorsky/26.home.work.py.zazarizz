"""
загрузить массив json, каждый цыкл в одельный файл in requests
"""
import requests
import json
import os

def main(url, directory):

    os.makedirs(directory, exist_ok = True)
    response = requests.get(url)
    data = response.json()

    for i, item in enumerate(data):
        filename = f"{directory}/file№{i}.json"
        with open(filename, 'w') as f:
            json.dump(item, f,  indent = 4 )

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"  
    directory = "files"  
    main(url, directory)
