import plotly.graph_objects as go
import pandas as pd
import os

d = {'y-axis': ['TEIs and RCs S3', 'TEIs and RCs S2', 'TEIs and RCs S1', 'Socioeconomic Factors S2', 'Socioeconomic Factors S1', 'Learning Modality S2', 'Learning Modality S1'],
     'Neutral': [2, 1, 1, 4, 5, 2, 0],
     'Disagree': [0, 0, 1, 1, 1, 1, 0],
     'Strongly Disagree': [1, 3, 2, 4, 4, 1, 0],
     'Agree': [3, 3, 5, 5, 4, 5, 9],
    'Strongly Agree': [7, 10, 8, 3, 3, 8, 8]}
df = pd.DataFrame(d)

fig = go.Figure()
fig.add_trace(go.Bar(x=-df["Neutral"].values/2,
                     y=df['y-axis'],
                     orientation='h',
                     name="Neutral",
                     customdata=df["Neutral"],
                     xperiodalignment="middle",
                     hovertemplate = "%{y}: %{customdata}",
                     showlegend=False,
                     marker_color='purple'))

fig.add_trace(go.Bar(x=+df["Neutral"].values/2,
                     y=df['y-axis'],
                     orientation='h',
                     name="Neutral",
                     customdata=df["Neutral"],
                     xperiodalignment="middle",
                     hovertemplate = "%{y}: %{customdata}",
                     marker_color='purple'))

for col in df.columns[2:4]:
    fig.add_trace(go.Bar(x=-df[col].values,
                         y=df['y-axis'],
                         orientation='h',
                         name=col,
                         customdata=df[col],
                         hovertemplate = "%{y}: %{customdata}"))
for col in df.columns[4:]:
    fig.add_trace(go.Bar(x=df[col],
                         y=df['y-axis'],
                         orientation='h',
                         name=col,
                         customdata=df[col], 
                         hovertemplate="%{y}: %{x}"))    

    fig.update_layout(barmode='relative', 
                  height=400, 
                  width=700, 
                  yaxis_autorange='reversed',
                  bargap=0.01,
                  legend_orientation ='h',
                  legend_x=-0.05, legend_y=1.3
                 )
fig.show()
fig.write_html(os.getcwd()+"\\dda.html")
