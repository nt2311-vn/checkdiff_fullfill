from typing import Callable


class CliCommand:
    def __init__(self, description: str, callback: Callable[[], None]):
        self.description = description
        self.callback = callback
