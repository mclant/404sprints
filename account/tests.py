from django.test import TestCase
from account import models as amod


# Create your tests here.
class AccountTests(TestCase):
    fixtures = [ 'account.yaml' ]

    def test_user_get(self):
        u1 = amod.User.objects.get(id=1)
        # assertEqual just lays it out in a nicer way in the termal, to see which test failed and how it failed etc
        self.assertEqual(u1.first_name, 'mattlantis', msg="Name should have been 'mattlantis'")
        
    def test_user_create(self)
        u = amod.User()
        u.first_name = 'Lloyd'
        u.last_name = 'Christmas'
        u.save()
        u2 = amod.User.objects.get(u.id)
        self.assertEqual(u.first_name, u2.first_name, msg="...")

    def test_user_login(self):
        credentials = {
            'username': 'luke',
            'password': ''
        }

        response = self.client.post('/account/login/', credentials)

        