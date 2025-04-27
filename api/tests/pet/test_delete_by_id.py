import pytest


@pytest.mark.order(4)
def test_delete_by_id(api_delete_by_id_init):
    api_delete_by_id_init.delete_by_id(pet_id=12349)


def test_delete_by_id_negative(api_delete_by_id_init):
    api_delete_by_id_init.delete_nonexistent_pet(pet_id=23453310)
