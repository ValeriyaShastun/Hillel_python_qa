from lesson20.HW21_sql_alchemy.session import session
from lesson20.HW21_sql_alchemy.models.products import Products
from sqlalchemy import select, delete


class ProductsRepository:
    def __init__(self):
        self.__session = session

    def get_by_id(self, id_value: int):
        product = self.__session.get(Products, {'id': id_value})
        return product

    def get_all(self):
        all_products = self.__session.query(Products).all()
        for product in all_products:
            print(f'\n{product}')
        return all_products

    def insert_one(self, product: Products):
        self.__session.add(product)
        self.__session.commit()

    def delete_one(self, product: Products):
        self.__session.delete(product)
        self.__session.commit()

    def get_by_name(self, product_name):
        stmt = select(Products).where(Products.name == f"{product_name}")
        order = self.__session.scalars(stmt).one()
        return order

    def delete_by_id(self, id):
        stmt = delete(Products).where(Products.id == int(f'{id}'))
        print(stmt)
        self.__session.execute(stmt)
        self.__session.commit()
