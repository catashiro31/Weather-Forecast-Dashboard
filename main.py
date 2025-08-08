import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input(label='Place:', placeholder='Enter a place.')
day = st.slider(label='Forecast Days', min_value=1, max_value=5,
                help='Select the number of forecasted days')
kind = st.selectbox(label='Select data to view', options=['Temperature', 'Sky'])
st.subheader(f'{kind} for the next {day} days in {place}')

d, ot = get_data(place, day, kind)
if (d,ot) == (None, None):
    st.write('City not found')
elif kind == 'Temperature':
    figure = px.line(x=d, y=ot, labels={'x':'Date Time','y':'Temperature (C)'})
    st.plotly_chart(figure)
else:
    figure, ax = plt.subplots(nrows=day*2,ncols=4, figsize=(12,6*day))
    ax = ax.flatten()
    for idx in range(day*8):
        img = plt.imread('images/' + ot[idx] + '.png')
        ax[idx].imshow(img)
        ax[idx].set_title(d[idx].strftime('%A, %d %B %Y\n%H:%M'))
        ax[idx].axis(False)
    st.pyplot(fig=figure)