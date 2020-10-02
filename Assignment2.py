
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. This is the dataset to use for this assignment. Note: The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[1]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np
import datetime as dt
def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# In[33]:


data = pd.read_csv("data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv")
df = pd.DataFrame(data)
df["Date"] =  pd.to_datetime(df['Date'])
df = df.sort_values(by = "Date")
df_2015 = df[df['Date'] >= '2015-01-01']
df = df.loc[df['Date'] <= '2014-12-31']
df = df.loc[~(df['Date'].dt.month.eq(2) & df['Date'].dt.day.eq(29))]
df['month'] = df.Date.dt.month
df['day'] = df.Date.dt.day

df.set_index('Date', inplace = True)
df = df.groupby(['month', 'day']).agg({"Data_Value": ['max', 'min']})
df = df.reset_index()

df_2015 = df_2015.loc[~(df_2015['Date'].dt.month.eq(2) & df_2015['Date'].dt.day.eq(29))]
df_2015['month'] = df_2015.Date.dt.month
df_2015['day'] = df_2015.Date.dt.day

df_2015.set_index('Date', inplace = True)
df_2015 = df_2015.groupby(['month', 'day']).agg({"Data_Value": ['max', 'min']})
df_2015 = df_2015.reset_index()


plt.figure()
plt.rcParams.update({'figure.max_open_warning': 0})
plt.plot((df['Data_Value']['max']), '.',(df['Data_Value']['min']), '.')

plt.gca().fill_between(range(len(df['Data_Value']['max'])), 
                       df['Data_Value']['max'], df['Data_Value']['min'], 
                       facecolor='black', 
                       alpha=0.50)
m = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
# This is the vital step. It will create a list of day numbers corresponding to middle of each month i.e. 15(Jan), 46(Feb), ... 
ticks = [(dt.date(2017,m,1)-dt.date(2016,12,15)).days for m in range(1,13)]
# It is important to use a non-leap year for this calculation (I used 2017).
# Also, I used (2016,12,15) to substract so that I get middle of each month rather than beginning, it just looks better that way.
ax = plt.gca()
ax.set_xticks(ticks)
ax.set_xticklabels(m)
plt.xlabel('Months')
plt.ylabel('Degree')
plt.title('Highest and Lowest Degrees For Everyday Between 2005-2014')

for every in range(len(df_2015['Data_Value']['max'])):
    if list(df_2015['Data_Value']['max'])[every] > list(df['Data_Value']['max'])[every]:
        string = str(df_2015['month']) + "-" + str(df_2015['day'])  
        plt.plot((list(df_2015['Data_Value']['max'])[every]), '.', c = 'red')
     
for every in  range(len(df_2015['Data_Value']['min'])):
    if list(df_2015['Data_Value']['min'])[every] < list(df['Data_Value']['min'])[every]:
        plt.plot((list(df_2015['Data_Value']['min'])[every]), '.', c = 'red')

        
plt.show()


# In[ ]:




# In[ ]:



