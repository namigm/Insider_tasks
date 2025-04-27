from pydantic import BaseModel, ConfigDict


class DeleteByID200(BaseModel):
    code: int
    type: str
    message: str
    model_config = ConfigDict(extra='forbid')
