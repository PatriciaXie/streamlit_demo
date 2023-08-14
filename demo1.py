import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Sine Wave Plotter')

# Get user input for frequency and amplitude
freq = st.slider('Frequency', min_value=1, max_value=10, value=1)
amp = st.slider('Amplitude', min_value=1, max_value=5, value=1)

# Create x values
x = np.linspace(0, 2*np.pi, 1000)

# Create y values
y = amp * np.sin(freq * x)

# Plot the graph
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Sine Wave')
ax.set_xlabel('X')
ax.set_ylabel('Y')
st.pyplot(fig)