import pandas as pd
import plotly.express as px

df = pd.read_csv("studentattempt.csv")
r = df.groupby(['student_id','level'],as_index=False)['attempt'].mean()
print(r)

fig = px.scatter(r,x="student_id",y="level",size = 'attempt',color = 'attempt')
fig.show()