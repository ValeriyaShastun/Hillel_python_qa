from lesson20.HW21_sql_alchemy.models.products import Products
from lesson20.HW21_sql_alchemy.session import session
from lesson20.HW21_sql_alchemy.models.orders import Orders
from sqlalchemy import select, delete
from sqlalchemy.sql import operators


class TotalProductsInOrdersRepository:
    def __init__(self):
        self.__session = session

    def total_calc(self):
        stmt = select(Products.name, Products.price, Orders.quantity, operators.mul(
            Products.price, Orders.quantity).label("total")).join_from(Orders, Products)
        print(stmt)
        total_table = self.__session.execute(stmt)
        for ttl in total_table:
            print(f'name: {ttl["name"]}, price: {ttl["price"]}, quantity: {ttl["quantity"]}, total: {ttl["total"]}')
        return total_table
