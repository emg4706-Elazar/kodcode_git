from employee import Employee


class Manager(Employee):

    def __init__(self, id , name, base_salary, bonus):
        super().__init__(id , name, base_salary)
        self.bonus = bonus


    def calculate_salary(self):
        return self.base_salary + self.bonus


if __name__ == "__main__":
    m1 = Manager(3, "David", 6000, 2500)
    m1.display_employee()
    print(m1.calculate_salary())





