from flask import request, jsonify

class Schema:
  status = {"payload_is_correct": False,
            "name_is_correct":False,
            "age_is_correct": False
           }
  def __init__(self,payload):
    self.payload = payload
    self.name = payload.get('name')
    self.age = payload.get('age')

    res =set(self.payload.keys()).difference(['name','age'])
    if not res and len(payload)<=2:
      self.status['payload_is_correct'] = True
    else: self.status['payload_is_correct'] = False
    if isinstance(self.name,str) and len(self.name) <= 50: 
      self.status['name_is_correct'] = True
    else:self.status['name_is_correct'] = False
    if isinstance(self.age, int) and self.age <= 200:
      self.status['age_is_correct'] = True
    else:self.status['age_is_correct'] = False

  
  def check(self):
    values = self.status.values()
    values = [x for x in values]
    result = all(element == True for element in values)
    if request.method == 'PATCH' and values.count(True)>1: return True
    if result == True: 
      return result
    else: return self.status

def animal_data_validator(func):
    def wrapper(*args, **kwargs):
        data = request.get_json()
        validate_animal = Schema(data).check()
        if validate_animal == True:
            return func(*args, **kwargs)
        else: return jsonify(validate_animal)
    return wrapper
