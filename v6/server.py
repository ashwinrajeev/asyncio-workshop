import asyncio
import websockets
import aioredis


async def producer_handler(websocket, room):

    pass

async def consumer_handler(websocket, room):
    # TODO : read message from redis
    pass


async def handler(websocket, path):
    room = await websocket.recv()
    consumer_task = asyncio.ensure_future(consumer_handler(websocket, room))
    producer_task = asyncio.ensure_future(producer_handler(websocket, room))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )

start_server = websockets.serve(handler, 'localhost', 9998)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
