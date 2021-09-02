#!/usr/bin/env python
# coding: utf-8

# IMPORT NECESSARY LIBRARIES

# In[117]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# LET'S SEE OUR BASIC DATASET

# In[118]:


raw =  pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
raw.head()


# In[119]:


raw.shape


# In[120]:


raw["Age"].isnull().sum()


# In[121]:


raw["Age"] =raw['Age'].replace(np.nan , 0)
raw["Age"].value_counts()


# In[122]:


raw['Directors'].value_counts()[:20]


# In[123]:


directors = [raw['Directors'].value_counts()[:10]]
directors=pd.DataFrame(directors)
directors =directors.transpose()

directors=directors.reset_index()
plt.figure(figsize=(10,6),dpi=100)
plt.barh(directors["index"], directors['Directors'])
plt.show()



# SO MOST ONLINE PLATFORM RELEASED DIRECTORS "JAY CHAPMAN", "RAUL CAMPOS,JAN SUTER" ,"JAY KARAS"

# In[124]:


review = raw[['Title','Directors','IMDb','Rotten Tomatoes']]
review.head()

I create seperate dataset for review analysis for our convinience
# In[125]:


review = review.sort_values("IMDb" ,ascending =False )
review['IMDb'] =  review['IMDb'].str[:3].astype('float')

review.head()


# In[126]:


plt.figure(figsize=(10,6),dpi=100)
plt.barh(review['Title'][:10], review['IMDb'][:10])
plt.show()


# By IMDB Top 3 highrated movies are "Ruby's Studio: the Feelings Show" 'Ostatni ludzie Czarnobyla' 'Jingle Pols'

# In[127]:


review = review.sort_values("IMDb")


plt.figure(figsize=(10,6),dpi=100)
plt.barh(review['Title'][:10], review['IMDb'][:10])
plt.show()


# By IMDB Top 3 low rated movies are "Finding Jesus" "Izzie's Way Home" 'Aerials'

# In[128]:


review = review.sort_values("Rotten Tomatoes" , ascending = False)
review["Rotten Tomatoes"] = review["Rotten Tomatoes"].str[:2].astype('float')
plt.figure(figsize=(10,6),dpi=100)
plt.barh(review['Title'][:10], review["Rotten Tomatoes"][:10])
plt.show()


# By Rotten Tomatoes Top 3 highrated movies are "The Irishman" 'Dangal' 'Mary Poppins' . So IMDb and Rotten Tomatoes not having a
# single common movies in the top list . So they have different opinions maybe

# In[129]:


review = review.sort_values("Rotten Tomatoes" )
plt.figure(figsize=(10,6),dpi=100)
plt.barh(review['Title'][:10], review["Rotten Tomatoes"][:10])
plt.show()


# By Rotten Tomatoes Top 3 low rated movies too not common IMDB

# In[130]:


review.head()


# In[144]:


review = review.sort_values("IMDb" , ascending =False)
review = review.replace(np.nan ,"Unknown")
review.head()


# In[146]:


plt.figure(figsize=(10,6),dpi=100)
plt.barh(review['Directors'][:10], review["IMDb"][:10])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




