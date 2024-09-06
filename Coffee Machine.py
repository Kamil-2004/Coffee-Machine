logo = """

  ^    ^    ^    ^    ^    ^       ^    ^    ^    ^    ^    ^    ^  
 /c\  /o\  /f\  /f\  /e\  /e\     /m\  /a\  /c\  /h\  /i\  /n\  /e\ 
<___><___><___><___><___><___>   <___><___><___><___><___><___><___>

"""
print(logo)


class CoffeeMachine:
    def __init__(self):
        self.water_available = 1000  # in ml
        self.coffee_beans_available = 500  # in grams
        self.milk_available = 750  # in ml
        self.cups_available = 10  # number of cups

    def check_resources(self, water_needed, coffee_beans_needed, milk_needed):
        if (self.water_available >= water_needed and
            self.coffee_beans_available >= coffee_beans_needed and
            self.milk_available >= milk_needed and
            self.cups_available >= 1):
            return True
        else:
            return False

    def make_coffee(self, water_needed, coffee_beans_needed, milk_needed):
        if self.check_resources(water_needed, coffee_beans_needed, milk_needed):
            print("Making coffee...")
            self.water_available -= water_needed
            self.coffee_beans_available -= coffee_beans_needed
            self.milk_available -= milk_needed
            self.cups_available -= 1
            print("Coffee is ready! Enjoy.")
        else:
            print("Sorry, not enough resources to make coffee. Please refill.")

    def refill(self, water_amount, coffee_beans_amount, milk_amount, cups_amount):
        self.water_available += water_amount
        self.coffee_beans_available += coffee_beans_amount
        self.milk_available += milk_amount
        self.cups_available += cups_amount
        print("Refilled successfully.")

# Example usage:
if __name__ == "__main__":
    my_coffee_machine = CoffeeMachine()

    # Making a cappuccino (example quantities)
    water_needed = 200  # ml
    coffee_beans_needed = 20  # grams
    milk_needed = 100  # ml

    my_coffee_machine.make_coffee(water_needed, coffee_beans_needed, milk_needed)

    # Check remaining resources
    print(f"Remaining resources: Water - {my_coffee_machine.water_available} ml, "
          f"Coffee beans - {my_coffee_machine.coffee_beans_available} grams, "
          f"Milk - {my_coffee_machine.milk_available} ml, "
          f"Cups - {my_coffee_machine.cups_available}")

    # Refill the machine (example refill amounts)
    my_coffee_machine.refill(1000, 500, 500, 10)

    # Check resources after refill
    print(f"After refill: Water - {my_coffee_machine.water_available} ml, "
          f"Coffee beans - {my_coffee_machine.coffee_beans_available} grams, "
          f"Milk - {my_coffee_machine.milk_available} ml, "
          f"Cups - {my_coffee_machine.cups_available}")


    


