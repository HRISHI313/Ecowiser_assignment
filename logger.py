import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m,%d,%Y,%H,%M,%S')}.log"
LOG_PATH = os.path.join(os.getcwd(), 'Logs')

os.makedirs(LOG_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
