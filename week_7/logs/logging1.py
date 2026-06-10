import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logging1.log", encoding="utf-8")
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
stream_handler = logging.StreamHandler()

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)




# exercise 1
def add(a, b):
    logger.info("start to add numbers: %s, %s",a, b)
    try:
        result = a + b
        logger.info("The numbers was added successfully: %s, %s", a, b)
        return result
    except TypeError as e:
        logger.error("adding failed: %s", e)

    return None



# exercise 3
# existed function
def save_tasks(filename, tasks):
    logger.info("Start to save tasks into %s", filename)
    try:
        with open(filename, "a", encoding="utf-8") as f:
            for d in tasks:
                row = f"{d['id']}|{d['status']}|{d['description']}\n"
                f.write(row)
        logger.info("End to save into %s", filename)
    except Exception as e:
        logger.error("saving failed %(e)s")

    return

add(3,4)

