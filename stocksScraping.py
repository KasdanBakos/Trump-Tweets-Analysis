# STOCK SCRAPING PROGRAM #

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


 
style.use('ggplot')

#FOR NYT
# start = dt.datetime(2015, 6, 1)
# end = dt.datetime(2017, 12, 8)

# df = web.DataReader('NYT', 'yahoo', start, end)
# print(df.head(100))

# df.to_csv('NYT.csv')
#df = pd.read_csv('NYT.csv', parse_dates=True, index_col=0)

# #FOR FOX
# start = dt.datetime(2015, 6, 1)
# end = dt.datetime(2017, 12, 8)

# df = web.DataReader('FOXA', 'yahoo', start, end)
# print(df.head(100))

# df.to_csv('FOX.csv')
# #df = pd.read_csv('FOX.csv', parse_dates=True, index_col=0)


# #FOR COMCAST
# start = dt.datetime(2015, 6, 1)
# end = dt.datetime(2017, 12, 8)

# df = web.DataReader('CMCSA', 'yahoo', start, end)
# print(df.head(100))

# df.to_csv('CMCSA.csv')
# #df = pd.read_csv('CMSCA.csv', parse_dates=True, index_col=0)


# #FOR CBS
# start = dt.datetime(2015, 6, 1)
# end = dt.datetime(2017, 12, 8)

# df = web.DataReader('CBS', 'yahoo', start, end)
# print(df.head(100))

# df.to_csv('CBS.csv')
# #df = pd.read_csv('CBS.csv', parse_dates=True, index_col=0)




#print(df.head())
#df["Adj Close"].plot()
#plt.show()



