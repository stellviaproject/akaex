import json
from structure.models import Structure

#serializa un structure en un dict para luego a json
class SchoolJSONSerializer:
    def __init__(self, struct:Structure) -> None:
        #establecer atributos
        self.id = str(struct.id) #id de structure
        self.name = struct.name
        self.address = struct.address
        self.code = struct.code
        self.email = struct.email
        pass
    #retorna el dict
    def to_dict(self):
        return {
            'id': self.id, #id de structure
            'name': self.name,
            'address': self.address,
            'code': self.code,
            'email': self.email,
        }
        
#convierte structure a SchoolJSONSerializer
def structure_to_school(structure):
    return SchoolJSONSerializer(structure)#llamada al constructor

