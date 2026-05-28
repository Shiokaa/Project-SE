from ecosystem.entity import Entity
from ecosystem.field import Field

class Cell:
    def __init__(self, field: Field, resource: int | None = None, entity: Entity | None = None) -> None:
        self.field = field
        self.resource = resource
        self.entity = entity