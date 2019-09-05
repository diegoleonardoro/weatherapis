#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
from citipy import citipy
import numpy as np
import requests
import json


# In[3]:


# np.random.uniform:
# Samples are uniformly distributed over the half-open interval [low, high) (includes low, but excludes high). 
# In other words, any value within the given interval is equally likely to be drawn by uniform.


# In[4]:


lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
cities = []


for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name  
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)
        


# In[5]:


url = "https://api.openweathermap.org/data/2.5/weather?q= CITY &APPID=031ad12ed03c53ab328ec8e6b0885922"

urls = []
for city in cities:
    x = url.replace("CITY", city)
    urls.append (x)

responses= []
for u in urls:
    response = requests.get(u).json()
    x = response
    responses.append (x)
    


# In[ ]:





# In[7]:


cities_weather_info =  []
for response in responses:
    try: 
        x = {"Latitude":response["coord"]['lat'],
             "Humidity": response["main"]["humidity"],
        "Longitude": response["coord"]['lon'], 
        "Temperature": response["main"]["temp"], 
        "Cloudiness": response["clouds"]["all"],
        "Wind Speed": response["wind"]["speed"],
        "City Name": response["name"], 
        "City id" : response["id"]}
        cities_weather_info.append (x)
    except KeyError:
        continue 


# In[21]:


cities_info_df = pd.DataFrame(cities_weather_info )


# In[22]:


cities_info_df.head()


# In[23]:


#* Temperature (F) vs. Latitude
#* Humidity (%) vs. Latitude
#* Cloudiness (%) vs. Latitude
#* Wind Speed (mph) vs. Latitude


# In[42]:


plt.scatter(cities_info_df["Latitude"],cities_info_df["Temperature"] )
plt.grid()
plt.title ("City Latitude Vs Temperatute")
plt.ylabel ("Max Temperature")
plt.xlabel ("Latitude")


# In[38]:


plt.scatter(cities_info_df["Latitude"] , cities_info_df["Humidity"])
plt.grid()

plt.title ("City Latitude Vs Humidity")
plt.ylabel ("Max Temperature")
plt.xlabel ("Latitude")


# In[39]:


plt.scatter(cities_info_df["Latitude"] , cities_info_df["Cloudiness"])
plt.grid()

plt.title ("City Latitude Vs Cloudiness")
plt.ylabel ("Max Temperature")
plt.xlabel ("Latitude")


# In[40]:


plt.scatter(cities_info_df["Latitude"] , cities_info_df["Wind Speed"])
plt.grid()

plt.title ("City Latitude Vs Wind Speed")
plt.ylabel ("Max Temperature")
plt.xlabel ("Latitude")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




