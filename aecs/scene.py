import uuid

from .component.component_builder import Component
from .entity.entity_builder import Entity
from .system.system_builder import System

class Scene:

    def __init__(self, id=None, name=None):
        self.id = id if id else uuid.uuid4()
        self.name = name
        self.entities = []
        # self.components = []
        # self.systems = []
    
    def add_entity(self, entity):
        self.entities.add(entity)
    
    def create_entity(self, *args):
        entity = Entity()
        for component in args:
            entity.add_component(component)
        self.add_entity(entity)
        


    