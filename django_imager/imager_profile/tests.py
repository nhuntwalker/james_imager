from django.test import Client, RequestFactory, TestCase
from bs4 import BeautifulSoup as soup
from django.urls import reverse

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
    # if the user isn't authenticated, show login button
    # if the user is authenticated, show logout button