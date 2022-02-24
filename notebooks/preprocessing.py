import pandas as pd
import re


def preprocess (location, returnType): 
    """
    Method to preprocess dataframe given by pandas reader.
    """
    df = pd.read_csv(location, delimiter=';', header=None)
    # Drops NaN Columns
    df = df.drop([df.columns[3]], axis=1)

    
    
    if(returnType == 'df'):
        return df
    elif(returnType == 'list'):
        return df.astype(str).values.tolist()

def tokenize(df):
    """
    Tokenizes cleaned artificial logs. Returns 2D List containing Tokens for each row.
    """
    return df.values.tolist()

def cleanLog(location):
    """
    Cleans log on given location of ['TimeStamp:', 'Trace ID:', 'Activity Name:'] and saves it under <location>_clean. Useful for artifical logs.
    """
    with open(location, 'r') as f:
        original_csv = f.read()

    subStrings = ['TimeStamp:', 'Trace ID:', 'Activity Name:'] #Strings to delete out of csv log.

    clean_csv = re.sub(subStrings[0],'', original_csv)
    clean_csv = re.sub(subStrings[1],'', clean_csv)
    clean_csv = re.sub(subStrings[2],'', clean_csv)

    with open(location+'_clean', 'w') as f:
        f.write(clean_csv)

def loadLog(log, returnType):
    """
    Method to manage different logs.
    """
    if(log == 'basic'):
        retVal = preprocess('../logs/basic_log_clean.csv',returnType)
        return retVal


def test_run():
    df = pd.read_csv('../logs/basic_log.csv', delimiter=';', header=None)
    preprocess(df)


if __name__ == "__main__":
    test_run()