import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Devil's Curve")

st.write("A devil's curve is a set of point in polar coordinates specified by" \
         "the polar equation:")

st.latex(r"r = \sqrt{\frac{b^2\sin^2(\theta) - a^2\cos^2(\theta)}{\sin^2(\theta)-\cos^2(\theta)}}")

st.write("This program uses this equation to calculate the graph:")

st.latex(r"y^2(y^2 - b^2) = x^2(x^2 - a^2)")

st.write("In this equation, when `a` is less than `b`, the graph is shown as horizontal. " \
"However, when `a` is greater than `b`, the graph is shown as vertical.")

st.write("Here is a graph of the devil's curve:")

def top_chart(a,b,num_steps,xmin,xmax,ymin,ymax,col):
  df = pd.DataFrame()
  if a < b:
    x = np.linspace(x_min, x_max, num_steps)
    xx = np.power(x, 2)
    d = np.power(b, 4) + (4 * xx * (xx - np.power(a, 2)))
    y1 = np.sqrt( (np.power(b, 2) + np.sqrt(d)) / 2 )
    df['x'] = pd.Series(x)
    df['y'] = pd.Series(y1)
    ord = 'x'
  else:
    y = np.linspace(y_min, y_max, num_steps)
    yy = np.power(y, 2)
    d = np.power(a, 4) + (4 * yy * (yy - np.power(b, 2)))
    x1 = np.sqrt( (np.power(a, 2) + np.sqrt(d)) / 2 )
    df['x'] = pd.Series(x1)
    df['y'] = pd.Series(y)
    ord = 'y'

  chart1 = alt.Chart(df).mark_line(clip=True, color=col).encode(
      x=alt.X(
          'x',
          axis=alt.Axis(title='X'),
          scale=alt.Scale(zero=False, domain=(x_min, x_max)),
      ),
      y=alt.Y(
          "y",
          axis=alt.Axis(title='Y'),
          scale=alt.Scale(zero=False, domain=(y_min, y_max)),
      ),
      order = ord
  )
  return chart1

def bottom_chart(a,b,num_steps,xmin,xmax,ymin,ymax,col):
  df = pd.DataFrame()

  if a < b:
    x = np.linspace(x_min, x_max, num_steps)
    xx = np.power(x, 2)
    d = np.power(b, 4) + (4 * xx * (xx - np.power(a, 2)))
    y3 = -1*np.sqrt( (np.power(b, 2) + np.sqrt(d)) / 2 )
    df['x'] = pd.Series(x)
    df['y'] = pd.Series(y3)
    ord = 'x'
  else:
    y = np.linspace(y_min, y_max, num_steps)
    yy = np.power(y, 2)
    d = np.power(a, 4) + (4 * yy * (yy - np.power(b, 2)))
    x3 = -np.sqrt( (np.power(a, 2) + np.sqrt(d)) / 2 )
    df['x'] = pd.Series(x3)
    df['y'] = pd.Series(y)
    ord = 'y'

  chart3 = alt.Chart(df).mark_line(clip=True, color=col).encode(
      x=alt.X(
          'x',
          axis=alt.Axis(title='X'),
          scale=alt.Scale(zero=False, domain=(x_min, x_max)),
      ),
      y=alt.Y(
          "y",
          axis=alt.Axis(title='Y'),
          scale=alt.Scale(zero=False, domain=(y_min, y_max)),
      ),
      order = ord
  )

  return chart3

def top_mid(a,b,num_steps,xmin,xmax,ymin,ymax,col):
  df = pd.DataFrame()

  if a < b:
    x = np.linspace(-a, a, num_steps)
    xx = np.power(x, 2)
    d = np.power(b, 4) + (4 * xx * (xx - np.power(a, 2)))
    y2 = np.sqrt( (np.power(b, 2) - np.sqrt(d)) / 2 )
    df['x'] = pd.Series(x)
    df['y'] = pd.Series(y2)
    ord = 'x'
  else:
    y = np.linspace(-b, b, num_steps)
    yy = np.power(y, 2)
    d = np.power(a, 4) + (4 * yy * (yy - np.power(b, 2)))
    x2 = np.sqrt( (np.power(a, 2) - np.sqrt(d)) / 2 )
    df['x'] = pd.Series(x2)
    df['y'] = pd.Series(y)
    ord = 'y'

  chart2 = alt.Chart(df).mark_line(clip=True, color=col).encode(
      x=alt.X(
          'x',
          axis=alt.Axis(title='X'),
          scale=alt.Scale(zero=False, domain=(x_min, x_max)),
      ),
      y=alt.Y(
          "y",
          axis=alt.Axis(title='Y'),
          scale=alt.Scale(zero=False, domain=(y_min, y_max)),
      ),
      order = ord
  )

  return chart2

def bottom_mid(a,b,num_steps,xmin,xmax,ymin,ymax,col):
  df = pd.DataFrame()

  if a < b:
    x = np.linspace(-a, a, num_steps)
    xx = np.power(x, 2)
    d = np.power(b, 4) + (4 * xx * (xx - np.power(a, 2)))
    y4 = -1*np.sqrt( (np.power(b, 2) - np.sqrt(d)) / 2 )
    df['x'] = pd.Series(x)
    df['y'] = pd.Series(y4)
    ord = 'x'
  else:
    y = np.linspace(-b, b, num_steps)
    yy = np.power(y, 2)
    d = np.power(a, 4) + (4 * yy * (yy - np.power(b, 2)))
    x4 = -np.sqrt( (np.power(a, 2) - np.sqrt(d)) / 2 )
    df['x'] = pd.Series(x4)
    df['y'] = pd.Series(y)
    ord = 'y'

  chart4 = alt.Chart(df).mark_line(clip=True, color=col).encode(
      x=alt.X(
          'x',
          axis=alt.Axis(title='X'),
          scale=alt.Scale(zero=False, domain=(x_min, x_max)),
      ),
      y=alt.Y(
          "y",
          axis=alt.Axis(title='Y'),
          scale=alt.Scale(zero=False, domain=(y_min, y_max)),
      ),
      order = ord
  )

  return chart4

def generate_devils_curve(a,b,num_steps,xmin,xmax,ymin,ymax,color):
  chart1 = top_chart(a,b,num_steps,xmin,xmax,ymin,ymax,color)
  chart2 = bottom_chart(a,b,num_steps,xmin,xmax,ymin,ymax,color)
  chart3 = top_mid(a,b,num_steps,xmin,xmax,ymin,ymax,color)
  chart4 = bottom_mid(a,b,num_steps,xmin,xmax,ymin,ymax,color)

  finchart = alt.layer(chart1,chart2,chart3,chart4
    ).configure_view(
        strokeWidth=0
    ).properties(
        height = 700,
        width = 500
    )
  return finchart

a = st.slider("a", 0.1, 2.0, 0.8, 0.1)
b = st.slider("b", 0.1, 2.0, 1.0, 0.1)
num_steps = 1001
x_min = -2
x_max = 2
y_min = -2
y_max = 2

curve = generate_devils_curve(a,b,num_steps,x_min,x_max,y_min,y_max,'red')
curve