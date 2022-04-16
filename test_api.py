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
        self.assertEqual(response.json,{"message":"Animal Duck Created!"})
    
    def test_3_update_animal(self):
        data = {"name":"Hen","age":5}
        response = self.client.put('/update-animal/Duck',json=data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json,{"message":"Animal Duck Updated!"})
    
    def test_4_partial_animal_update(self):
        data = {"name":"Hen","age":16}
        response = self.client.patch('/partial-update/Hen',json=data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json,{"message":"Animal Hen Partially Updated!"})

    def test_5_delete_animal(self):
        response = self.client.delete('/delete-animal/Hen')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json,{"message":"Animal Hen deleted!"})
    
    def test_error_statement(self):
        response = self.client.get('/random-url')
        self.assertEqual(response.status_code,404)
    
    def test_fake_data_sent(self):
        data = {"weight":40,"name":"Hiena"}
        response = self.client.post('/create-animal',json=data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json,{'age_is_correct': False, 'name_is_correct': True, 'payload_is_correct': False})

if __name__ == '__main__':
    unittest.main()
