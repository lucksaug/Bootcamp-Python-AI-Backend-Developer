from typing import Annotated

from pydantic import UUID4, Field

from web_api.contrib.schemas import BaseSchema, OutMixin


class CategoriaIn(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome da categoria", example="Scale", max_length=10)
    ]


class CategoriaOut(CategoriaIn, OutMixin):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]
