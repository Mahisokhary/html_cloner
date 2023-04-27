import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        x = input(">>")
        async with session.get(x) as response:
            html = await response.text()
            print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())