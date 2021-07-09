# from utils.setup_test import TestSetup
from todo.models import Todo
from utils.setup_test import TestSetup


class TestModel(TestSetup):

    def test_should_create_user(self):


        user = self.create_test_user()
        todo=Todo(owner=user, title='Buy milk', description= 'get it done')

        todo.save()

        self.assertEqual(str(todo), 'Buy milk')