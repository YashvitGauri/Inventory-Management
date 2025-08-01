# Inventory Management
    Video Demo:  https://youtu.be/85AoD2Y0Pa4?si=-Iy6mpR5PnULTudh


   ### Description:
### Project Title: **Interactive Inventory Management System**

#### **Project Overview**

This project is an **Interactive Inventory Management System** designed to manage products within a store. It provides users with a command-line interface to perform various inventory management tasks, such as adding new products, restocking existing products, selling products, viewing the current inventory, and removing products from the inventory. The system is implemented using functions and dictionaries, ensuring a modular and straightforward approach.

#### **Key Features**

1. **Add Product**:
   - Allows the user to add a new product to the inventory by specifying its ID, name, price, and quantity. The system ensures that each product ID is unique, preventing duplicate entries.

2. **Restock Product**:
   - Enables the user to increase the quantity of an existing product in the inventory. The user must provide the product ID and the amount to restock. The system updates the product’s quantity accordingly.

3. **Sell Product**:
   - Lets the user sell a certain quantity of a product. The user specifies the product ID and the amount to sell. The system checks if there is enough stock before proceeding and updates the inventory.

4. **View Inventory**:
   - Displays all products currently in the inventory, including their ID, name, price, and available quantity. This feature provides a snapshot of the store’s current stock.

5. **Remove Product**:
   - Allows the user to remove a product from the inventory by specifying its ID. The system ensures that only existing products can be removed.

6. **Exit Program**:
   - Gives the user the option to exit the program, ending the interactive session.

#### **Technical Details**

- **Data Representation**:
  - **Products**: Each product is represented as a dictionary containing its ID, name, price, and quantity.
  - **Inventory**: The inventory is a dictionary where the keys are product IDs, and the values are the corresponding product dictionaries.

- **Functions**:
  - **`create_product`**: Initializes a new product with specified attributes.
  - **`restock_product`**: Increases the quantity of a specified product.
  - **`sell_product`**: Decreases the quantity of a specified product based on sales.
  - **`add_product_to_inventory`**: Adds a new product to the inventory.
  - **`remove_product_from_inventory`**: Removes a product from the inventory.
  - **`get_product_from_inventory`**: Retrieves a product from the inventory using its ID.
  - **`print_inventory`**: Displays all products currently in the inventory.

- **User Interaction**:
  - The program runs in a loop, repeatedly presenting a menu of options to the user. The user selects an option by entering a corresponding number. The program processes the user’s input, performs the requested action, and provides feedback.

- **Input Validation**:
  - The system includes basic input validation to handle common errors, such as attempting to sell more items than are in stock or trying to add a product with a duplicate ID.

#### **Testing**

The project also includes a test suite (`test_inventory_management.py`) that uses `pytest` to ensure the core functionality of the inventory management system works as expected. The tests cover product creation, restocking, selling, adding and removing products from the inventory, and verifying overall inventory operations.

#### **Use Case**

This system can be used by small to medium-sized retail stores to manage their inventory effectively. It serves as an educational project for understanding basic inventory management concepts, user input handling, and testing in Python.

#### **Conclusion**

This **Interactive Inventory Management System** is a practical and educational project that demonstrates key programming concepts such as data manipulation, function-based programming, user interaction, and testing. It is designed to be easily extensible, allowing future enhancements like saving the inventory to a file or expanding the types of operations available to users.


