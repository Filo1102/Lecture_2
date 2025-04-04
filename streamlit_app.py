import streamlit as st
import pandas as pd
import numpy as np

st.title("Metric")

st.metric(label="Number of Assists", value="25", delta="+6")

st.metric(label="Goals", value="13", delta="-5")

#dataframe
st.title(":blue[dataframe]")

data={
    "Player's Name": ["Pelè", "Maradona", "Baggio"],
    "Goals": [13, 25, 24],
    "Team" :["Juventus", "Napoli", "Inter"]
}

df1=pd.DataFrame(data)

st.subheader("Dataframe")
st.dataframe(df1)  #display dataframe

st.subheader("Static Table")
st.table(df1) 

#Data creaation
n_goals = np.random.randint(4, 21, size=(38, 3))
player_names = ["Fonseca", "Maradona", "Baggio"]

df2=pd.DataFrame(n_goals, columns=player_names)
st.dataframe(df2)


#line chart
st.title("Line chart")

#st.line_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, width=None, height=None, use_container_width=True)
st.line_chart(df2)

#Area chart
st.title('Area chart')
st.area_chart(df2)

#bar chart
st.title('**Bar** chart')
st.bar_chart(df2)

#Scatter chart
n_matches=38
x_coord=np.random.rand(n_matches)*100
y_coord=np.random.rand(n_matches)*100
goal_values = np.random.randint(0, 15, size=(n_matches))

goal_colors = np.random.rand(n_matches, 3) #RGB colors
goal_colors_lot = [tuple(c) for c in goal_colors]

goal_data={"X": x_coord,
           "Y":y_coord,
           "Goals": goal_values,
           "Colors": goal_colors_lot
}

df3=pd.DataFrame(goal_data)
st.dataframe(df3)

st.scatter_chart(goal_data, x="X", y="Y", size="Goals", color="Colors")
