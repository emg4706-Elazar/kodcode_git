from utils import find_soldier_by_id
from utils import is_valid_name

def add_soldier(soldier_id: int, name: str, my_data: list) -> None:
    """
    מוסיפה חייל חדש למערכת.

    סוג: לוגיקה עסקית (Business Logic)

    מקבלת:
        soldier_id (int): מספר אישי של החייל
        name (str): שם החייל
        my_data (list): הרשימה  של החיילים הקיימים
    מחזירה:
        None - הפונקציה מוסיפה את החייל או זורקת exception

    זורקת:
        ValueError: אם id כבר קיים במערכת
        ValueError: אם name ריק או לא תקין

    למה הפונקציה קיימת:
    לוגיקה עסקית טהורה של הוספת חייל.
    מבצעת בדיקות תקינות ומוסיפה את החייל לנתונים.
    לא מטפלת בקלט/פלט - רק בלוגיקה.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    soldier_is_exist = find_soldier_by_id(soldier_id, my_data)
    if soldier_is_exist:
        raise ValueError("This soldier is already exist.")
    if not is_valid_name(name):
        raise ValueError("Invalid name")
    else:
        new_soldier = {
            "id": soldier_id,
            "name": name,
            "duties": []
        }
        my_data.append(new_soldier)
    return

def remove_soldier(soldier_id: int, my_data:list) -> None:
    """
    מסירה חייל מהמערכת לפי id.

    סוג: לוגיקה עסקית (Business Logic)

    מקבלת:
        soldier_id (int): מספר אישי של החייל

    מחזירה:
        None - הפונקציה מסירה את החייל או זורקת exception

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת

    למה הפונקציה קיימת:
    לוגיקה עסקית של הסרת חייל.
    מבצעת בדיקת קיום ומסירה מהנתונים.
    זורקת exception במקרה שהחייל לא קיים.
    """
    exist_soldier = find_soldier_by_id(soldier_id, my_data)
    if not exist_soldier:
        raise KeyError("This soldier is not exist.")

    else:
        my_data.remove(exist_soldier)
    return


def get_all_soldiers() -> list:
    """
    מחזירה את רשימת כל החיילים במערכת.

    סוג: גישה לנתונים (Data Access)

    מקבלת: כלום

    מחזירה:
        list: רשימה של מילונים, כל מילון מייצג חייל
              רשימה ריקה אם אין חיילים

    זורקת: כלום - תמיד מחזירה רשימה (ריקה או מלאה)

    למה הפונקציה קיימת:
    גישה לנתונים בצורה מבוקרת.
    מאפשר לקבל את הנתונים מבלי לגשת ישירות למשתנה הגלובלי.
    """
    pass
