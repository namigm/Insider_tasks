import time

from jsonschema.validators import validate
from api.base_api.base_api import BaseApi
from api.schemas.pets.get_by_id import GetByID200
from support.logger import save_log


class GetByID(BaseApi):
    LOG = save_log()

    def __init__(self, base_url, version, endpoint):
        super().__init__(base_url, version, endpoint)

    def get_by_id(self, pet_id, expected_name, timeout=10, interval=2):
        start_time = time.time()
        while time.time() - start_time < timeout:
            response = self.get_method(headers={"accept": "application/json"}, params=pet_id)
            if response.status_code == 200:
                pet_data = response.json()
                if pet_data.get("id") == pet_id:
                    validate(instance=pet_data, schema=GetByID200.model_json_schema())
                    assert pet_data["name"] == expected_name
                    self.LOG.info(f"[get_by_id] Pet with id={pet_data.get("id")} found")
                    return pet_data
                else:
                    self.LOG.info(f"[get_by_id] Pet with id={pet_id} not found, we are trying again")
                    time.sleep(interval)
            else:
                self.LOG.info(
                    f"[get_by_id] Failed to fetch pet with id={pet_id}. Status code: {response.status_code}")
        raise TimeoutError(f"Pet with id={pet_id} not created for {timeout} seconds")
