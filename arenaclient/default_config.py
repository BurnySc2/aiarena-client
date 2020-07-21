#########################################################
#                                                       #
# DEFAULT CONFIG                                        #
#                                                       #
# !!!! DO NOT UPDATE THIS FILE WITH LOCAL SETTINGS !!!! #
# Create a config.py file to override config values     #
#                                                       #
#########################################################
import logging
import os
import platform

# GERERAL
from arenaclient.matches import FileMatchSource

ARENA_CLIENT_ID = "aiarenaclient_000"
API_TOKEN = "12345"
ROUNDS_PER_RUN = 5  # Set to -1 to ignore this
SHUT_DOWN_AFTER_RUN = True
USE_PID_CHECK = False
DEBUG_MODE = True
PYTHON = "python3"
RUN_LOCAL = False
CLEANUP_BETWEEN_ROUNDS = True
SYSTEM = platform.system()
SC2_PROXY = {"HOST": "127.0.0.1", "PORT": 8765}

# LOGGING
LOGGING_HANDLER = logging.FileHandler("supervisor.log", "a+")
LOGGING_LEVEL = 10

# PATHS AND FILES
TEMP_PATH = "/tmp/aiarena/"
LOCAL_PATH = os.path.dirname(__file__)
WORKING_DIRECTORY = LOCAL_PATH  # same for now
LOG_FILE = os.path.join(WORKING_DIRECTORY, "client.log")
REPLAYS_DIRECTORY = os.path.join(WORKING_DIRECTORY, "replays")
BOTS_DIRECTORY = os.path.join(WORKING_DIRECTORY, "bots")

MATCH_SOURCE_CONFIG = FileMatchSource.FileMatchSourceConfig(
    matches_file=os.path.join(WORKING_DIRECTORY, "matches"), results_file=os.path.join(WORKING_DIRECTORY, "results")
)

# STARCRAFT
SC2_HOME = "/home/aiarena/StarCraftII/"
SC2_BINARY = os.path.join(SC2_HOME, "Versions/Base75689/SC2_x64")
MAX_GAME_TIME = 60486
MAX_FRAME_TIME = 1000
STRIKES = 10
REALTIME = False
VISUALIZE = False

# Override values with environment specific config
try:
    from arenaclient.config import *
except ImportError as e:
    if e.name == "arenaclient.config":
        pass
    else:
        raise
