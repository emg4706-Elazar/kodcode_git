from employee import Employee



class Developer(Employee):

    def __init__(self, id , name, base_salary,
                 overtime_hours, hourly_rate):
        super().__init__(id , name, base_salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        result = self.base_salary + (self.overtime_hours * self.hourly_rate)
        return result


if __name__ == "__main__":
    d1 = Developer(2, "Shmuel", 5500, 3, 120)
    d1.display_employee()
    print(d1.calculate_salary())







