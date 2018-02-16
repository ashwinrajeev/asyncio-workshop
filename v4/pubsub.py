import asyncio
import aioredis


async def main():
    sub = await aioredis.create_redis(('localhost', 6379))
    res = await sub.subscribe('mychannel')
    ch = res[0]

    while (await ch.wait_message()):
        msg = await ch.get(encoding='utf-8')
        print("Got Message:", msg)



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
