import time

from jsonschema.validators import validate
from api.base_api.base_api import BaseApi
from api.schemas.pets.delete_by_id import DeleteByID200
from support.logger import save_log


class DeleteByID(BaseApi):
    LOG = save_log()

    def __init__(self, base_url, version, endpoint):
        super().__init__(base_url, version, endpoint)

    def delete_by_id(self, pet_id, timeout=10, interval=2):
        start_time = time.time()
        while time.time() - start_time < timeout:
            response = self.delete_method(headers={"accept": "application/json"}, params=pet_id)
            if response.status_code == 200:
                pet_data = response.json()
                if pet_data.get("message") == str(pet_id):
                    assert pet_data['code'] == 200
                    validate(instance=pet_data, schema=DeleteByID200.model_json_schema())
                    self.LOG.info(f"[delete_by_id] Pet with id={pet_id} found for delete")
                    return pet_data
                else:
                    self.LOG.info(f"[delete_by_id] Pet with id={pet_id} not found for delete, we are trying again")
                    time.sleep(interval)
            else:
                self.LOG.info(
                    f"[delete_by_id] Failed to fetch pet during delete with id={pet_id}. Status code: {response.status_code}")
        raise TimeoutError(f"Pet with id={pet_id} not found for delete for {timeout} seconds")

    def delete_nonexistent_pet(self, pet_id):
        response = self.delete_method(
            headers={"accept": "application/json"},
            params=pet_id)
        assert response.status_code == 404, f"Expected 404 Not Found but got {response.status_code}"
        self.LOG.info(f"[delete_nonexistent_pet] Correctly handled non-existent pet with id={pet_id}")

