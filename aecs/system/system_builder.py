import uuid

class System:

    def __init__(self, id=None, name=None):
        self.id = id if id else uuid.uuid4()
        self.name = name