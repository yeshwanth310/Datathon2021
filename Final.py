#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[6]:


df=pd.read_excel('C://Users//USER//Downloads//Data challenge.xlsx',sheet_name='customer purchases')


# In[7]:


df


# In[8]:


df.head(5)


# In[9]:


df['total']=df['NumDealsPurchases']+df['NumWebPurchases']+df['NumCatalogPurchases']+df['NumStorePurchases']


# In[10]:


df


# In[13]:


df1=pd.read_excel('C://Users//USER//Downloads//Data challenge.xlsx',sheet_name='Customer details')


# In[14]:


df1


# In[17]:


df1=df1[['ID','Marital_Status','Country']]


# In[18]:


df1


# In[19]:


final=pd.merge(df1,df,on='ID',how='inner')


# In[20]:


final


# In[27]:


result=final.to_excel('C://Users//USER//Downloads//Final2.xlsx',sheet_name='Result',index=False)


# In[24]:


result


# In[25]:


result


# In[28]:


df1=pd.read_excel('C://Users//USER//Downloads//Data challenge.xlsx',sheet_name='Customer details')


# In[29]:


df1


# In[30]:


df4=df1[['ID','Country']]


# In[31]:


df4


# In[34]:


df5=pd.read_excel('C://Users//USER//Downloads//Final2.xlsx',sheet_name='Result')


# In[35]:


df5


# In[43]:


df6=[['ID','total']]


# 

# In[44]:


df6


# In[47]:


df6=df5[['ID','total']]


# In[49]:


df6


# In[50]:


final1=pd.merge(df4,df6,on='ID',how='inner')


# In[51]:


final1


# In[53]:


result1=final1.to_excel('C://Users//USER//Downloads//Final3.xlsx',sheet_name='Result1',index=False)


# In[54]:


result1


# In[ ]:




