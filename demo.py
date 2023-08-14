import math

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
# plt.rc("font", family='MicroSoft YaHei', weight="bold")

# 参数输入
st.title('制导Demo')
max_simulate_time = st.slider('仿真时长', min_value=5, max_value=200, value=100)
speed = st.slider('速度', min_value=50, max_value=500, value=200)
Ns = st.multiselect("N", [1, 2, 3, 4, 5], [3, 4, 5])
x0 = st.number_input("x0 (m)", -2000)
y0 = st.number_input("y0 (m)", 2000)
gamma0 = st.number_input("gamma0 (deg)", 45)

# 仿真
count = len(Ns)
t_all = []
x_all = []
y_all = []
command_all = []

for N in Ns:
    t = 0.0
    dt = 0.01
    x = x0
    y = y0
    gamma = gamma0 * math.pi / 180.0
    vx = speed * math.cos(gamma)
    vy = speed * math.sin(gamma)
    command = 0.0

    t_recorder = [t]
    x_recorder = [x]
    y_recorder = [y]
    command_recorder = [command]

    while t <= max_simulate_time:
        R = math.sqrt(x*x + y*y)
        speed = math.sqrt(vx*vx + vy*vy)
        if R < 10:
            break
        theta = math.atan2(-y, -x)
        gamma = math.atan2(vy, vx)
        sigma = gamma - theta
        if sigma < -math.pi:
            sigma = sigma + 2*math.pi
        if sigma > math.pi:
            sigma = sigma - 2*math.pi
        command = -N*speed*speed*math.sin(sigma)/R
        ax = command*math.cos(gamma+math.pi/2)
        ay = command*math.sin(gamma+math.pi/2)

        vx = vx + ax*dt
        vy = vy + ay*dt
        x = x + vx*dt
        y = y + vy*dt

        t = t + dt
        t_recorder.append(t)
        x_recorder.append(x)
        y_recorder.append(y)
        command_recorder.append(command)
    t_all.append(t_recorder)
    x_all.append(x_recorder)
    y_all.append(y_recorder)
    command_all.append(command_recorder)


fig, axs = plt.subplots(2, 1)  # 创建画布与子图

ax = axs[0]
ax.set_title('Trajectory')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.axis('equal')
for i in range(count):
    x_data = x_all[i]
    y_data = y_all[i]
    ax.plot(x_data, y_data)
ax.legend(Ns)

ax = axs[1]
ax.set_title('Acceleration')
ax.set_xlabel('time (s)')
ax.set_ylabel('command (m/s^2)')
for i in range(count):
    x_data = t_all[i]
    y_data = command_all[i]
    ax.plot(x_data[1:], y_data[1:])

fig.subplots_adjust(left=None, bottom=None, right=None, top=None, hspace=0.5, wspace=None)
st.pyplot(fig)
