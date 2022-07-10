from sqlalchemy.orm import relationship
from sqlalchemy import INTEGER, Column, VARCHAR
from lesson20.HW21_sql_alchemy.models.base import Base


class Products(Base):
    __tablename__ = "products"
    id = Column(INTEGER, primary_key=True, nullable=False)
    name = Column(VARCHAR(25))
    price = Column(INTEGER)

    orders = relationship("Orders", back_populates = "products", cascade = "all, delete-orphan")

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, price: {self.price}'
