import logging


logger = logging.getLogger('weapons')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("weapons_manager.log", encoding="utf-8")
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)





