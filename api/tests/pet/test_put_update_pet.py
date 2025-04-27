import pytest


@pytest.mark.order(2)
def test_post_create_pet(api_update_pet_init):
    api_update_pet_init.put_update_pet()
