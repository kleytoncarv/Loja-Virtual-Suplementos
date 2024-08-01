from enum import Enum
from pydantic import BaseModel, Field
from src.domain.base import DomainBase

class OrderStatusName(str, Enum):
    ACCOMPLISHED = "realizado"
    IN_PREPARATION = "em preparação"
    SENT = "enviado"
    DELIVERED = "entregue"
    FINISHED = "finalizado"

class OrderStatus(BaseModel):
    name: OrderStatusName = Field(default=OrderStatusName.ACCOMPLISHED) # por padrão o primeiro é realizado 

class OrderItem(BaseModel):
    product_id: str
    price: float
    quantity: int

class Order(DomainBase):
    status: list[OrderStatus] = Field(default=[])
    items: list[OrderItem] = Field(default=[])
   