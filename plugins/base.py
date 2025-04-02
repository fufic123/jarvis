from debug.mixins import DebugMixin


class Plugin(DebugMixin):
    registry = []
    
    _name: str = ""
    _aliases: list = []
    _description: str = ""
    
    def __init__(self):
        super().__init__()
    
    @property
    def name(self):
        return self._name
    
    @property
    def aliases(self):
        return getattr(self, "_aliases", "No aliases provided")
    
    @property
    def description(self):
        return getattr(self, "_description", "No description provided")
         
    async def run(self, args: list) -> str:
        raise NotImplementedError
    

def register_plugin(cls):
    Plugin.registry.append(cls())
    return cls
