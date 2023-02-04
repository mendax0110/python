import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

Vz = 5 # Zener voltage
Iz = 20 # Zener current
Rl = 1000 # Load resistance

V = []
I = []
for v in range(0, 20):
    i = (v - Vz) / Rl
    if i <= Iz:
        V.append(v)
        I.append(i)

ax.plot(V, I)

ax.set_xlabel("Voltage (V)")
ax.set_ylabel("Current (A)")

# Add sliders for Vz, Iz, and Rl
ax_Vz = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_Iz = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_Rl = plt.axes([0.25, 0.05, 0.65, 0.03])

slider_Vz = Slider(ax_Vz, "Vz", 0, 10, valinit=Vz)
slider_Iz = Slider(ax_Iz, "Iz", 0, 50, valinit=Iz)
slider_Rl = Slider(ax_Rl, "Rl", 0, 5000, valinit=Rl)

def update(val):
    Vz = slider_Vz.val
    Iz = slider_Iz.val
    Rl = slider_Rl.val

    V = []
    I = []
    for v in range(0, 20):
        i = (v - Vz) / Rl
        if i <= Iz:
            V.append(v)
            I.append(i)

    ax.clear()
    ax.plot(V, I)
    ax.set_xlabel("Voltage (V)")
    ax.set_ylabel("Current (A)")
    fig.canvas.draw_idle()

slider_Vz.on_changed(update)
slider_Iz.on_changed(update)
slider_Rl.on_changed(update)

plt.show()
