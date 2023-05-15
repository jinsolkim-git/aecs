import uuid

class Entity:

    def __init__(self, id=None, name=None):
        self.id = id if id else uuid.uuid4()
        self.name = name
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)

    