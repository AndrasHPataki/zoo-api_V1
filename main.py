from flask import Flask,jsonify,request, json
from models import Zoo

app = Flask(__name__)

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
    result = Zoo().see_all()
    return jsonify(result)

@app.post("/create-animal",endpoint='create_animal')
def create_animal():
    result = Zoo().create_animal(request.get_json())
    return jsonify(result)
   
@app.put("/update-animal/<string:animal_name>",endpoint='update_animal')
def update_animal(animal_name):
    result = Zoo().update_animal(request.get_json(),animal_name)
    return jsonify(result)
    
@app.delete('/delete-animal/<string:animal_name>')
def delete_animal(animal_name):
    result = Zoo().delete_animal(animal_name)
    return jsonify(result)

@app.patch("/partial-update/<string:animal_name>",endpoint='partial_update')
def partial_update(animal_name):
    result = Zoo().partial_update(request.get_json(),animal_name)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
