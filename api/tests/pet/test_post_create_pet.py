import pytest


@pytest.mark.order(1)
def test_post_create_pet(api_create_pet_init):
    api_create_pet_init.post_create_pet()


def test_post_create_pet_negative(api_create_pet_init):
    api_create_pet_init.post_create_pet_empty_body()
