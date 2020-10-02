
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **sports or athletics** (see below) for the region of **None, None, Germany**, or **Germany** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **None, None, Germany** to Ann Arbor, USA. In that case at least one source file must be about **None, None, Germany**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **None, None, Germany** and **sports or athletics**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **sports or athletics**?  For this category we are interested in sporting events or athletics broadly, please feel free to creatively interpret the category when building your research question!
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[57]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib notebook')
plt.style.use('seaborn')

data09 = pd.read_csv('2009value.txt')
data10 = pd.read_csv('2010value.txt')
data11 = pd.read_csv('2011value.txt')
data12 = pd.read_csv('2012value.txt')
data13 = pd.read_csv('2013value.txt')
data14 = pd.read_csv('2014value.txt')
data15 = pd.read_csv('2015value.txt')
data16 = pd.read_csv('2016value.txt')
data17 = pd.read_csv('2017value.txt')
data18 = pd.read_csv('2018value.txt')
data19 = pd.read_csv('2019value.txt')
data20 = pd.read_csv('2020value.txt')

#read_file.to_csv('2020value.csv')
#read_file2020 = pd.read_csv('2020value.csv')
df_2009 = pd.DataFrame(data09)
df_2010 = pd.DataFrame(data10)
df_2011 = pd.DataFrame(data11)
df_2012 = pd.DataFrame(data12)
df_2013 = pd.DataFrame(data13)
df_2014 = pd.DataFrame(data14)
df_2015 = pd.DataFrame(data15)
df_2016 = pd.DataFrame(data16)
df_2017 = pd.DataFrame(data17)
df_2018 = pd.DataFrame(data18)
df_2019 = pd.DataFrame(data19)
df_2020 = pd.DataFrame(data20)

liv_2009 = df_2009.loc[df_2009['Team '] == 'Liverpool ']

new_df = pd.concat([df_2009,df_2010,df_2011,df_2012,df_2013,df_2014,df_2015,df_2016,df_2017,df_2018,df_2019,df_2020], axis=0)
liv = new_df.loc[new_df['Team '] == 'Liverpool ' ]
liv = liv.reset_index(drop=True)
liv = liv['Revenue ($M) ']
ars = new_df.loc[new_df['Team '] == 'Arsenal ' ]
ars = ars.reset_index(drop=True)
ars = ars['Revenue ($M) ']
final_df =pd.concat([ars, liv], axis=1, join='inner')
final_df.columns = ['Arsenal', 'Liverpool']
final_df = final_df.rename( index=lambda s: s + 2009)

final_df.plot();
plt.xlabel('Years')
plt.ylabel('Million Dollars')
plt.title('Anuual Revenue of Arsenal and Liverpool Between 2009-2020 in Million Dollars')


# In[ ]:




# In[ ]:



