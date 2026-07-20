import factory
from django.contrib.auth import get_user_model

from domain.base.models import Profile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ("username",)

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@gscashadvance.co.zm")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    role = Profile.Role.STAFF
    branch = "Woodlands"
