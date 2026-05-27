

def get_input():
    choice = input("Enter your choice: ")
    return choice

def print_available_shapes():
    print(
        "==== All Shapes =====\n",
        "1. Rectangle\n",
        "2. Square\n",
        "3. Circle\n"
    )
    return


def handle_create_shape():
    """
    1. print available shapes.
    2. get valid input from user
    3. get valid input for attributes shape
    4. create this shape
    5. append to all shapes
    :return:
    """
    print_available_shapes()
    user_choice = get_input()
    pass



def handle_read():
    """
    1. get all shapes from shape_manager
    2. print all shapes with loop,
    :return:
    """
    pass


def handle_update_shape():
    """
    1. get valid input
        a. id_shape
        b. new_data

    2. get all shapes
    3. change the shape by id_shape(try/except),
        It's a function with condition to check,
        if this shapes exist.
    4. print match message
    :return: None
    """
    pass


def handle_delete_shape():
    """
    1. get valid input
        a. id_shape

    2. get all shapes
    3. delete the shape by id_shape(try/except),
        It's a function with condition to check,
        if this shapes exist.
    4. print match message
    :return: None
    """
    pass










