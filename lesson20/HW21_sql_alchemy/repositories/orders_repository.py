from lesson20.HW21_sql_alchemy.session import session
from lesson20.HW21_sql_alchemy.models.orders import Orders
from sqlalchemy import select, delete


class OrdersRepository:
    def __init__(self):
        self.__session = session

    def get_by_product_id(self, id_value: int): # Return an instance based on the given primary key identifier
        order = self.__session.get(Orders, {'id': id_value})
        return order

    def get_by_order_id(self, product_id):
        stmt = select(Orders).where(Orders.id == f"{product_id}")
        order = self.__session.scalars(stmt).one()
        return order

    def get_all(self):
        all_orders = self.__session.query(Orders).all()
        for order in all_orders:
            print(f'\n{order}')
        return all_orders

    def insert_one(self, order: Orders):
        self.__session.add(order)
        self.__session.commit()

    def delete_one(self, order: Orders):
        self.__session.delete(order)
        self.__session.commit()

    def delete_by_id(self, id):
        stmt = delete(Orders).where(Orders.id == int(f'{id}'))
        print(stmt)
        self.__session.execute(stmt)
        self.__session.commit()
