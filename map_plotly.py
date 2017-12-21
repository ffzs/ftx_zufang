import random
import pandas as pd
import plotly
from plotly.graph_objs import *
import math

mapbox_access_token = 'pk.eyJ1IjoiZmZ6cyIsImEiOiJjamJlZ3JhdTEwdjVpMnlxd2xpdnY5Y2NjIn0.tm2mSVe0SU6G5NvXxkBbPQ'

df = pd.read_csv('zufang2.csv')
df = df.sort_values("location")
df['text'] = df['name'] + '<br> ' + (df['number']).astype(str)+' 套房出租'
name_list =['东城', '丰台', '北京周边', '大兴', '密云', '崇文', '延庆', '怀柔', '房山', '昌平', '朝阳', '海淀', '燕郊', '石景山', '西城', '通州', '门头沟', '顺义']
colors = ["red","rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","green","rgb(138 ,43, 226)","rgb(47 ,79 ,79)"]
cities = []
scale = 5

for i in range(0,len(name_list)):
    name = name_list[i]
    df_sub = df[df['location'].isin([name])]
    city = Data([Scattermapbox(
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        mode='markers',
        marker = Marker(
            size = df_sub["number"],
            color = random.choice(colors),
            # line = dict(width=0.5, color='rgb(40,40,40)'),
            sizemode = 'area'
        ),
        text=df_sub['text'],
        name = name
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
plotly.offline.plot(fig)