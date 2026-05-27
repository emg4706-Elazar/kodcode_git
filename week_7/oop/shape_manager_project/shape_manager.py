import logging
from rectangle import Rectangle
from circle import Circle
from square import Square


class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):
        pass








    def get_all_shapes(self):
        pass

    def update_shape(self, shape_id, new_data):
        pass

    def delete_shape(self, shape_id):
        pass

    def save_to_json(self):
        pass

    def load_from_json(self):
        pass



def get_logger():
    l = logging.getLogger('shapes')
    l.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("shape_manager.log", encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    l.addHandler(file_handler)

    return l



