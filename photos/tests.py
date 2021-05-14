from django.test import TestCase
from .models import User, ImageLocation, ImageCategory, Image


# Create your tests here.
class UserTestClass(TestCase):
    """
    User test class that holds all test cases to the User class
    """

    # Set up method
    def setUp(self) -> None:
        self.new_user = User(first_name='Paul', last_name='Ngigi', email='paul@ngigi.com', phone_number='0711111111')

    # Tear down method
    def tearDown(self) -> None:
        User.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(self.new_user, User)

    # Testing saving a user
    def test_save_user(self):
        self.new_user.save_user()
        user_list = User.objects.all()
        self.assertTrue(len(user_list) > 0)

    # Testing saving multiple users
    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User(first_name='Test', last_name='User', email='test@user.com', phone_number='0722222222')
        test_user.save_user()
        user_list = User.objects.all()
        self.assertTrue(len(user_list) > 1)

    # Testing deleting a user
    def test_delete_user(self):
        self.new_user.save_user()
        user_list = User.objects.all()
        self.new_user.delete_user()
        self.assertTrue(len(user_list) < 1)
