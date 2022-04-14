from flask_testing import TestCase
import unittest
import flask_testing
from main import app,zoo
class MyTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_1_see_all_endpoint(self):
        response = self.client.get('/see-all')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json,zoo['animals'])
    
    def test_2_create_animal(self):
        data = {"name":"Duck","age":5}
        response = self.client.post('/create-animal',json=data)
        self.assertEqual(response.status_code, 200)
    
    def test_3_update_animal(self):
        data = {"name":"Hen","age":5}
        response = self.client.put('/update-animal/Duck',json=data)
        self.assertEqual(response.status_code,200)
    
    def test_4_partial_animal_update(self):
        data = {"name":"Hen","age":16}
        response = self.client.patch('/partial-update/Hen',json=data)
        self.assertEqual(response.status_code,200)
        
    def test_5_delete_animal(self):
        response = self.client.delete('/delete-animal/Hen')
        self.assertEqual(response.status_code,200)
    
    def test_error_statement(self):
        response = self.client.get('/random-url')
        self.assertEqual(response.status_code,404)

if __name__ == '__main__':
    unittest.main()
