from pydantic import Field, UUID4
from typing import Annotated
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT King', max_length=30)]
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', example='Rua A, 123', max_length=100)]
    proprietario: Annotated[str, Field(description='Proprietário do Centro de Treinamento', example='John Doe', max_length=50)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT King', max_length=30)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do Centro de Treinamento')]