from flask import Flask,jsonify,request,json
app = Flask(__name__)

#Zoo is a dict mixed with list, simulating one database
#There only 3 animals registered
zoo = {"animals": [
    {"name": "Horse", "age": 3},
    {"name": "Zebra", "age": 10},
    {"name": "Elephant", "age": 22}
    ]}

#In order to handle HTTP exceptions, like route misstyping, there this function below to return a custom JSON error message
from werkzeug.exceptions import HTTPException
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

#In this first route, all animals are shown
@app.get("/see-all")
def see_all():
    return jsonify(zoo['animals'])

#To create a new animal, just make a post request with Json-data following this schema: {'name':'youranimal_name','age':your_age}
#Remember, this project is very unstable because we dont have any data validator, therefore any information could be sent.
@app.post("/create-animal")
def create_animal():
    new_animal = request.get_json()
    zoo['animals'].append(new_animal)
    animal_name = new_animal.get('name')
    return jsonify({"message": f'Animal {animal_name} Created!'})

#Like the REST concept, the PUT method update ALL information associated in the register (in this case name and age), but need to preserve the index or "id".
#If the information being sought is not found, the put method create a new one.
@app.put("/update-animal/<string:animal_name>")
def update_animal(animal_name):
    new_animal = request.get_json()
    index = -1
    for animal in zoo['animals']:
        index += 1
        if animal.get('name') == animal_name:
            zoo['animals'].remove(animal)
            zoo['animals'].insert(index,new_animal)
            return jsonify({"message": f'Animal {animal_name} Updated!'})
    zoo['animals'].append(new_animal)
    return jsonify({"message": f'Animal {animal_name} Created!'})

#Delete is the most simple, only remove the sought data.  
@app.delete('/delete-animal/<string:animal_name>')
def delete_animal(animal_name):
    for animal in zoo['animals']:
        if animal.get('name') == animal_name:
            zoo['animals'].remove(animal)
            return jsonify({"message": f'Animal {animal_name} deleted!'})
    return jsonify({"message": f'Animal {animal_name} Not found!'})
  
#The Patch method update only specific keys, preserving the rest of data
@app.patch("/partial-update/<string:animal_name>")
def partial_update(animal_name):
    new_animal = request.get_json()
    for animal in zoo['animals']:
        if animal.get('name') == animal_name:
            animal.update(new_animal)
            return jsonify({"message": f'Animal {animal_name} Partially Updated!'})
    return jsonify({"message": f'Animal {animal_name} Not found!'})

if __name__ == '__main__':
    app.run(debug=True)
