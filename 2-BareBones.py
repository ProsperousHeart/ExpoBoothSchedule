# =================================================
# PROJECT:  EXPO BOOTH SCHEDULE
#
# Github Link:
# https://github.com/ProsperousHeart/ExpoBoothSchedule
#
# Here is the process I follow for this
# 3rd "bare bones" phase ...
#
#   1 - write out the comments of expected functions
#   2 - create those functions with proper docstrings,
#       logging, and pass ONLY
#       NOTE:  pass is a null operation (nothing happens) and is therefore
#              only used as a placeholder when no code needs to be executed
#              such as when a function doesn't do anything yet or have logging
#   3 - tie the functions together in your __main__
#   4 - test the logic with print or logging statements
# =================================================

# import pandas as pd

# =============================================================================
# LOGGING SETUP - more information on logging can be found here:
#   www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging
#   www.digitalocean.com/community/tutorials/how-to-use-logging-in-python3
#   www.loggly.com/ultimate-guide/python-logging-basics
# =============================================================================

import logging
logging.basicConfig(
    filename='ExpoBoothSchedule-Step3.log', # consider using formatting instead
    filemode='w',                           # overwrites the file every time
    level=logging.DEBUG,                    # lowest logging level
    format="%(asctime)s|%(levelname)s: %(name)s @ %(lineno)d|%(message)s"
    )

# setup logging buffer for console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG) # all DEBUG or higher will show on console

# set format easy for console to use
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger(__name__).addHandler(console)
logger = logging.getLogger(__name__)

# =============================================================================

# wrapper function - pulled from:
# https://realpython.com/primer-on-python-decorators/
import functools
def debug_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug('Starting {}()...'.format(func.__name__))
        rtn_data = func(*args, **kwargs)
        logger.debug('Ending {}()...'.format(func.__name__))
        return rtn_data
    return wrapper

# =============================================================================

# function to pull in data
#   1. pull in top 10 sessions data
#   2. pull in ranked requests

@debug_wrapper
def get_Sessions(gsuite: bool = False):
    """
    This function either takes in a Google sheet or XLSX document.
    The data to be input is the session information for the event.
    Data is limited to the culmination of sessions provided by attendee feedback.

    If GSuite is marked as TRUE, the CLI will request the URL of the Google Sheet.
    Otherwise, it will pull a file from local machine - hard coded.

    The expected file has 4 tabs:
    1. Raw Top 10       | uncleaned data
    2. Cleaned Data     | "cleaned" data from participants
    3. Top 10 Agenda    | session data for accumulated "top 10" (may be more than 10 per day)
    4. Booth Schedule   | likely not to be used with this program (manual schedule)

    This function focuses on tab 3.

    Returns a pandas DataFrame.
    """

    if gsuite == True:
        logger.debug('Google Sheet (gsuite) was true - need to get link to use.')
    else:
        logger.debug('File to read in was requested.')

    return


@debug_wrapper
def get_Users(gsuite: bool = False):
    """
    This function either takes in a Google sheet or XLSX document.
    The data to be input is the user session requests for the event.
    Data is limited to the culmination of sessions provided by attendee feedback.

    If GSuite is marked as TRUE, the CLI will request the URL of the Google Sheet.
    Otherwise, it will pull a file from local machine - hard coded.

    The expected file has 4 tabs:
    1. Raw Top 10       | uncleaned data
    2. Cleaned Data     | "cleaned" data from participants
    3. Top 10 Agenda    | session data for accumulated "top 10" (may be more than 10 per day)
    4. Booth Schedule   | likely not to be used with this program (manual schedule)

    This function focuses on tab 2.

    Returns a pandas DataFrame.
    """

    if gsuite == True:
        logger.debug('Google Sheet (gsuite) was true - need to get link to use.')
    else:
        logger.debug('File to read in was requested.')

    return


# create Session & User objects for sorting OR use pandas DF
@debug_wrapper
def sort_Sessions(sessions_DF, user_DF):
    """

    :param sessions_DF:
    :param user_DF:
    :return:
    """
    return

# =============================================================================

if __name__ == "__main__":
    """
    This function is only executed if run as a script.
    """

    logger.debug('Starting {}()...'.format(__name__))

    # ==========================================================
    # The functions needed are as follows:
    #   - get data input (either XLSX or Google Sheet)
    #       1. top 10 (manual) session data - to be used
    #           in creation of Session objects
    #       2. ranked session data from participants
    #   - create Session objects for each of the daily top 10
    #   - create User objects to have their preferred rankings
    #
    #   NOTE:  Be sure that you ALWAYS check the data returned
    #          This ensures you are getting the excct type of
    #          data expected as well as avoid future bugs.
    # ==========================================================

    # gather data (input)
    sessions_DF = get_Sessions()
    user_DF = get_Users()

    # create Session & User objects for sorting OR use pandas DF
    sort_Sessions(sessions_DF, user_DF)

    # ================================================
    # Nice to have needs:
    #   - creation of schedule vs just pulling info
    #   - way to store info (database)
    #   - way to retrieve info
    #   - way to email
    #   - possibly Jinja2 for a nice HTML look
    # ================================================

    logger.debug('Ending {}()...'.format(__name__))