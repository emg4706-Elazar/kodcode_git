import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logging_exercise2.log", encoding="utf-8")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)



# exercise 6
def process_payment(user_id, amount):
    logger.info(f"Starting payment for user {user_id}")
    if amount <= 0:
        logger.error("Invalid amount")
        return
    if amount > 10000:
        logger.warning("Large transaction")
    logger.info(f'Payment of {amount} completed for user {user_id}')


# exercise 7
def add(a, b):
    logger.info("starting add: %s, %s",a, b)
    try:
        result = a + b
        logger.info("numbers was added successfully: %s, %s", a, b)
        return result
    except TypeError as e:
        logger.error("adding failed: %s", e)

    return None


# exercise 8
def read_config(filepath):
    logger.debug(f"start read configuration of file in path '{filepath}'")
    try:
        with open(filepath) as f:
            data = f.read()
        logger.info(f"success to read in path '{filepath}'")
        return data
    except FileNotFoundError as e:
        logger.exception(f"{e}")
        return None


# exercise 8





# exercise 14
def process_request(request_id, user_id, action):
    log_extra = {
        "request_id": request_id,
        "user_id": user_id
    }

    logger.info("Start to process request", extra=log_extra)
    logger.info("Processing request", extra=log_extra)
    logger.info("End to process request", extra=log_extra)

    return



############################################
logger2 = logging.getLogger("payments")
file_handler2 = logging.FileHandler("app.log", encoding="utf-8")
formatter2 = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s"
)
file_handler2.setFormatter(formatter2)
logger2.addHandler(file_handler2)


def make_log(level, msg):
    if level == "debug":
        logger.debug(msg)
    elif level == "info":
        logger.info(msg)
    elif level == "warning":
        logger.warning(msg)
    elif level == "error":
        logger.error(msg)

    return

