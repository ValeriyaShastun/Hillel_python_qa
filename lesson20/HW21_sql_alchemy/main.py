from lesson20.HW21_sql_alchemy.models.orders import Orders
from lesson20.HW21_sql_alchemy.repositories.orders_repository import OrdersRepository
from lesson20.HW21_sql_alchemy.models.products import Products
from lesson20.HW21_sql_alchemy.repositories.products_repository import ProductsRepository
from lesson20.HW21_sql_alchemy.repositories.total_products_in_orders_quantity_repository import \
    TotalProductsInOrdersRepository

orders_repo = OrdersRepository()
products_repo = ProductsRepository()
total_products_price_in_orders = TotalProductsInOrdersRepository()

product = Products(id=6, name='garlic', price=12)
product_2 = Products(id=6, name='cucumber', price=8)
print(products_repo.get_by_id(1))
print(products_repo.get_by_name('apple'))
print(products_repo.get_all())
products_repo.insert_one(product)
print(products_repo.get_all())
products_repo.delete_one(product)
print(products_repo.get_all())
products_repo.insert_one(product_2)
print(products_repo.get_all())

order = Orders(id=6, product_id=6, quantity= 12)
print(orders_repo.get_by_order_id(1))
print(orders_repo.get_by_product_id(4))
print(orders_repo.get_all())
orders_repo.insert_one(order)
print(orders_repo.get_all())
orders_repo.delete_one(order)
print(orders_repo.get_all())

products_repo.delete_by_id(6)

print(total_products_price_in_orders.total_calc())
