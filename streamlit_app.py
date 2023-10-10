import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Generate data and PCA
df = pd.read_csv("pca.csv")
zn = df[["z", "n"]].values

fig = go.Figure()


# colors = embs_pca[:, 2]
st.title("Interactive PCA Plot with Streamlit")

# Sliders for selecting PCs

x_pc = st.slider("Select PC for X-axis:", 1, 10, 1)
y_pc = st.slider("Select PC for Y-axis:", 1, 10, 2)
color = st.slider("Select PC for color:", 1, 10, 3)


fig = px.scatter(
        df,
        x=f"PC{x_pc}",
        y=f"PC{y_pc}",
        hover_data=["z", "n"],
        labels={"x": f"PC{x_pc}", "y": f"PC{y_pc}"},
        color=f"PC{color}",
        color_continuous_scale="rdbu"
    )

st.plotly_chart(fig)

