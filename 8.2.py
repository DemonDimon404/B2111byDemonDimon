import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='logs_p8.2.log',
                    filemode='w',
                    format="we have message: %(astime)s%(levelname)s - %(message)s")

try:
    print(10/0)
except Exception:
    logging.exception("exception")