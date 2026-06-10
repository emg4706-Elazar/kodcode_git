from utils import is_valid_name
from soldier_manager import add_soldier, remove_soldier
from data import db



def main(my_data) -> None:
    is_over = False
    while not is_over:

        show_menu()

        user_choice = get_user_choice()

        if user_choice == "1":
            handle_add_soldier(my_data)
        elif user_choice == "2":
            handle_remove_soldier(my_data)
        elif user_choice == "3":
            handle_view_soldiers(my_data)
        elif user_choice == "4":
            handle_add_duty(my_data)
        elif user_choice == "5":
            handle_update_duty_status(my_data)
        elif user_choice == "6":
            handle_view_soldier_duties(my_data)
        elif user_choice == "7":
            is_over = True
    return


def show_menu() -> None:
    print("=========================================\n"
          " Wellcome to management soldiers duties \n\n"
          "--------------- Main Menu ---------------\n"
          "1. Add a new soldier\n"
          "2. Remove an exist soldier\n"
          "3. Display soldiers\n"
          "4. Add a duty for a solider\n"
          "5. Update status duty\n"
          "6. Display duties of a soldier\n"
          "7. Exit\n"
          "==========================================\n"
          "Enter your choice!"
    )
    return


def get_user_choice() -> str:
    user_choice = input("Type here: ")
    return user_choice


def handle_add_soldier(my_data: list) -> None:

    name_input = input("Enter name soldier: ")

    # Validate input
    is_valid_id = False
    while not is_valid_id:

        try:
            id_input = int(input("Enter id soldier: "))
            is_valid_id = True
        except ValueError:
            print("Invalid input enter only digits!")

    # Add soldier into "my_data"
    try:
        add_soldier(id_input, name_input,my_data)
    except ValueError as e:
        print(f"{e} The process failed.\n")

    return



def handle_remove_soldier(my_data) -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """

    # Validate input
    is_valid_id = False
    while not is_valid_id:

        try:
            id_input = int(input("Enter id soldier: "))
            is_valid_id = True
        except ValueError:
            print("Invalid input enter only digits!")

    # Remove soldier into "my_data"
    try:
        remove_soldier(id_input, my_data)
    except KeyError as e:
        print(f"{e}, The process failed.\n")

    return


def handle_view_soldiers(my_data) -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """



def handle_add_duty(my_data) -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_update_duty_status(my_data) -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_view_soldier_duties(my_data) -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


if __name__ =="__main__":
    main(db)