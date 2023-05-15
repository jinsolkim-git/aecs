import uuid

class Project:

    def __init__(self, id=None, name=None):
        self.id = id if id else uuid.uuid4()
        self.name = name
        self.location = None
        self.scenes = []
    
    def add_scene(self, scene):
        self.scenes.add(scene)

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    