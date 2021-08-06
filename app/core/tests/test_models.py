from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'test@check.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        """Test the email for new user is normalized"""
        email = 'test@RANDOM.COM'
        user = get_user_model().objects.create_user(email, 'random')

        self.assertEqual(user.email, email.lower())

    def test_invalid_email(self):
        """Raises ValueError if email is not passed"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
