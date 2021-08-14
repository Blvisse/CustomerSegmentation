"""
This script contains eda scripts
"""
import pandas as pd
import numpy as np
import logging
from scipy import stats
import mlflow 
import logging
import sys

logging.basicConfig(filename='../logs/cleanData.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

def num_nulls(data):
    try:
        logging.debu("")
        sumMissing=data.isna().sum()
        percenategeMissing=sumMissing/len(data)*100

        loggin.info("")

        missingValue=pd.DataFrame(data=[sumMissing,percenategeMissing])
        missingValue=missingValue.T
        missingValue.columns=["Total Missing","Percenated Missing"]
        
        logging.info("")
        print("") 

        return missingValue
    except Exception as e:


def num_nulls(data):

    try:
        logging.debug("Calculating the missing values")

        sumMissing=data.isna().sum()
        percentageMissing=sumMissing/len(data)*100

        #create a dataframe to present the findings
        logging.info("Creating Dataframe")

        missingValues=pd.DataFrame(data=[sumMissing,percentageMissing])
        missingValues=missingValues.T
        missingValues.columns=['Total Missing','Percentage Missing']

        logging.info("Missing Values calculated")
        print("The report of missing values is as follows")


        return missingValues



    except Exception as e:
            logging.error("Error message {} ".format(e.__class__))
            print("The following error occured{} ".format(e.__class__))
            sys.exit("The system run into an error")
def drop_duplicate(data):


    # This function looks for duplicates and drops them 
    try:

        logging.debug("Launching duplicates search")
        print("Droppping duplicates\n")
        data=data.drop_duplicates()
        dupCount=len(data)-len(data.drop_duplicates())
        print ("There are {} duplicates in the dataset\n".format(dupCount))
        logging.info("Number of duplicates in the datset are {} ".format(dupCount))

        print("Done dropping duplicates! \n")

        return data 

    except Exception as e:
        logging.info("An erro has occured")
        logging.error("The follocing error occured {} ".format(e.__class__))
        print("The following error occured {} ".format(e.__class__))
        sys.exit(1)

def valueCounts(self,columns):
        # function to calculate the number of records per each unique value
    try:

        logging.debug("Value counts of {} column".format(columns))
        count=data[columns].value_counts()
        countDF=pd.DataFrame(data=[count])
        count=count.T 

        return count
    except Exception as e:
        logging.info("An erro occured")
        logging.error("The following error occured {} ".format(e.__class__))
        print("The following error occured {} ".format(e.__class__))
        sys.exit(1)

