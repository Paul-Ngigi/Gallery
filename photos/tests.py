from django.test import TestCase
from .models import User, ImageLocation, ImageCategory, Image


# Create your tests here.
class UserTestClass(TestCase):
    """
    User test class that holds all test cases for the User class
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


class ImageCategoryTestClass(TestCase):
    """
    Test case class that runs test cases for the ImageCategory class
    """

    # set up method
    def setUp(self) -> None:
        self.new_image_category = ImageCategory(name='Travel')

    # tear down method
    def tearDown(self) -> None:
        ImageCategory.objects.all().delete()

    # testing instance
    def test_instance(self):
        self.assertTrue(self.new_image_category, ImageCategory)

    # testing saving image category
    def test_save_image_category(self):
        self.new_image_category.save_category()
        category_list = ImageCategory.objects.all()
        self.assertTrue(len(category_list) > 0)

    # testing saving multiple image categories
    def test_save_multiple_image_categories(self):
        self.new_image_category.save_category()
        new_category = ImageCategory(name='food')
        new_category.save_category()
        category_list = ImageCategory.objects.all()
        self.assertTrue(len(category_list) > 1)

    # testing deleting a category
    def test_delete_category(self):
        self.new_image_category.save_category()
        category_list = ImageCategory.objects.all()
        self.new_image_category.delete_category()
        self.assertTrue(len(category_list) < 1)