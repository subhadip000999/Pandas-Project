#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


# In[3]:


mylist = [10,20,30,40]
pd.Series(data = mylist)


# In[4]:


pd.Series(data = mylist, index = ['a','b','c','d'])


# In[5]:


myarray = np.array(mylist)
myarray


# In[6]:


mydict = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
pd.Series(mydict)


# In[7]:


series1 = pd.Series([10,20,30,40], index = ['aa','bb','cc','dd'])
series1['cc']


# In[8]:


df = pd.DataFrame(np.random.randint(10, 100, 20).reshape(5,4), ['a', 'b', 'c', 'd', 'e'], ['kol', 'dub', 'lis', 'par'])
df


# In[9]:


df['dub']


# In[10]:


df[['dub','lis']]


# In[11]:


df['sml'] = df['dub'] + df['lis'] - df['par']
df


# In[12]:


df['ams'] = 63


# In[13]:


df


# In[14]:


df.drop('ams', axis = 1)   ## 1 is column, 0 is row


# In[15]:


df


# In[16]:


df.drop('sml', axis = 1, inplace = True)
df


# In[17]:


df['index'] = range(0,5)
df


# In[18]:


df.set_index('index', inplace=True)
df


# In[19]:


df.loc[:2]


# In[20]:


df.loc[df.index[1:3],['dub','lis']]


# In[21]:


df.reset_index(inplace = True)
df


# In[22]:


(df > 0).all()


# In[23]:


(df > 0).any()


# In[24]:


df.empty


# In[25]:


from io import StringIO


# In[26]:


## data = "       "
## pd.read_csv(StringIO(data))


# In[27]:


a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a,b))
c


# In[28]:


df1 = pd.read_excel('Superstore.xlsx')
df1.head(2)


# In[29]:


df1.loc[:,['Sales','Profit']].applymap(lambda x:x+1) #The applymap() function is used to apply a function to a Dataframe elementwise.


# In[30]:


df2 = pd.DataFrame({
    'a' : ['1.1b','2.2.b','3.3b'],
    'b' : ['4.4b', '5.5c', '6.6c']
})
df2


# In[31]:


df2.applymap(lambda x:x[:-1])


# In[32]:


df1.head(3)


# In[33]:


df1.Region.nunique()


# In[34]:


df3 = pd.read_excel('abc-products.xlsx')
df3.head(3)


# In[35]:


df3.groupby('Product Name')['Quantity'].count()


# In[36]:


df3[df3.Quantity == 10]


# In[37]:


df4 = df3['Product Name'].value_counts()
df4


# In[38]:


df1.head(2)


# In[39]:


df1.loc[df1['Profit']> 150 ].head(2)


# In[40]:


df1.loc[df1['Profit'] > 800].head(2)


# In[41]:


(df1['Sub-Category']=='Machines').sum()


# In[42]:


((df1['Sub-Category']=='Copiers')&( df1['City']=='New York City')).sum()


# In[43]:


len(pd.unique(df1['Category']))


# In[44]:


pd.unique(df1['Category'])


# In[45]:


df1.loc[((df1['Sub-Category']=='Copiers')&( df1['City']=='New York City'))].head(2)


# In[46]:


df1.loc[df1['Sub-Category'] == 'Copiers'].sort_values('Profit', ascending=False).head(2)


# In[47]:


df1.loc[df1['Quantity'].isin({1,2})].head(2)


# In[48]:


df1.loc[(df1['City']=='Henderson')& df1['Category'].isin({'Furniture','Office Supplies'})].head(2)


# In[53]:


df1.loc[df1['City']=='Henderson'].sort_values(by=['Sales','Profit'],ascending=False).head(2)


# In[ ]:




