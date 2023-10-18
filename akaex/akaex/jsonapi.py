import json
from structure.models import Structure

class School:
    def __init__(self, struct:Structure) -> None:
        self.id = str(struct.id)
        self.name = struct.name
        self.province = struct.province.short_name
        self.municipality = struct.municipality.short_name
        self.address = struct.address
        self.code = struct.code
        self.email = struct.email
        pass
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'province': self.province,
            'municipality': self.municipality,
            'address': self.address,
            'code': self.code,
            'email': self.email,
        }
        
def structure_to_school(structure):
    return School(structure)