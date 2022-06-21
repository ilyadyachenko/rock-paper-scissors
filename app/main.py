from json import JSONDecodeError

import uvicorn
from fastapi import FastAPI, WebSocket
from loguru import logger

from state import State

app = FastAPI()


class Context:

    _state = None

    def __init__(self, state: State):
        self.transition_to(state)

    def transition_to(self, state: State):
        self._state = state
        self._state.context = self

    def run(self):
        self._state.run()

    def next(self):
        self._state.next()

    def prev(self):
        self._state.prev()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """ """
    await websocket.accept()
    while True:
        try:
            json_value = await websocket.receive_json()
        except JSONDecodeError as err:
            logger.exception(err)
            continue

        if 'operation' not in json_value:
            logger.error("request without operation")
            continue

        if json_value['operation'] == 'battle_create':

            await websocket.send_json({'success': True})
            continue

        elif json_value['operation'] == 'battles_list':
            await websocket.send_json({'success': True})
            continue

        elif json_value['operation'] == 'battles_accept':
            await websocket.send_json({'success': True})
            continue

        elif json_value['operation'] == 'battles_start':
            await websocket.send_json({'success': True})
            continue

        elif json_value['operation'] == 'battles_move':
            await websocket.send_json({'success': True})
            continue

        await websocket.send_json({'success': False})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
