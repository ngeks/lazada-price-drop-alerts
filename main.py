import os

from product import Product


def main(product):
    actions = ("view", "add", "remove", "exit")

    while True:
        action = input("What do you want to do? [view, add, remove, exit] -> ")

        if action not in actions:
            print("\nError: Invalid action. Please try again.")
        elif action == "exit":
            print("\nIf you find this script helpful you can support me below.\n"
                  "Donate: https://bit.ly/3y33k36\n"
                  "Twitter: @ngeksdev\n"
                  "Email: ngeksdev@gmail.com")
            print("\n===> Run the alerts.py script to send alerts. Goodbye! :) <===\n")
            break
        else:
            data = product.data()
            if data.empty and action != "add":
                print(f"\nError: Your data is empty. There is nothing to {action}.")
            elif action == "view":
                product.view()
            elif action == "add":
                try:
                    product.add(
                        input("Name: "),
                        float(input("Price: ")),
                        input("Product URL: ")
                    )
                except ValueError:
                    print("\nError: Please enter a valid price.")
                else:
                    print("\nProduct has been added.")
            elif action == "remove":
                try:
                    product.remove(int(input("Index Number: ")))
                except (KeyError, ValueError):
                    print("\nError: Please enter a valid index number.")
                else:
                    print("\nProduct has been removed.")


if __name__ == "__main__":
    main(Product(os.environ['DATA_FILE']))
    