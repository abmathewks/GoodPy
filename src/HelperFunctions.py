

import os 
import datetime
import calendar


def CreateProjectFiles(PROJECT_PATH):

    """

    # Goal:
    Generate project folders for a new project
  
    # Output
    Creates a number of folders in the specified PROJECT_PATH
  
    # Parameters
    PROJECT_PATH: Main project path

    """

    print("CreateProjectFiles: Function initalized")

    if os.path.exists(PROJECT_PATH) and any(os.scandir(PROJECT_PATH)):
        folders = ["data", "deploy", "docs", "models", "notebooks", 
                   "scripts", "tests", "utils"]    

        for each_folder in folders:
            os.makedirs(os.path.join(PROJECT_PATH, each_folder))

        print("CreateProjectFiles: Function run completed")

    elif not os.path.exists(PROJECT_PATH):
        print("CreateProjectFiles: Project directory does not exist")





def AddMonths(DATE_VAL, 
              ADD_N,
              DATE_FORMAT = "%Y-%m-%d"):

    """

    # Goal:
    Take a date output and add N months to it
  
    # Output
    Creates a new date value
  
    # Parameters
    DATE_VAL: Initial date value
    ADD_N: Number of months to add to the original date
    DATE_FORMAT: Format of the date value

    """

    print("AddMonths: Function initalized")

    FUNCTION_OUTPUT = dict()

    FUNCTION_OUTPUT['ORIGINAL_DATE'] = DATE_VAL
    FUNCTION_OUTPUT["ADD_N"] = ADD_N

    START_DATE = datetime.datetime.strptime(DATE_VAL, DATE_FORMAT)

    DAYS_IN_MONTHS = calendar.monthrange(START_DATE.year, START_DATE.month)[1]

    NEW_DATE = START_DATE + datetime.timedelta(days = DAYS_IN_MONTHS)

    FUNCTION_OUTPUT['NEW_DATE'] = NEW_DATE.strftime(DATE_FORMAT) 

    print("AddMonths: Function run completed")

    return FUNCTION_OUTPUT







