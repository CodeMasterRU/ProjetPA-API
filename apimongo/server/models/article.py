from typing import Optional

from pydantic import BaseModel, Field


class ArticleSchema(BaseModel):
    titre: str = Field(...)
    prix_barquette: str = Field(...)
    prix_par_kilo: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "titre": "test_titre",
                "prix_barquette": "test_prix_barquette",
                "prix_par_kilo": 222,
            }
        }


class UpdateArticleModel(BaseModel):
    titre: str = Field(...)
    prix_barquette: str = Field(...)
    prix_par_kilo: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "titre": "update_test_titre",
                "prix_barquette": "update_test_prix_barquette",
                "prix_par_kilo": 222,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}