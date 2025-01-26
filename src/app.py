#  """
# This module takes care of starting the API Server, Loading the DB and Adding the endpoints
# """

import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200

# estoy obteniendo un miembro de la familia 
@app.route('/member/<int:id>', methods=['GET']) 
def obtener_solo_miembro(id):
   member, status_code = jackson_family.get_member(id)
   return jsonify(member), status_code

# estoy creando un nuevo miembro: siempre en el método post hay que capturarf la respuesta del cliente en en formato json
@app.route('/member', methods=['POST'])
def crear_miembro():
    body = request.get_json(silent=True)
    if body is None: 
        return jsonify({"msg":"debes enviar informacion en el body"}), 400 
    if "first_name" not in body: 
       return jsonify({"msg":"first name es obligatorio"}), 400 
    new_member = {
        "fisrt_name": body["first_name"],
        "last_name": jackson_family.last_name,
        "age": body["age"],
        "lucky_numbers": body["lucky_numbers"],
    }
    if "id" in body:
        new_member["id"] = body["id"]
    new_member = jackson_family.add_member(new_member)
    return jsonify({"msg":"familiar agregado"}), 200

    # member = request.json
    # print("miembro añadido", member)
    # #simepre la integracion en un metodo post hay qe gurdarla 
    # jackson_family.add_member(member)
    # return jsonify({"done":"familiar agregado"}), 200 
    
@app.route('/member/<int:member_id>', methods=['DELETE'])
def borrar_miembro(member_id): 
    print(member_id) 
    response, status_code = jackson_family.delete_member(member_id) 
    return jsonify(response), status_code 
       





# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
