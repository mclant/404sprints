from django.test import TestCase
from account import models as amod
from django.contrib.auth import models as pmod
from datetime import datetime

# Create your tests here.
class AccountTests(TestCase):
    fixtures = [ 'account.yaml' ]

    def setUp(self):
        self.matt = amod.User()
        self.matt.username = 'matthew'
        self.matt.set_password('letmein')
        self.matt.first_name = 'Matt'
        self.matt.last_name = 'Lantis'
        self.matt.birthdate = datetime(2000,1,1)
        self.matt.save()
    
    def test_user_login(self):
        credentials = {
            'username': 'matthew',
            'password': 'letmein',
        }
        response = self.client.post('/account/login/', credentials)
        request = response.wsgi_request

        self.assertTrue(request.user.is_authenticated, msg="User should have been authenticated")
        self.assertEqual(request.user.id, self.matt.id, msg="User should have been matt")
        self.assertEqual(response.status_code, 302, msg="User wasnt redirected")
        response = self.client.get('/account/logout')
        request = response.wsgi_request
        self.assertEqual(response.status_code, 302, msg="User wasn't logged out")
        self.assertFalse(request.user.is_authenticated, msg="User should not be authenticated")

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
    

    def test_group_permissions(self):
        u1 = amod.User.objects.get(id=1)
        p1 = pmod.Permission.objects.get(codename = 'change_user')
        g1 = pmod.Group(name="Dope")
        g1.save()
        g1.permissions.add(p1.id)
        g1.save()
        u1.groups.add(g1.id)
        u1.save()
        self.assertTrue(u1.has_perm(22), msg='User should have the add user permission')


    def test_change_password(self):
        u1 = amod.User.objects.get(id=1)
        pswd = u1.password
        u1.set_password('new password')
        u1.save()
        self.assertNotEqual(u1.password, pswd, msg="Password should be new password")


    def test_users_and_groups(self):
        g1 = pmod.Group(name="my_group")
        g1.save()
        u1 = amod.User.objects.get(id=1)
        u1.groups.add(g1.id)
        u1.save()
        self.assertTrue(u1.groups.filter(name = g1.name).exists(), msg = "User should be in my group")





