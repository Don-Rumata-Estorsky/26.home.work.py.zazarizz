"""
загрузить массив json, каждый цыкл в одельный файл в https
"""

import asyncio
import aiohttp
import os
import json

async def fetch(session,  url):
    async with session.get(url) as response:
        response.raise_for_status()  

        return await response.json()

async def save_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 4 )

async def main(url, directory ):
    os.makedirs(directory, exist_ok = True)

    async with aiohttp.ClientSession() as  session:
        data = await fetch(session, url)

        tasks = []
        for i, item in enumerate(data):
            filename = f"{directory}/file№_{i}.json"
            tasks.append(asyncio.create_task(save_file(item, filename)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    directory = "new_files"
    asyncio.run(main(url, directory))
