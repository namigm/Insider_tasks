import pytest


@pytest.mark.order(3)
def test_get_by_id(api_get_by_id_init):
    api_get_by_id_init.get_by_id(pet_id=12349, expected_name='doggie_updated')
