# Zoo simulation API (Version 1)

The purpose of this project is to build an API that simulates a zoo, using simple development resources.
With each repository released, a new update is made to the project, so that it brings security and stability improvements. (This API is purely developed for educational purposes.)
**Technology being Used: Python With Flask Framework**
## Introduction
A dictionary is responsible for storing the data submitted to the API:

    zoo = {"animals": [
    {"name":"Horse","age":12},
    {"name":"Elephant":"age": 5}
    ]}
The animals key carries a list that contains records about each animal registered in the zoo.  Animals only have 2 attributes: Name and age. Name must be a string, while age an integer.
The API provides 5 accesses:

 - View all animals (GET)
 - Register a new animal (POST)
 - Update an animal completely (PUT)
 - Partially update an animal (PATCH)
 - Remove an animal from the dictionary (DELETE)
 
 *For routes that receive PATCH, PUT and DELETE methods, all of them must have a string as a variable in the endpoint, so that the animal sought is identified.*
## Main Problems
This version of the API is not secure, it does not have any data validation system, nor access control. If any user submits a payload with random data, it will be registered. There is also no persistence of the submitted data. If the server restarts, everything that was done will be lost.
## Tests
The focus of the tests is to verify that the routes are operating normally (absence of errors on the part of the server). A test is also done to verify the application response when a non-existent route is accessed.
## How to use
To view all animals (GET):

    curl http://127.0.0.1:5000/see-all
To register an animal (POST):

    curl -X POST http://127.0.0.1:5000/create-animal
    -H 'Content-Type: application/json'
    -d '{"name":"Duck","age":3}'
   
  To update and animal completely (PUT)

    curl -X PUT http://127.0.0.1:5000/update-animal/Elephant
    -H 'Content-Type: application/json'
    -d '{"name":"Monkey","age":6}'
  To partially update and animal (PATCH)
  
    curl -X PATCH http://127.0.0.1:5000/partial-update/Horse
    -H 'Content-Type: application/json'
    -d '{"age":11}'
To delete and animal (DELETE)

     curl -X DELETE http://127.0.0.1:5000/delete-animal/Horse

