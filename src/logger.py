from datetime import datetime
import logging
import os

log_file = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
LOGS_folder = os.path.join(os.getcwd(),"LOGS",log_file)
os.makedirs(LOGS_folder,exist_ok = True)

log_file_path = os.path.join(LOGS_folder,log_file)

logging.basicConfig(
    filename = log_file_path,
    level = logging.INFO,
    format = "%(asctime)s : %(name)s : %(levelname)s : %(message)s"
)