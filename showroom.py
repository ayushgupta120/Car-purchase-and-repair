# Parent Class for Showroom Management
class ShowroomManagement:
    def __init__(self):
        self.cars = []               # List to store car details
        self.employees = []          # List to store employee details

    def display_cars(self):
        print("\n--- Car Inventory ---")
        for car in self.cars:
            print(car)

    def display_employees(self):
        print("\n--- Employee Details ---")
        for emp in self.employees:
            print(emp)


# Class for New Car Purchase
class Car:
    def __init__(self, car_id, model, price, quantity):
        self.car_id = car_id
        self.model = model
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"CarID: {self.car_id}, Model: {self.model}, Price: {self.price}, Quantity: {self.quantity}"


# Class for Employee Availability & Leave
class Employee:
    def __init__(self, emp_id, name, expertise_level):
        self.emp_id = emp_id
        self.name = name
        self.expertise_level = expertise_level
        self.is_available = True

    def apply_leave(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.name} is now on leave.")
        else:
            print(f"{self.name} is already on leave.")

    def return_from_leave(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.name} is back from leave.")
        else:
            print(f"{self.name} is already available.")

    def update_expertise(self, feedback_score):
        # Simple rule: increase expertise if feedback is good
        if feedback_score >= 4:
            self.expertise_level += 1
            print(f"{self.name}'s expertise increased to {self.expertise_level}")
        elif feedback_score <= 2 and self.expertise_level > 1:
            self.expertise_level -= 1
            print(f"{self.name}'s expertise decreased to {self.expertise_level}")
        else:
            print(f"No change in expertise for {self.name}")

    def __str__(self):
        status = "Available" if self.is_available else "On Leave"
        return f"EmpID: {self.emp_id}, Name: {self.name}, Expertise Level: {self.expertise_level}, Status: {status}"


# Class for Price Update (Based on Statistics)
class PriceStatistics:
    def __init__(self, showroom):
        self.showroom = showroom

    def update_car_price(self, car_id, percentage_change):
        for car in self.showroom.cars:
            if car.car_id == car_id:
                old_price = car.price
                car.price += (car.price * percentage_change / 100)
                print(f"Updated price of {car.model} from {old_price} to {car.price}")
                return
        print("Car not found!")


# Test the functionality
if __name__ == "__main__":
    showroom = ShowroomManagement()

    # Adding Cars (New Car Purchase)
    car1 = Car(1, "Toyota Camry", 30000, 5)
    car2 = Car(2, "Honda Civic", 25000, 3)
    showroom.cars.extend([car1, car2])

    # Adding Employees
    emp1 = Employee(101, "Alice", 3)
    emp2 = Employee(102, "Bob", 4)
    showroom.employees.extend([emp1, emp2])

    showroom.display_cars()
    showroom.display_employees()

    # Employee Leave Handling
    emp1.apply_leave()
    emp1.return_from_leave()

    # Updating Expertise based on Customer Feedback
    emp2.update_expertise(feedback_score=5)
    emp2.update_expertise(feedback_score=1)

    # Updating Car Prices
    stats = PriceStatistics(showroom)
    stats.update_car_price(car_id=1, percentage_change=10)  # Increase price by 10%
    stats.update_car_price(car_id=2, percentage_change=-5)  # Decrease price by 5%

    showroom.display_cars()
