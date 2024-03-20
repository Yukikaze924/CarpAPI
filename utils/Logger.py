
import logging

from rich.logging import RichHandler


class Log:

    @staticmethod
    def getLogger():
        FORMAT = "%(message)s"
        logging.basicConfig(
            level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
        )
        log = logging.getLogger("rich")
        return log