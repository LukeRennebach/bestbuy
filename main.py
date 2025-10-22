import products
import store


product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(store_obj):
    """Start the store menu interface for user interaction."""
    while True:
        print("   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ")
        if choice == "1":
            print("------")
            for i, p in enumerate(store_obj.get_all_products(), 1):
                print(f"{i}. {p.name}, Price: ${int(p.price)}, Quantity: {p.quantity}")
            print("------")
        elif choice == "2":
            total = store_obj.get_total_quantity()
            print(f"Total of {total} items in store")
        elif choice == "3":
            print("------")
            for i, p in enumerate(store_obj.get_all_products(), 1):
                print(f"{i}. {p.name}, Price: ${int(p.price)}, Quantity: {p.quantity}")
            print("------")
            shopping_list = []
            while True:
                print("When you want to finish order, enter empty text.")
                prod_num = input("Which product # do you want? ")
                if prod_num == "":
                    break
                amount = input("What amount do you want? ")
                if amount == "":
                    break
                try:
                    prod_index = int(prod_num) - 1
                    amt = int(amount)
                    product = store_obj.get_all_products()[prod_index]
                    shopping_list.append((product, amt))
                except (ValueError, IndexError):
                    continue
            print("********")
            total_payment = store_obj.order(shopping_list)
            print(f"Order made! Total payment: ${total_payment}")
        elif choice == "4":
            break

if __name__ == "__main__":
    start(best_buy)
