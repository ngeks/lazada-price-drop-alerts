def main():
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
            if action == "view":
                pass
            elif action == "add":
                pass
            elif action == "remove":
                pass


if __name__ == "__main__":
    main()
