


class Employee:

    def __init__(self, id, name, base_salary):
        self.id = id
        self.name = name
        self.base_salary = base_salary

    def display_employee(self):
        print(f"Id: {self.id} | Name: {self.name} | Salary:{self.base_salary}")


    def calculate_salary(self):
        return self.base_salary


if __name__ == "__main__":
    e1 = Employee(1, "Elazar", 5000)
    e1.display_employee()
    print(e1.calculate_salary())







