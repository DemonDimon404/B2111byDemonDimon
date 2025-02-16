import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='logs_p8.log',
                    filemode='w',
                    format="we have message: %(astime)s%(levelname)s - %(message)s")

logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")
