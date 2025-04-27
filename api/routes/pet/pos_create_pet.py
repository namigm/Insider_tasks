import time

from jsonschema.validators import validate
from api.base_api.base_api import BaseApi
from api.schemas.pets.post_create_pet import CreatePet200


class CreatePet(BaseApi):
    def __init__(self, base_url, version, endpoint):
        super().__init__(base_url, version, endpoint)

    def post_create_pet(self):
        pet = CreatePet200(
            id=12348,
            category={'id': 0, 'name': 'pet_test'},
            name='doggie_test',
            photoUrls=['string'],
            tags=[{'id': 0, 'name': 'doggie_test'}],
            status='available'
        )
        body = pet.model_dump()
        start_time = time.time()
        response = self.post_method(body=body, headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        })
        end_time = time.time()
        elapsed_time = end_time - start_time
        pet_data = response.json()
        validate(instance=pet_data, schema=CreatePet200.model_json_schema())
        assert response.status_code == 200
        assert elapsed_time < 2, f"Test failed, response time exceeded 2 seconds: {elapsed_time:.3f}s"
        assert pet_data['category']['name'] == 'pet_test'
        assert pet_data['name'] == 'doggie_test'
        assert pet_data['tags'][0]['name'] == 'doggie_test'
        assert pet_data['id'] == 12348

    def post_create_pet_empty_body(self):
        empty_body = {}

        response = self.post_method(body=empty_body, headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        })
        pet_data = response.json()
        assert response.status_code == 200, f"Expected 200 OK but got {response.status_code}"
        assert "id" in pet_data, "Expected 'id' in response"
        assert isinstance(pet_data["id"], int), f"Expected 'id' to be int but got {type(pet_data['id'])}"
        assert "name" not in pet_data
        assert "category" not in pet_data
        assert "photoUrls" in pet_data
        assert isinstance(pet_data["photoUrls"], list)
        assert len(pet_data["photoUrls"]) == 0
        assert "tags" in pet_data
        assert isinstance(pet_data["tags"], list)
        assert len(pet_data["tags"]) == 0
