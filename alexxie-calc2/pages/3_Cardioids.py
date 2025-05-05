import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

st.title("Cardioid Curve")

st.write("A cardioid is a set of point in polar coordinates specified by" \
"the polar equation:")

st.latex(r"r = a \cdot (1 \pm \cos(\theta))")
st.latex(r"r = a \cdot (1 \pm \sin(\theta))")

st.write("In this equation, `a` is the scale factor." \
" The functions `sin` and `cos` determine whether the cardioid is horizontal or vertical.")

st.write("This program uses these parametric equations to calculate the graphs:")

st.latex(r"x = r \cdot \cos(\theta)")
st.latex(r"y = r \cdot \sin(\theta)")

def generate_cardioid(a=1, func = 'cos', num_points=1000):
    theta = np.linspace(0, 2 * np.pi, num_points)
    
    if func == 'cos':
        x = a * (2 * np.cos(theta) - np.cos(2 * theta))# * scale_x + offset_x
        y = a * (2 * np.sin(theta) - np.sin(2 * theta))# * scale_y + offset_y
    else:
        x = a * (2 * np.sin(theta) - np.sin(2 * theta))
        y = a * (2 * np.cos(theta) - np.cos(2 * theta))
    
    df = pd.DataFrame({
        'x': x,
        'y': y,
        'order': np.arange(num_points)
    })
    
    return df

def plot_cardioid(df, col):
    chart = alt.Chart(df).mark_line(color=col).encode(
        x=alt.X(
            'x',
            axis=alt.Axis(title='X'),
            scale=alt.Scale(zero=False),
        ),
        y=alt.Y(
            "y",
            axis=alt.Axis(title='Y'),
            scale=alt.Scale(zero=False),
        ),
        order='order:O'
    ).properties(
        width=500,
        height=700
    )
    
    return chart

st.checkbox("Add a second cardioid", value=False, key="cardioid_checkbox")
if st.session_state.cardioid_checkbox:
    st.write("Here is a graph with two cardioids:")
    slider1 = st.slider("a", 1, 10, 1, 1)

    a = slider1
    func = st.radio("Function", ["cos", "sin"], index=0)
    df = generate_cardioid(a, func)
    chart1 = plot_cardioid(df, 'blue')

    slider3 = st.slider("a2", 1, 10, 1, 1)

    a2 = slider3
    func2 = st.radio("Function2", ["cos", "sin"], index=1)
    df2 = generate_cardioid(a2, func2)
    chart2 = plot_cardioid(df2, 'red')
    finchart = alt.layer(chart1, chart2)
    finchart
else:
    st.write("Here is a graph with a singular cardioid:")
    slider1 = st.slider("a", 1, 10, 1, 1)

    a = slider1
    func = st.radio("Function", ["cos", "sin"], index=0)
    df = generate_cardioid(a, func)
    chart1 = plot_cardioid(df, 'blue')
    chart1