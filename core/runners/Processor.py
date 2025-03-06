from typing import Any, Self

from core.helpers.Logger import Logger
from core.runners.BaseRunner import BaseRunner


class Processor(BaseRunner):

    def setup(self): ...

    def run(self) -> Self:
        Logger.get().warning("Processor.run() not implemented.")
        return self
        # raise NotImplementedError

    def get_data(self) -> Any: ...
