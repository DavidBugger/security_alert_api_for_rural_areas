import unittest
from app import create_app, db

class RouteTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_alert(self):
        response = self.client.post('/alert', json={
            'description': 'Suspicious activity',
            'latitude': 9.08,
            'longitude': 8.67,
            'timestamp': '2024-10-10T10:00:00'
        })
        self.assertEqual(response.status_code, 201)
    
    def test_get_alerts(self):
        # Add alert first
        self.client.post('/alert', json={
            'description': 'Suspicious activity',
            'latitude': 9.08,
            'longitude': 8.67,
            'timestamp': '2024-10-10T10:00:00'
        })
        response = self.client.get('/alerts?latitude=9.08&longitude=8.67')
        self.assertEqual(response.status_code, 200)
