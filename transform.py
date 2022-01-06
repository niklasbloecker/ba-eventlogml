from numpy import vectorize
import pandas as pd
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.cluster import KMeans

def oneString(file, returnVal):
    """Reads given csv and returns traces in one row and as a combined String.
    """

    df = pd.read_csv(file)
    cases = df.case.unique()

    liste = []

    for case in cases:
        df_loop = df[df.case == case]
        case_list = []
        for i in range(len(df_loop)):
            temp = df_loop.iloc[[i]]
            case_list.extend(temp.values.tolist()[0])
        case_string=','.join([str(item) for item in case_list])
        liste.append(case_string)
        #print(f"{case} to list added")

    columns = df.columns.tolist()

    df_merged = pd.DataFrame(liste)
    
    if(returnVal == 'df'):
        return df_merged
    elif(returnVal == 'list'):
        return liste
    else:
        print("oneString needs returnVal to be df/list")
        exit()

def valueTable(file, returnVal):
    """Reads given csv and returns traces in one row with all attributes of the other rows concatenated.
    """

    df = pd.read_csv(file)
    cases = df.case.unique()

    liste = []

    for case in cases:
        df_loop = df[df.case == case]
        case_list = []
        for i in range(len(df_loop)):
            temp = df_loop.iloc[[i]]
            case_list.extend(temp.values.tolist()[0])
        liste.append(case_string)
        #print(f"{case} to list added")

    columns = df.columns.tolist()

    df_merged = pd.DataFrame(liste)
    
    if(returnVal == 'df'):
        return df_merged
    elif(returnVal == 'list'):
        return liste
    else:
        print("valueTable needs returnVal to be df/list")
        exit()

def main():
    liste = oneString('logs/sepsis.csv','list')
    vectorizer = HashingVectorizer(n_features=10000,norm=None,alternate_sign=False)
    X = vectorizer.fit_transform(liste)
    kmeans = KMeans(n_clusters = 2).fit(X)
    print(liste)

if __name__ == "__main__":
    main()