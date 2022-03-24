from unittest import TestCase

from django.core.exceptions import ValidationError
from django.test import TestCase as DTestCase

from testing_demos.web.models import Profile


class ProfileTests(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Nikoleta',
        'last_name': 'Zlateva',
        'age': 23,
    }

    def test_profile_when_first_name_contains_only_letters__except_success(self):
        profile = Profile(**self.VALID_USER_DATA)
        profile.save()

        self.assertIsNotNone(profile.pk)

    def test_profile_create_when_first_name_contains_digit__fail(self):
        first_name = 'Nikoleta1'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create_when_first_name_contains_dollar__fail(self):
        first_name = 'Nikoleta$'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create_when_first_name_contains_space__fail(self):
        first_name = 'Nikole ta'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)
        pass

    def test_profile_full_name_when_valid_expect_correct(self):
        profile = Profile(
            first_name='Nikoleta',
            last_name='Zlateva',
            age=23,
        )

        self.assertEqual('Nikoleta Zlateva', profile.full_name)