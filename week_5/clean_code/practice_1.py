


# exercise 1 - Correct Naming

def active_members(members_list):
    act_members = []
    for member in members_list:
        member_name = member[0]
        age = member[1]
        is_active = member[2]
        if age >= 18 and is_active:
            act_members.append(member_name)
    return act_members

data_members = [
    ["Dan", 25, True],
    ["Noa", 16, True],
    ["Yael", 30, False],
]



# exercise 2 - Small Functions

def is_valid(user_email,quantity,stock) -> bool:
    if not user_email:
        print("Invalid user")
        return False
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return False
    return True

def price_calculate(product_price, quantity):
    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price


def create_report(user_email, product_name, price,  quantity):
    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    return order_user, order_product, order_quantity, order_total, order_status


def print_order(order_report):
    order_user = order_report[0]
    order_product = order_report[1]
    order_quantity = order_report[2]
    order_total = order_report[3]
    order_status = order_report[4]
    print(
        f"Order {order_status}:",
        f"{order_user}",
        f"bought {order_quantity}",
        f"x {order_product}",
        f"for ${order_total}"
    )


def update_stock(stock, quantity):
    stock -= quantity
    return stock


def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if is_valid(user_email, quantity, stock):
        price = price_calculate(product_price, quantity)
        stock = update_stock(stock, quantity)
        order_report = create_report(user_email, product_name, price, quantity)
        print_order(order_report)
        return order_report
    else:
        return None


# Exercise 3 - Single Responsibility

def manage_students(names, grades, new_name, new_grade):
    # validation
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return students
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return students

    # add student
    grades.append(new_grade)

    # calculate stats
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)

    # print report
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

    # save to file
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")

    return names, grades


def valid_name(new_name):
    pass

def valid_grade():
    pass


def validation(new_name, new_grade):

    pass




