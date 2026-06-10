import logging


logger = logging.getLogger('Server')
logger.setLevel("DEBUG")

file_handler = logging.FileHandler('store.log', encoding="utf-8")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(name)s | %(levelname)s | %(asctime)s | %(msg)s"
)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)



