import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Generate data and PCA
df = pd.read_csv("pca.csv")

st.title("Select PCA components to plot")
# Sliders for selecting PCs
st.write("## 2D PCA Plot")

# empty_line = st.empty() # this is where the plot will be rendered
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
    color_continuous_scale="rdbu",
)

st.plotly_chart(fig)

# add another plot but in 3D, with the same sliders
st.write("## 3D PCA Plot")
z_pc = st.slider("Select PC for Z-axis:", 1, 10, 3)

fig = px.scatter_3d(
    df,
    x=f"PC{x_pc}",
    y=f"PC{y_pc}",
    z=f"PC{z_pc}",
    hover_data=["z", "n"],
    color=f"PC{color}",
    color_continuous_scale="rdbu",
    # size=[2] * len(df),
)

st.plotly_chart(fig)
