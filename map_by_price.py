import random
import pandas as pd
import plotly
from plotly.graph_objs import *
import math

mapbox_access_token = 'pk.eyJ1IjoiZmZ6cyIsImEiOiJjamJlZ3JhdTEwdjVpMnlxd2xpdnY5Y2NjIn0.tm2mSVe0SU6G5NvXxkBbPQ'

df = pd.read_csv('zufang3.csv')
df = df.sort_values("location")
df['text'] = df['name'] + '<br> ' + (df['number']).astype(str)+' 套房出租' + '<br> ' +'每平每月房租'+ (df['mean_prc']).astype(int).astype(str)
limits = [(0,50),(51,70),(71,90),(91,120),(121,200),(200,3000)]
colors = ["rgb(255,65,54)","rgb(0,116,217)","rgb(133,20,75)","rgb(255,133,27)","rgb(138 ,43, 226)","rgb(47 ,79 ,79)"]  #"red",,"green"
cities = []
scale = 5

for i in range(0,len(limits)):
    # name = name_list[i]
    lim = limits[i]
    df_sub1 = df[df.mean_prc>lim[0]]
    df_sub=df_sub1[df_sub1.mean_prc<=lim[1]]
    city = Data([Scattermapbox(
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        mode='markers',
        marker = Marker(
            size = df_sub["number"].apply(lambda x:math.sqrt(x))*scale,
            color =colors[i],
            # line = dict(width=0.5, color='rgb(40,40,40)'),
            sizemode = 'area'
        ),
        text=df_sub['text'],
        name = '{0} - {1}'.format(lim[0],lim[1])
         )])
    cities.extend(city)

layout = Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=39.925557,
            lon=116.410285
        ),
        pitch=0,
        zoom=5,
        style='mapbox://styles/mapbox/streets-v10'
    ),
)


fig = dict( data=cities, layout=layout )
plotly.offline.plot(fig,filename="map_by_price.html")