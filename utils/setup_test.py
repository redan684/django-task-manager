from django.test import TestCase
from authentication.models import User
from faker import Faker



class TestSetup(TestCase):

    def setUp(self):

        self.faker= Faker()
        self.password = self.faker.paragraph(nb_sentences=5)
        print(self.faker.name())
        print(self.faker.email())
        self.user = {
            "username": self.faker.name().split(" ")[0],
            "email": self.faker.email(),
            "password": self.password,
            "password2": self.password,
        }

        self.user_short_password={
            'email':'testemail@gmail.com',
            'username':'username',
            'password':'tes',
            'password2':'tes',

        }
        self.user_unmatching_password={

            'email':'testemail@gmail.com',
            'username':'username',
            'password':'teslatt',
            'password2':'teslatto',

        }

        self.user_invalid_email={
            
            'email':'test.com',
            'username':'username',
            'password':'teslatto',
            'password2':'teslatto',

        }
        self.user_no_username={
            
            'email':'test.com',
            'username':'',
            'password':'teslatto',
            'password2':'teslatto',
            'name':'fullname'
        }

        

    def create_test_user(self):
        
        user = User.objects.create_user(username='username',email='email@app.com')
        user.set_password('password12!')
        user.save()

        return user

        

    def create_test_user(self):
        user = User.objects.create_user(
            username='username', email='email@app.com')
        user.set_password('password12!')
        user.is_email_verified = True
        user.save()
        return user

   
    def tearDown(self):

        return super().tearDown()
