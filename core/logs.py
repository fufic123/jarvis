import logging
import sys

CONTEXT_LEVEL = 25
logging.addLevelName(CONTEXT_LEVEL, "CONTEXT")

def context(self, message, *args, **kwargs):
    if self.isEnabledFor(CONTEXT_LEVEL):
        self._log(CONTEXT_LEVEL, message, args, **kwargs)

logging.Logger.context = context

class ColorFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[90m',
        'INFO': '\033[94m',
        'WARNING': '\033[93m',
        'ERROR': '\033[91m',
        'CRITICAL': '\033[95m',
        'CONTEXT': '\033[96m',
    }
    RESET = '\033[0m'

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        message = super().format(record)
        return f"{color}{message}{self.RESET}"

def setup_logging():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColorFormatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%H:%M:%S"
    ))

    logger = logging.getLogger("jarvis")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.propagate = False