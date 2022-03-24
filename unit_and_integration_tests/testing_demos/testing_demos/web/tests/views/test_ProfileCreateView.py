from django.test import TestCase
from django.urls import reverse

from testing_demos.web.models import Profile


class ProfileCreateViewTests(TestCase):
    VALID_DATA = {'first_name': 'Nikoleta',
                  'last_name': 'Zlateva',
                  'age': 23, }

    def test_create_profile_when_valid(self):
        profile_data = {
            'first_name': 'Nikoleta',
            'last_name': 'Zlateva',
            'age': 23,
        }

        self.client.post(reverse('create profile'), data=profile_data, )

        profile = Profile.objects.first()

        self.assertIsNotNone(profile)
        self.assertEqual(profile_data['first_name'], profile.first_name)
        self.assertEqual(profile_data['last_name'], profile.last_name)
        self.assertEqual(profile_data['age'], profile.age)

    def test_create_profile_when_valid_expect_to_redirect(self):
        response = self.client.post(
            reverse('create profile'),
            data=self.VALID_DATA,
        )

        profile = Profile.objects.first()
        exp_url = reverse('details profile', kwargs={'pk': profile.pk})
        self.assertRedirects(response, exp_url)
