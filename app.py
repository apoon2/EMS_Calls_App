import streamlit as st
import pickle

# app title
st.title('NYC Emergency Call Volume Estimator')

# About Section
st.write('''Can we predict emergency call volume in NYC using time, weather, and traffic data? While these features are beyond our control, the goal of this project is to increase preparedness for a surge in emergency services given specific conditions. Using predictive modeling, we hope to be able to provide an indication of when the city should increase staff in emergency call centers or even on response teams.
___
### Datasets:
[EMS](https://data.cityofnewyork.us/Public-Safety/EMS-Incident-Dispatch-Data/76xm-jjuj) | [Weather](https://www.ncdc.noaa.gov/cdo-web/search) | [Traffic](https://data.ny.gov/Transportation/511-NY-Events-Beginning-2010/ah74-pg4w)

We first combined data from these three different sources to get our training dataset.

### Data Dictionary:
| Feature                   | Notes                                         |
| ---                       | ---                                           |
| Month                     | Month of the year (1-12)                      |
| Day                       | Day of the month (1-31)                       |
| Hour                      | Hour of the day (0-23)                        |
| Precipitation             | Precipitation by intensity (1-3 : L,M,H)      |
| Snow Depth                | Snow depth on ground in inches                |
| Temp (F)                  | Temperature in Fahrenheit                     |
| Traffic Incidents         | Number of traffic incidents within the hour   |

### Results:
The best performing model used here was a random forest with a max_depth of 5 and n_estimators of 250. The model had train and test r2 scores of 0.81 and a RMSE of 24 calls. Overall, this model had a relatively high score with no overfitting.

### For More Details:
[Github](https://github.com/dsi-group1/nyc-emergency-call-volume)

### Contributors:
[Chris Caress](https://www.linkedin.com/in/chris-caress-4245a51b5/) | [Christina Holland](https://www.linkedin.com/in/christina-holland-7400a1140/) | [Ashley Poon](https://www.linkedin.com/in/ashley-poon-y95/) | [David Romo](https://www.linkedin.com/in/daromo/)

''')

# sliders for each model param:
st.sidebar.write('## Use the sliders to predict the EMS Call Volume in NYC.')

year = 2016

month = st.sidebar.slider('Month',1,12)

day = st.sidebar.slider('Day',1,31)

hour = st.sidebar.slider('Hour',0,23)

PRCP = st.sidebar.slider('Precipitation',0,2)

if PRCP == 0:
    PRCP = 0
elif PRCP == 1:
    PRCP = 0.134018
else:
     PRCP = 5.810000

SNOW = 0.08702925584135096

SNWD = st.sidebar.slider('Snow Depth (inches)',0,24)

TAVG_CALC = st.sidebar.slider('Temp (F)',0,105)

Incidences = st.sidebar.slider('Traffic Incidents',0,53) #get actual range for this

params = [[year, month, day, hour, PRCP, SNOW, SNWD, TAVG_CALC, Incidences]]

# import  model
with open('app-model.pkl', mode='rb') as pickle_in:
    model = pickle.load(pickle_in)

# make prediction
prediction = model.predict(params)

st.sidebar.write(f'Predicting **{int(prediction)}** calls during the specified hour.')
