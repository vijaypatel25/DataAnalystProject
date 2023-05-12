#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Import libraries

import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)  # Adjusts the configuration of the plots we will create

# Read in the data

df = pd.read_csv(r'C:\Users\Vijay Patel\Downloads\movies.csv')


# In[10]:


# Let's Look at the data

df.head()


# In[11]:


# To see if there is missing data

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[12]:


# Data types for our columns

print(df.dtypes)


# In[13]:


# Are there any Outliner?

df.boxplot(column=['gross'])


# In[14]:


df.drop_duplicates()


# In[15]:


# Order our Data a little bit to see

df.sort_values(by=['gross'], inplace=False, ascending=False)


# In[32]:


sns.regplot(x="gross", y="budget", data=df, scatter_kws={"color":"red"}, line_kws={"color":"blue"})


# In[22]:


sns.regplot(x="score", y="gross", data=df)


# In[ ]:


# change data type of columns  drop the 0 after the decimal point
df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')


# In[23]:


# Create correct year column

df['yearcorrect'] = df['released'].astype(str).str[:4]

df


# In[28]:


# Highest gross film

df = df.sort_values(by=['gross'], inplace=False, ascending=False)


# In[25]:


# Put scroll option on the right

pd.set_option('display.max_rows', None)


# In[26]:


# Drop any duplicates

df['company'].drop_duplicates().sort_values(ascending=False)


# In[31]:


# Budget high correlation
# company high correlation
# Scatter plot with budget vs gross

plt.scatter(x=df['budget'], y=df['gross'])
plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earning')
plt.ylabel('Budget for Film')

plt.show()


# In[29]:


df.head()


# In[35]:


# Looking at Correlation

df.corr(method='pearson') #pearson, kendall, spearman


# In[37]:


correlation_matrix = df.corr(method='pearson')
sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlation matrix for Numeric Features")
plt.xlabel("Movie Features")
plt.ylabel("Movie Features")
plt.show()


# In[40]:


correlation_mat = df.apply(lambda x: x.factorize()[0]).corr()

corr_pairs = correlation_mat.unstack()

print(corr_pairs)


# In[41]:


sorted_pairs = corr_pairs.sort_values()

sorted_pairs


# In[42]:


high_corr = sorted_pairs[(sorted_pairs) > 0.5]

high_corr


# In[44]:


# Looking at the top 15 companies by gross revenue

CompanyGrossSum = df.groupby('company')[["gross"]].sum()
CompanyGrossSumSorted = CompanyGrossSum.sort_values('gross', ascending = False)[:15]
CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64')
CompanyGrossSumSorted


# In[45]:


df['Year'] = df['released'].astype(str).str[:4]
df


# In[ ]:


sns.stripplot(x="rating", y="gross", data=df)


# In[ ]:


sns.swarmplot(x="rating", y="gross", data=df)

