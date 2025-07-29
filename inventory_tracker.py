inventory = []

def add_item():
    name = input("Item name: ")
    price = float(input("Item price: "))
    quantity = int(input("Item quantity: "))
    inventory.append({"name": name, "price": price, "quantity": quantity})
    print("Item added.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    for item in inventory:
        print(f"{item['name']} - ₹{item['price']} - Qty: {item['quantity']}")

def update_quantity():
    name = input("Enter item name to update: ")
    for item in inventory:
        if item['name'] == name:
            item['quantity'] = int(input("Enter new quantity: "))
            print("Quantity updated.")
            return
    print("Item not found.")

def remove_item():
    name = input("Enter item name to remove: ")
    for item in inventory:
        if item['name'] == name:
            inventory.remove(item)
            print("Item removed.")
            return
    print("Item not found.")

def inventory_menu():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Quantity")
        print("4. Remove Item")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_quantity()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

inventory_menu()
