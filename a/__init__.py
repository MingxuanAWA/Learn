import json
import asyncio
import httpx
async def fetch():


    async with         httpx.AsyncClient() as c:
        r= await c.get(        "https://httpbin.com/get")
        return r.json()  
if __name__ == "__main__":
    print(asyncio.run(fetch()))
