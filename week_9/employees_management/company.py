from employee import Employee
from developer import Developer
from manager import Manager

class Company:

    def __init__(self):
        self.employees = []


    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all_employees(self):
        for e in self.employees:
            e.display_employee()

    def calculate_salary(self):
        sumi = 0
        for e in self.employees:
            sumi += e.calculate_salary()
        return sumi

    def get_employee_by_id(self, id):
        for e in self.employees:
            if e.id == id:
                e.display_employee()
                return

    def delete_employee(self, id):
        employees = self.employees[:]
        for e in employees:
            if e.id == id:
                self.employees.remove(e)
                return

if __name__ == "__main__":
    company = Company()
    e1 = Employee(1, "Elazar", 5000)
    d1 = Developer(2, "Shmuel", 5500, 3, 120)
    m1 = Manager(3, "David", 6000, 2500)
    company.add_employee(e1)
    company.add_employee(d1)
    company.add_employee(m1)
    company.display_all_employees()
    print(company.calculate_salary())
    company.get_employee_by_id(2)
    company.delete_employee(3)
    company.display_all_employees()












