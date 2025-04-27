import pytest

from api.env_setup import BASE_URL
from api.routes.pet.put_update_pet import UpdatePet
from api.routes.pet.pos_create_pet import CreatePet
from api.routes.pet.get_by_id import GetByID
from api.routes.pet.delete_by_id import DeleteByID


def init_api(api_class):
    return api_class(base_url=BASE_URL, version="v2", endpoint="pet")


@pytest.fixture()
def api_create_pet_init():
    return init_api(CreatePet)


@pytest.fixture()
def api_update_pet_init():
    return init_api(UpdatePet)


@pytest.fixture()
def api_get_by_id_init():
    return init_api(GetByID)


@pytest.fixture()
def api_delete_by_id_init():
    return init_api(DeleteByID)
