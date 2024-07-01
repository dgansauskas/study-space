from workout_api.contrib.models import BaseModel
from workout_api.atleta.models import AtletaModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamentos'

    pk_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(100), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(50), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')