import logging

def get_logger():
    l = logging.getLogger('messages')
    l.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('intel_messages_dal.log')
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )
    file_handler.setFormatter(formatter)
    l.addHandler(file_handler)
    l.addHandler(stream_handler)
    return l
l1 = get_logger()
















