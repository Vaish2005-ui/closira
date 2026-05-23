import logging
import json


class JsonFormatter(logging.Formatter):

    def format(self, record):

        log_data = {
            "level": record.levelname,
            "message": record.getMessage()
        }

        return json.dumps(log_data)


logger = logging.getLogger("closira")

handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())

logger.addHandler(handler)
logger.setLevel(logging.INFO)