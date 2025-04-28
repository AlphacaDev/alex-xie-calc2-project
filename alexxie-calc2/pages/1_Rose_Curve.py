import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Rose Curve")

st.write("A rose curve is a set of point in polar coordinates specified by" \
"the polar equation:")

st.latex(r"r = a \cdot \sin(k \cdot \theta)")
st.latex(r"r = a \cdot \cos(k \cdot \theta)")

st.write("In this equation, `a` is the scale factor and `k` is the number of petals." \
" The functions `sin` and `cos` determine the orientation of the petals.")

st.write("This program uses these parametric equations to calculate the graphs:")

st.latex(r"x = r \cdot \cos(\theta)")
st.latex(r"y = r \cdot \sin(\theta)")

def generate_rose_curve(a=1, k=5, function='cos', num_points=1000):
    theta = np.linspace(0, 2 * np.pi, num_points)

    if function == 'cos':
        r = a * np.cos(k * theta)
    else:
        r = a * np.sin(k * theta)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    df = pd.DataFrame({'x': x, 'y': y, 'order': np.arange(num_points)})
    return df

def plot_rose_curve(df, col):
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
        width = 500,
        height = 700
    )
    return chart

st.checkbox("Add a second rose curve", value=False, key="rose_curve_checkbox")
if st.session_state.rose_curve_checkbox:
    st.write("Here is a graph with two rose curves:")
    slider1 = st.slider("a", 1, 10, 1, 1)
    slider2 = st.slider("k", 1, 10, 3, 1)
    choice1 = st.radio("Function", ["cos", "sin"], index=1)

    a,k,function = slider1, slider2, choice1
    df = generate_rose_curve(a, k, function)
    chart1 = plot_rose_curve(df, 'blue')

    slider3 = st.slider("a2", 1, 10, 1, 1)
    slider4 = st.slider("k2", 1, 10, 3, 1)
    choice2 = st.radio("Function2", ["cos", "sin"], index=0)

    a2,k2,function2 = slider3, slider4, choice2
    df2 = generate_rose_curve(a2, k2, function2)
    chart2 = plot_rose_curve(df2, 'red')
    finchart = alt.layer(chart1, chart2)
    finchart
else:
    st.write("Here is a graph with a singular rose curve:")
    slider1 = st.slider("a", 1, 10, 1, 1)
    slider2 = st.slider("k", 1, 10, 4, 1)
    choice1 = st.radio("Function", ["cos", "sin"], index=1)

    a,k,function = slider1, slider2, choice1
    df = generate_rose_curve(a, k, function)
    chart1 = plot_rose_curve(df, 'blue')
    chart1

