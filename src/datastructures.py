
# """
# update this file to implement the following already declared methods:
# - add_member: Should add a member to the self._members list
# - delete_member: Should delete a member from the self._members list
# - update_member: Should update a member from the self._members list
# - get_member: Should return a member from the self._members list
# """

from random import randint

class FamilyStructure:
    
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # example list of members
        self._members = [ {
            "id": self._generateId(),
            "first_name": "Antuan",
            "last_name": self.last_name,
            "age": 29,
            "lucky_numbers": [5, 13, 22],
        },

        {
            "id": self._generateId(),
            "first_name": "Lucy",
            "last_name": self.last_name,
            "age": 20,
            "lucky_numbers": [7, 14, 32],
        },

        {
            "id" : self._generateId(),
            "first_name": "Carlos",
            "last_name": self.last_name,
            "age": 40,
            "lucky_numbers": [1, 100, 56],
        },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # me estoy asegurando que el apellido del nuevo miembro sea el mismo que el de la familia 
        # member["last_name"] = self.last_name
        
        # # de esta forma agrego un ID a un miembro llamando al metodo encargado de asignar el id
        # member['id'] = self._generate_id()

        # # 
        # member["lucky_numbers"] = list(member.get("lucky_numbers", set()))
        if not member.get("id"): 
            member["id"]= self._generateId()

        # añado el miembro a la lista de miembros
        self._members.append(member)

        return member 

    def delete_member(self, id):
        # estoy recorriendo la lista de miembros utilizando enel lugar que estan
        for member in self._members: 
            # sw comprueba si el id del miembro actual es igual al id que queremos eliminar.
            if member["id"] == id:
                #se elimina de la lista el mimbro indicsdo
                self._members.remove(member)

                return {"message": f"El miembro con id {id} ya no forma parte de la familia"}, 200
            
        return {"message": f"No se elimino el miembro de la familia con {id}"}, 404

    def get_member(self, id):
        #Revisa a todos los miembros de la lista 
        for member in self._members:
            #comprueba si el id del miembro selecionado coincide con el id que se le dio como argumento
            if member["id"] == int(id):
                # me devuelve el miembro econtrado 
                return {"message": f"Se ha encontrado el miembro de la familia con el  id {id}"}, 200
            
        return {"message": f"No se encontró el miembro de la familia con {id}"}, 404
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
