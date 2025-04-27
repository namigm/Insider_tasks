from jsonschema.validators import validate
from api.base_api.base_api import BaseApi
from api.schemas.pets.put_update_pet import UpdatePet200


class UpdatePet(BaseApi):
    def __init__(self, base_url, version, endpoint):
        super().__init__(base_url, version, endpoint)

    def put_update_pet(self):
        pet = UpdatePet200(
            id=12349,
            category={'id': 0, 'name': 'update_pet'},
            name='doggie_updated',
            photoUrls=['string'],
            tags=[{'id': 0, 'name': 'update_pet'}],
            status='available'
        )
        body = pet.model_dump()
        response = self.post_method(body=body, headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        })

        pet_data = response.json()
        print(f"update {pet_data}")
        validate(instance=pet_data, schema=UpdatePet200.model_json_schema())
        assert response.status_code == 200
        assert pet_data['category']['name'] == 'update_pet'
        assert pet_data['name'] == 'doggie_updated'
        assert pet_data['tags'][0]['name'] == 'update_pet'
        assert pet_data['id'] == 12349
