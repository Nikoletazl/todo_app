from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from testing_demos.web.models import Profile
from testing_demos.web.views import ProfileListView

UserModel = get_user_model()


class ProfilesListViewTests(TestCase):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('list profiles'))

        self.assertTemplateUsed(response, 'profiles/list.html')

    def test_get__expect_context_to_contain_two_profiles(self):
        profiles_to_create = (
            Profile(first_name='Nikoleta',
                    last_name='Zlateva',
                    age=23
                    ),
            Profile(first_name='Ariya',
                    last_name='Zlateva',
                    age=25
                    ),
        )

        Profile.objects.bulk_create(profiles_to_create)

        response = self.client.get(reverse('list profiles'))

        profiles = response.context['object_list']

        self.assertEqual(len(profiles), 2)

    def test_get_when_not_loggedin_user__expect_no_user(self):
        response = self.client.get(reverse('list profiles'))

        self.assertEqual('No user', response.context['user'])

    def test_get_when_loggedin_user__expect_username(self):

        user_data = {
            'username': 'nikoleta',
            'password': 'nikoleta123',
        }

        UserModel.objects.create_user(**user_data)

        self.client.login(**user_data)

        response = self.client.get(reverse('list profiles'))

        self.assertEqual(user_data['username'], response.context['user'])