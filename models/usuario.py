from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator


class RolUsuario(str, Enum):
    JUGADOR = "jugador"
    ADMIN = "admin"
    CRITICO = "critico"


class Usuario(BaseModel):
    id: Optional[int] = Field(
        None, description="Identificador único (asignado por la base de datos)"
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$",
        description="Nombre de usuario alfanumérico sin espacios",
    )
    email: EmailStr = Field(
        ..., description="Correo electrónico válido del usuario"
    )
    rol: RolUsuario = Field(
        default=RolUsuario.JUGADOR, description="Rol del usuario en el sistema"
    )
    activo: bool = Field(
        default=True, description="Estado de la cuenta del usuario"
    )
    fecha_registro: datetime = Field(
        default_factory=datetime.now,
        description="Fecha y hora de creación de la cuenta",
    )
