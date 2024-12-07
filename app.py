from aiohttp.client import ClientSession
import asyncio


async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
        

async def main():
    cont = await fetch('https://jsonplaceholder.typicode.com/')
    print(cont)


if __name__ == "__main__":
    asyncio.run(main())