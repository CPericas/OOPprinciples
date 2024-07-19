class BudgetManager:
    def __init__(self, total_budget):
        self.__total_budget = total_budget
        self.__remaining_budget = total_budget
        self.__categories = {}

    def get_total_budget(self):
        return self.__total_budget

    def set_total_budget(self, new_total_budget):
        if new_total_budget < (self.__total_budget - self.__remaining_budget):
            raise ValueError("New total budget must be sufficient to cover existing expenses.")
        self.__remaining_budget += (new_total_budget - self.__total_budget)
        self.__total_budget = new_total_budget

    def get_remaining_budget(self):
        return self.__remaining_budget

    def get_categories(self):
        return self.__categories

    def add_category(self, name, budget):
        if name in self.__categories:
            raise ValueError("Category already exists.")
        if budget <= 0:
            raise ValueError("Category budget must be a positive number.")
        if budget > self.__remaining_budget:
            raise ValueError("Category budget exceeds remaining budget.")
        self.__categories[name] = budget
        self.__remaining_budget -= budget
        print(f"Category '{name}' added with a budget of ${budget:.2f}.")

    def update_total_budget(self, new_total_budget):
        self.set_total_budget(new_total_budget)
        print(f"Total budget updated to ${self.__total_budget:.2f}. Remaining budget: ${self.__remaining_budget:.2f}.")

    def update_category(self, name, new_name, new_budget):
        if name not in self.__categories:
            raise ValueError("Category does not exist.")
        if new_budget <= 0:
            raise ValueError("New category budget must be a positive number.")
        if new_budget > self.__remaining_budget + self.__categories[name]:
            raise ValueError("New category budget exceeds remaining budget.")
        
        self.__remaining_budget += self.__categories[name] - new_budget
        self.__categories.pop(name)
        self.__categories[new_name] = new_budget
        print(f"Category updated: '{name}' renamed to '{new_name}' with a new budget of ${new_budget:.2f}.")

    def display_summary(self):
        print(f"\nTotal Budget: ${self.__total_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")
        print("Categories:")
        for name, budget in self.__categories.items():
            print(f"  {name}: ${budget:.2f}")

def interact_with_budget_manager(budget_manager):
    while True:
        print("\n1. Add Category")
        print("2. Update Total Budget")
        print("3. Update Category")
        print("4. Display Summary")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter the category name: ")
            try:
                budget = float(input("Enter the category budget: "))
                budget_manager.add_category(name, budget)
            except ValueError as e:
                print(e)
        elif choice == '2':
            try:
                new_total_budget = float(input("Enter the new total budget: "))
                budget_manager.update_total_budget(new_total_budget)
            except ValueError as e:
                print(e)
        elif choice == '3':
            old_name = input("Enter the category name to update: ")
            new_name = input("Enter the new category name: ")
            try:
                new_budget = float(input("Enter the new category budget: "))
                budget_manager.update_category(old_name, new_name, new_budget)
            except ValueError as e:
                print(e)
        elif choice == '4':
            budget_manager.display_summary()
        elif choice == '5':
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    total_budget = float(input("Enter the total budget: "))
    budget_manager = BudgetManager(total_budget)
    interact_with_budget_manager(budget_manager)

