import pandas as pd
from sklearn import preprocessing
# import csv
# import json


def import_data():
    df1 = pd.read_csv('./processedoutput.csv')
    # df2 = pd.read_csv('./teamlist.csv', index_col=['Team'])
    return df1


if __name__ == "__main__":
    df = import_data()

    output = df.drop_duplicates(['Team'])
    print output.head()
    # output = df.iloc[:, 8].drop_duplicates()
    # print df.iloc[:, 9].drop_duplicates()
    # for x in range(8, 227):
    # output = pd.concat([output, df.iloc[:, 9].drop_duplicates()], axis=1)
    output.to_csv('processedoutput.csv')
    print "finished"
###########
import matplotlib.pyplot as plt
import datetime
import pandas.io.data as web
import pandas as pd
dfold = pd.read_csv('Nifty2015.csv', parse_dates=True)
dfnew=  pd.read_csv('Nifty2015New.csv', parse_dates=True)
dfnew = dfnew.drop_duplicates().fillna(0)
dfold=dfold.drop_duplicates().fillna(0)
print dfnew.tail(5)
print dfold.tail(5)
dfupdate=pd.merge(dfold, dfnew, on='Date')  
dfupdate.to_csv('NiftyFirst.csv', index=True)
#############
#