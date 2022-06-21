""" """

from . import State


class IdleState(State):

    def run(self) -> None:
        ...

    def next(self) -> None:
        ...

    def prev(self) -> None:
        ...
