class Plugin:
    _name: str = ""
    _aliases: list = []
    registry = []

    
    @property
    def name(self):
        return self._name
    
    @property
    def aliases(self):
        return self._aliases
    
    def run(self) -> str:
        raise NotImplementedError
    

def register_plugin(cls):
    Plugin.registry.append(cls())
    return cls
