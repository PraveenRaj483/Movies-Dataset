#!/usr/bin/env python
# coding: utf-8

# IMPORT NECESSARY LIBRARIES

# In[117]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#!/usr/bin/env python
# coding: utf-8

# IMPORT NECESSARY LIBRARIES

# In[9]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# LET'S SEE OUR BASIC DATASET

# In[10]:


raw =  pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
raw.head()


# In[11]:


raw.shape


# In[12]:


raw["Age"].isnull().sum()


# In[13]:


raw["Age"] =raw['Age'].replace(np.nan , 0)
raw["Age"].value_counts()


# In[14]:


raw['Directors'].value_counts()[:20]


# In[15]:


directors = [raw['Directors'].value_counts()[:10]]
directors=pd.DataFrame(directors)
directors =directors.transpose()

directors=directors.reset_index()
plt.figure(figsize=(10,6),dpi=100)
plt.barh(directors["index"], directors['Directors'])
plt.show()



# SO MOST ONLINE PLATFORM RELEASED DIRECTORS "JAY CHAPMAN", "RAUL CAMPOS,JAN SUTER" ,"JAY KARAS"

# In[16]:


review = raw[['Title','Directors','IMDb','Rotten Tomatoes']]
review.head()


# I create seperate dataset for review analysis for our convinience

# In[17]:


review = review.sort_values("IMDb" ,ascending =False )
review['IMDb'] =  review['IMDb'].str[:3].astype('float')

review.head()


# In[18]:


plt.figure(figsize=(10,6),dpi=100)
plt.barh(review['Title'][:10], review['IMDb'][:10])
plt.show()


# By IMDB Top 3 highrated movies are "Ruby's Studio: the Feelings Show" 'Ostatni ludzie Czarnobyla' 'Jingle Pols'

# In[19]:


review = review.sort_values("IMDb")


plt.figure(figsize=(10,6),dpi=100)
plt.barh(review['Title'][:10], review['IMDb'][:10])
plt.show()


# By IMDB Top 3 low rated movies are "Finding Jesus" "Izzie's Way Home" 'Aerials'

# In[20]:


review = review.sort_values("Rotten Tomatoes" , ascending = False)
review["Rotten Tomatoes"] = review["Rotten Tomatoes"].str[:2].astype('float')
plt.figure(figsize=(10,6),dpi=100)
plt.barh(review['Title'][:10], review["Rotten Tomatoes"][:10])
plt.show()


# By Rotten Tomatoes Top 3 highrated movies are "The Irishman" 'Dangal' 'Mary Poppins' . So IMDb and Rotten Tomatoes not having a
# single common movies in the top list . So they have different opinions maybe

# In[21]:


review = review.sort_values("Rotten Tomatoes" )
plt.figure(figsize=(10,6),dpi=100)
plt.barh(review['Title'][:10], review["Rotten Tomatoes"][:10])
plt.show()


# By Rotten Tomatoes Top 3 low rated movies too not common IMDB

# In[22]:


review.head()


# In[23]:


review = review.sort_values("IMDb" , ascending =False)
review = review.replace(np.nan ,"Unknown")
review.head()


# In[24]:


plt.figure(figsize=(10,6),dpi=100)
plt.barh(review['Directors'][:10], review["IMDb"][:10])
plt.show()


# In[25]:


raw.head()


# In[36]:


raw['Netflix'].value_counts()


# In[37]:


raw['Hulu'].value_counts()


# In[38]:


raw['Prime Video'].value_counts()


# In[39]:


raw['Disney+'].value_counts()


# In[44]:


label = ['Netflix','Prime Video', 'Disney+','Hulu']
values =[ 3695,1047,4113,922]
plt.pie(values ,labels = label, autopct='%1.0f%%')
plt.show()


# So as per the data "Disney+" contains 42% of movies and "Netflix" have 38% movies

# In[65]:


netflix = pd.DataFrame(raw , columns =['Netflix','Runtime'])


netflix.sample(10)


# In[71]:


netflix = netflix[netflix['Netflix'] == 1]

netflix.sample(10)


# In[73]:


netflix.describe()


# we got almost equal values of mean , median in runtime so this is Normal distribution .No Problem!!

# In[75]:


plt.figure(figsize=(10,6),dpi=300)
plt.hist(netflix['Runtime'])
plt.show()


# so Most of the Netflix movies having a 100 minuets of runtime

# In[77]:


Disney = pd.DataFrame(raw , columns =['Disney+','Runtime'])
Disney = Disney[Disney['Disney+'] == 1]
Disney.sample(10)


# In[78]:


Disney.describe()


# mean is less than median ,so it is left skewed distribution we can expect some outliers in minimum side 

# In[79]:


plt.figure(figsize=(10,6),dpi=300)
plt.hist(Disney['Runtime'])
plt.show()


# disney is almost having most of values around a 100 minutes like Netflix

# In[80]:


prime = pd.DataFrame(raw , columns =['Prime Video','Runtime'])
prime = prime[prime['Prime Video'] == 1]
prime.sample(10)


# In[81]:


prime.describe()


# this is almost normal distribution, however mean was higher tham so right skewed distribution we can expect some outliers

# In[82]:


plt.figure(figsize=(10,6),dpi=300)
plt.hist(prime['Runtime'])
plt.show()


# prime mostly having around 80-90 minutes contents.

# In[83]:


hulu = pd.DataFrame(raw , columns =['Hulu','Runtime'])
hulu = hulu[hulu['Hulu'] == 1]
hulu.sample(10)


# In[84]:


hulu.describe()


# this is almost normal distribution, however mean was higher tham so right skewed distribution we can expect some outliers

# In[85]:


plt.figure(figsize=(10,6),dpi=300)
plt.hist(hulu['Runtime'])
plt.show()


# hulu mostly having around 70-90 minutes contents.

