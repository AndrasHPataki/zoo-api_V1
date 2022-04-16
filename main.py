from flask import Flask,jsonify,request, json
from schema import animal_data_validator
app = Flask(__name__)

zoo = {"animals": [
    {"name": "Horse", "age": 3},
    {"name": "Zebra", "age": 10},
    {"name": "Elephant", "age": 22}
    ]}



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

@app.get("/see-all")
def see_all():
    return jsonify(zoo['animals'])


@app.post("/create-animal",endpoint='create_animal')
@animal_data_validator
def create_animal():
    new_animal = request.get_json()
    zoo['animals'].append(new_animal)
    animal_name = new_animal.get('name')
    return jsonify({"message": f'Animal {animal_name} Created!'})
   

@app.put("/update-animal/<string:animal_name>",endpoint='update_animal')
@animal_data_validator
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

@app.delete('/delete-animal/<string:animal_name>')
def delete_animal(animal_name):
    for animal in zoo['animals']:
        if animal.get('name') == animal_name:
            zoo['animals'].remove(animal)
            return jsonify({"message": f'Animal {animal_name} deleted!'})
    return jsonify({"message": f'Animal {animal_name} Not found!'})

@app.patch("/partial-update/<string:animal_name>",endpoint='partial_update')
@animal_data_validator
def partial_update(animal_name):
    new_animal = request.get_json()
    for animal in zoo['animals']:
        if animal.get('name') == animal_name:
            animal.update(new_animal)
            return jsonify({"message": f'Animal {animal_name} Partially Updated!'})
    return jsonify({"message": f'Animal {animal_name} Not found!'})

if __name__ == '__main__':
    app.run(debug=True)
