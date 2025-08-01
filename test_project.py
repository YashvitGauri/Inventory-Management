import pytest
from project import (
    create_product, restock_product, sell_product,
    add_product_to_inventory, remove_product_from_inventory,
    get_product_from_inventory
)

def test_create_product():
    product = create_product(1, "Laptop", 1200.00, 10)
    assert product["product_id"] == 1
    assert product["name"] == "Laptop"
    assert product["price"] == 1200.00
    assert product["quantity"] == 10

def test_restock_product():
    product = create_product(1, "Laptop", 1200.00, 10)
    restock_product(product, 5)
    assert product["quantity"] == 15

def test_sell_product():
    product = create_product(1, "Laptop", 1200.00, 10)
    sell_product(product, 3)
    assert product["quantity"] == 7

def test_add_product_to_inventory():
    inventory = {}
    product = create_product(1, "Laptop", 1200.00, 10)
    add_product_to_inventory(inventory, product)
    assert get_product_from_inventory
