import products
import store


def build_store():
    """Create and return a Store pre-populated with default products.

    Encapsulates setup to avoid side effects at import time.
    """
    product_list = []
    try:
        product_list.append(products.Product("MacBook Air M2", price=1450, quantity=100))
    except Exception as e:
        print(f"Invalid product skipped: {e}")
    try:
        product_list.append(products.Product("Bose QuietComfort Earbuds", price=250, quantity=500))
    except Exception as e:
        print(f"Invalid product skipped: {e}")
    try:
        product_list.append(products.Product("Google Pixel 7", price=500, quantity=250))
    except Exception as e:
        print(f"Invalid product skipped: {e}")
    return store.Store(product_list)


def print_menu():
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store_obj):
    print("------")
    for i, p in enumerate(store_obj.get_all_products(), 1):
        print(f"{i}. {p.name}, Price: ${int(p.price)}, Quantity: {p.quantity}")
    print("------")


def show_total(store_obj):
    total = store_obj.get_total_quantity()
    print(f"Total of {total} items in store")


def make_order(store_obj):
    # Show the product list as part of the order flow
    list_products(store_obj)

    if len(store_obj.get_all_products()) == 0:
        print("No active products available.")
        return

    shopping_list = []
    while True:
        print("When you want to finish order, enter empty text.")
        prod_num = input("Which product # do you want? ")
        if prod_num == "":
            break
        try:
            prod_index = int(prod_num) - 1
            if prod_index < 0 or prod_index >= len(store_obj.get_all_products()):
                print("Invalid product number. Please select a number from the list.")
                continue
        except ValueError:
            print("Invalid product number. Please select a number from the list.")
            continue
        amount = input("What amount do you want? ")
        if amount == "":
            break
        try:
            amt = int(amount)
            if amt <= 0:
                print("Amount must be a positive integer.")
                continue
            product = store_obj.get_all_products()[prod_index]
            if amt > product.get_quantity():
                print("Not enough quantity in stock.")
                continue
            shopping_list.append((product, amt))
            print("Product added to list!")
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

    print("********")
    try:
        total_payment = store_obj.order(shopping_list)
        print(f"Order made! Total payment: ${int(total_payment)}")
    except Exception as e:
        print(str(e))


def start(store_obj):
    """Start the store menu interface for user interaction."""
    while True:
        print_menu()
        choice = input("Please choose a number: ")
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, please try again.")
            continue
        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            show_total(store_obj)
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            break


if __name__ == "__main__":
    best_buy = build_store()
    start(best_buy)
