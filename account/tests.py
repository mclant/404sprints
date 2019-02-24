from django.test import TestCase
from account import models as amod
from datetime import datetime
from lxml import etree

# Create your tests here.
class AccountTests(TestCase):
    fixtures = [ 'account.yaml' ]

    def setUp(self):
        self.matt = amod.User.objects.get(username='matt')
        self.matt.set_password('letmein')
        self.matt.save()
    
    def test_user_login(self):
        credentials = {
            'username': 'matthew',
            'password': 'test101',
        }
        response = self.client.post('/account/login', credentials)
        request = response.wsgi_request

        self.assertTrue(request.user.is_authenticated, msg="User should have been authenticated")
        self.assertEqual(request.user.id, self.matt.id, msg="User should have been matt")
        self.assertEqual(response.status_code, 302, msg="User wasnt redirected")

    def test_user_get(self):
        u1 = amod.User.objects.get(id=1)
        # assertEqual just lays it out in a nicer way in the termal, to see which test failed and how it failed etc
        self.assertEqual(u1.first_name, 'mattlantis', msg="Name should have been 'mattlantis'")
        
    def test_user_create(self):
        u = amod.User()
        u.first_name = 'Lloyd'
        u.last_name = 'Christmas'
        u.username = 'dummer'
        u.save()
        u2 = amod.User.objects.get(username='dummer')
        self.assertEqual(u.first_name, u2.first_name, msg="Names should be the same")

        