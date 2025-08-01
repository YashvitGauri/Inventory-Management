
def main():

    inventory = {}

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. Restock Product")
        print("3. Sell Product")
        print("4. View Inventory")
        print("5. Remove Product")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            product = create_product(product_id, name, price, quantity)
            try:
                add_product_to_inventory(inventory, product)
                print("Product added successfully.")
            except ValueError as e:
                print(e)

        elif choice == '2':
            product_id = int(input("Enter Product ID: "))
            amount = int(input("Enter Amount to Restock: "))
            product = get_product_from_inventory(inventory, product_id)
            if product:
                try:
                    restock_product(product, amount)
                    print("Product restocked successfully.")
                except ValueError as e:
                    print(e)
            else:
                print("Product not found.")

        elif choice == '3':
            product_id = int(input("Enter Product ID: "))
            amount = int(input("Enter Amount to Sell: "))
            product = get_product_from_inventory(inventory, product_id)
            if product:
                try:
                    sell_product(product, amount)
                    print("Product sold successfully.")
                except ValueError as e:
                    print(e)
            else:
                print("Product not found.")

        elif choice == '4':
            print("\nInventory:")
            print_inventory(inventory)

        elif choice == '5':
            product_id = int(input("Enter Product ID: "))
            try:
                remove_product_from_inventory(inventory, product_id)
                print("Product removed successfully.")
            except ValueError as e:
                print(e)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


def create_product(product_id, name, price, quantity):
    """Create a new product."""
    return {
        "product_id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

def restock_product(product, amount):
    """Restock a product by a certain amount."""
    if amount > 0:
        product["quantity"] += amount
    else:
        raise ValueError("Restock amount must be positive.")

def sell_product(product, amount):
    """Sell a certain amount of a product."""
    if amount > 0 and amount <= product["quantity"]:
        product["quantity"] -= amount
    else:
        raise ValueError("Invalid amount to sell.")

def add_product_to_inventory(inventory, product):
    """Add a product to the inventory."""
    if product["product_id"] in inventory:
        raise ValueError("Product with this ID already exists.")
    inventory[product["product_id"]] = product

def remove_product_from_inventory(inventory, product_id):
    """Remove a product from the inventory."""
    if product_id in inventory:
        del inventory[product_id]
    else:
        raise ValueError("Product not found.")

def get_product_from_inventory(inventory, product_id):
    """Retrieve a product from the inventory."""
    return inventory.get(product_id, None)

def print_inventory(inventory):
    """Print all products in the inventory."""
    if not inventory:
        print("Inventory is empty.")
    for product in inventory.values():
        print(f"{product['name']} (ID: {product['product_id']}) - ${product['price']:.2f} - Quantity: {product['quantity']}")



if __name__ == "__main__":
    main()
