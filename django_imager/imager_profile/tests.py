from django.test import Client, RequestFactory, TestCase
from bs4 import BeautifulSoup as soup
from django.urls import reverse
from imager_profile.views import home_view
from django.contrib.auth.models import User
# Create your tests here.


class ProfileViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.req_factory = RequestFactory()

    # test the link button to the home page pops up
    def test_link_button_on_home_page_appears(self):
        response = self.client.get(reverse('home'))
        self.assertTrue(b'a href="/" class="icon-home"' in response.content)

    # test the home view context has an empty dictionary
    def test_home_view_returns_status_code_200(self):
        get_req = self.req_factory.get('/foo')
        response = home_view(get_req)
        self.assertTrue(response.status_code == 200)

    # if the user isn't authenticated, show login button
    def test_if_user_isnt_authenticated_shows_login(self):
        response = self.client.get(reverse('home'))
        self.assertTrue(b'login' in response.content.lower())

    # if the user is authenticated, show logout button
    def test_if_user_is_authenticated_shows_logout(self):
        test_bob = User(username='bob')
        test_bob.set_password('bobberton')
        test_bob.save()
        self.client.post(reverse('login'), {'username': 'bob', 'password': 'bobberton'})
        response = self.client.get(reverse('home'))
        self.assertFalse(b'login' in response.content.lower())
        self.assertTrue(b'logout' in response.content.lower())

    def test_if_user_is_authenticated_and_logsout_theyre_no_longer_authenticated(self):
        test_bob = User(username='bob')
        test_bob.set_password('bobberton')
        test_bob.save()
        self.client.post(reverse('login'), {'username': 'bob', 'password': 'bobberton'})
        response = self.client.get(reverse('logout'), follow=True)
        self.assertTrue(b'login' in response.content.lower())
