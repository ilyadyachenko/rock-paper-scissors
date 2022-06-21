""" """
import asyncio


class Server:
    # server

    def __init__(self):
        ...

    def run(self):
        asyncio.get_event_loop().run_until_complete(start_server)

        asyncio.get_event_loop().run_forever()