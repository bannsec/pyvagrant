
from appdirs import AppDirs
import os

appdirs = AppDirs("pyVagrant", "Michael Bann")
os.makedirs(appdirs.user_data_dir, exist_ok=True)
os.makedirs(appdirs.user_config_dir, exist_ok=True)
os.makedirs(appdirs.user_cache_dir, exist_ok=True)
os.makedirs(appdirs.user_log_dir, exist_ok=True)

