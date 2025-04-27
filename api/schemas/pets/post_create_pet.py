from pydantic import BaseModel, ConfigDict
from typing import List


class Tag(BaseModel):
    id: int
    name: str


class Category(BaseModel):
    id: int
    name: str


class CreatePet200(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: str
    model_config = ConfigDict(extra='forbid')
