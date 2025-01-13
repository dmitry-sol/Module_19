from django.test import TestCase
from .forms import UserRegister

class UserRegisterFormTest(TestCase):
    def test_form_valid(self):
        form = UserRegister(data={
            'username': 'TestUser',
            'password': 'StrongPassword123',
            'confirm_password': 'StrongPassword123',
            'age': 18,
        }, existing_users=[])
        self.assertTrue(form.is_valid(), "Форма должна быть валидной при правильных данных.")

    def test_form_existing_user(self):
        form = UserRegister(data={
            'username': 'ExistingUser',
            'password': 'Password123',
            'confirm_password': 'Password123',
            'age': 18,
        }, existing_users=['ExistingUser'])
        self.assertFalse(form.is_valid(), "Форма не должна быть валидной, если пользователь уже существует.")

    def test_form_password_mismatch(self):
        form = UserRegister(data={
            'username': 'NewUser',
            'password': 'Password123',
            'confirm_password': 'DifferentPassword123',
            'age': 18,
        }, existing_users=[])
        self.assertFalse(form.is_valid(), "Форма не должна быть валидной, если пароли не совпадают.")

    def test_form_age_below_minimum(self):
        form = UserRegister(data={
            'username': 'YoungUser',
            'password': 'Password123',
            'confirm_password': 'Password123',
            'age': 7,
        }, existing_users=[])
        self.assertFalse(form.is_valid(), "Форма не должна быть валидной, если возраст меньше 8 лет.")


# (venv) PS D:\Dima\PycharmProjects\Module_19\PM19> python manage.py test
# Found 4 test(s).
# Creating test database for alias 'default'...
# <QuerySet []>
# System check identified no issues (0 silenced).
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.002s
#
# OK
# Destroying test database for alias 'default'...
# (venv) PS D:\Dima\PycharmProjects\Module_19\PM19>
