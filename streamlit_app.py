import streamlit as st
import pandas as pd

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

df=pd.DataFrame(data)

st.subheader("Dataframe")
st.dataframe(df)  #display dataframe

st.subheader("Static Table")
st.table(df) 