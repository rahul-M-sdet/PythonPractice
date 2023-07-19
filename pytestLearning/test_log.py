import logging

def test_getLogger():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")
    formatter =logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)
    logger.debug("A debug stmt is executed.")
    logger.info("Some info to be printed")
    logger.error("A major error has happened.")
    logger.critical("Something went wrong")
