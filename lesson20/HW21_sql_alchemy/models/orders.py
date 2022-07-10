from sqlalchemy.orm import relationship
from sqlalchemy import INTEGER, Column, ForeignKey
from lesson20.HW21_sql_alchemy.models.base import Base


class Orders(Base):
    __tablename__ = "orders"
    # why this is primary key: https://docs.sqlalchemy.org/en/14/faq/ormconfiguration.html#faq-mapper-primary-key
    id = Column('id', INTEGER, primary_key=True)
    product_id = Column(INTEGER, ForeignKey('products.id'), nullable=False)
    quantity = Column(INTEGER)

    products = relationship("Products", back_populates="orders")

    def __str__(self):
        return f'id: {self.id}, product_id: {self.product_id}, quantity: {self.quantity}'

