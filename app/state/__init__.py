""" """

from abc import ABC, abstractmethod


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def run(self):
        """ """
        ...

    @abstractmethod
    def next(self):
        """ """
        ...

    @abstractmethod
    def prev(self):
        """ """
        ...
