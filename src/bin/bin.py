from src.mod_tool import ModTool
from src.service import ModService


class Bin:
    @property
    def service(self):
        return self._service

    def __init__(self, config, *args, **kwargs) -> None:
        tool = ModTool(config)
        self._service = ModService(tool)
