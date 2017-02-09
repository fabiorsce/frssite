import unittest
from django.test import Client
from mr.models import Request, Item
import json

class MakeRequestTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_added_request(self):
        
        response = self.client.get('/mr/food_request/')
        self.assertEqual(response.status_code, 200)
        
        requests_count = len(response.context['food_requests'])
        
        r = Request()
        r.name='AddTest'
        r.total = 10
        r.status = Request.WAITING
        r.save()
        
        
        response = self.client.get('/mr/food_request/')
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(len(response.context['food_requests']), requests_count+1)
        
        
    def test_make_request(self):
        
        
        data = {}
        data['name']='FabioTest'
        data['status']=Request.WAITING
        data['total'] = 20
        items = []
        item = {}
        item['id'] = 1
        item['quantity'] = 2
        items.append(item)
        item['id'] = 2
        item['quantity'] = 3
        items.append(item)
        data['items'] = items 
        
        json_data = json.dumps(data)
        response = self.client.post('/mr/make_request/', json_data,
                content_type='application/json',
                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/mr/food_request/')
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(len(response.context['food_requests']), 1)