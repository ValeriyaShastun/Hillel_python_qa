from lesson21.HW22_mongo_db.products_repository import ProductsRepo


products = ProductsRepo()

print(products.list_all_databases())
print(products.list_all_collections_names())

products.insert_products([{"name": "onion", "price": 2},
                          {"name": "apple", "price": 3, "perishable": False},
                          {"name": "orange", "price": 5},
                          {"name": "banana", "price": 7, "perishable": True},
                          {"name": "cherry", "price": 10, "perishable": True},
                          ])

print(products.list_all_databases())
print(products.list_all_collections_names())
print("\n")

for prod in products.find_all_products():
    print(prod)
print("\n")

products.insert_product({"name": "garlic", "price": 6})
garlic = products.find_product({"name": "garlic"})
print(garlic)
print("\n")

products.find_product_and_delete({"price": 5})
for prod in products.find_all_products():
    print(prod)
print("\n")

products.find_product_and_update({"perishable": False}, {"perishable": True})

perishables = products.find_many_products({"perishable": True})
for prod1 in perishables:
    print(prod1)
print("\n")

products.delete_products({"price": 10})
for prod2 in products.find_all_products():
    print(prod2)
print("\n")

products.update_many({"perishable":True}, {"price": 11})
for prod3 in products.find_all_products():
    print(prod3)
print("\n")

for prod4 in products.find_products_and_return_exact_fields(["name", "price", "perishable"], ["_id"]):
    print(prod4)
print("\n")

for prod5 in products.find_products_by_query_with_operator("price", "$gte", 5):
    print(prod5)
print("\n")

for prod6 in products.sort_ascending("price"):
    print(prod6)
print("\n")

for prod7 in products.sort_descending("name"):
    print(prod7)
print("\n")

for prod8 in products.limit(2):
    print(prod8)
print("\n")

for prod9 in products.limit_and_sort("id", 3, asc=False):
    print(prod9)
print("\n")

products.delete_all_docs_in_collection()
products.drop_collection()
print(products.list_all_collections_names())
