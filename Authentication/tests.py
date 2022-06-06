from django.contrib.auth.models import User
from django.test import TestCase

from .models import Profile


class SignUp_Test(TestCase):

    def setUp(self) -> None:
        self.testUser = {
            "username": "testUser",
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@testing.com",
            "password1": "AMaterasu123",
            "password2": "AMaterasu123",
        }

    def test_display_signuppage_template(self):
        response = self.client.get('/auth/signup/')
        self.assertTemplateUsed(response, 'Authentication/SignupPage.html')

    def test_profile_model(self):
        user = Profile(username='superman', first_name='clark', last_name='kent')
        user.save()

        usr_obj = Profile.objects.get(username='superman')

        self.assertEqual('superman', usr_obj.username)

    def test_signupveiw(self):
        response = self.client.post('/auth/signup/', data=self.testUser)

        self.assertEqual(response.status_code, 302, msg='Failed to redirect')
        user = User.objects.get(username='testUser')
        self.assertEqual('testUser', user.username)


class LoginPageTests(TestCase):
    def setUp(self) -> None:
        self.testUser = {
            "username": "testUser",
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@testing.com",
            "password1": "AMaterasu123",
            "password2": "AMaterasu123",
        }
        self.client.post('/auth/signup/', data=self.testUser)

    def test_userLogin(self):
        response = self.client.post("/auth/login/", data={
            "username": self.testUser['username'],
            "password": self.testUser["password1"],
        })

        self.assertTrue(self.client.session['_auth_user_id'])
        self.assertEqual(response.status_code, 302)

    def test_loginpage_template(self):
        response = self.client.get('/auth/login/')
        self.assertTemplateUsed(response, 'Authentication/LoginPage.html')
