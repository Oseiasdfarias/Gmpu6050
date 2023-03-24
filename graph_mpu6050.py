import numpy as np
from matplotlib.animation import FuncAnimation
import time

# import tkinter as Tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Modulos criados
from gmpu6050 import ColetaDados
from gmpu6050 import Graphs

# Themes: blue (default), dark-blue, green
ctk.set_default_color_theme("green")

# Objeto para coletar dados do sensor
coleta_dados = ColetaDados()
time.sleep(1)

# Graficos
graphs = Graphs()
fig, ax, ln = graphs.get_fig_axes_ln()

fila = coleta_dados.get_dados()

# tx = []


def init():
    for i in range(6):
        """tx.append(ax[i].text(40, int(fila[i][-1])+2, f"{fila[i][-1]}",
                             color=[0.3, 0.3, 0.5],
                             fontsize=9,
                             fontweight="bold"))"""
        ax[i].set_xlim(0, 50)
        ax[i].set_ylim(-15, 15)
        if i > 2:
            ax[i].set_xlim(0, 50)
            ax[i].set_ylim(-10, 10)
        ax[i].axhline(0, color="dimgray", lw=1.2)
        ax[i].axvline(0.5, color="dimgray", lw=1.2)

    return ln


def update(frame):
    dados = coleta_dados.get_dados()
    t = np.arange(0, len(dados[0]))
    for i, ax in enumerate(ln):
        """tx[i].set_y(int(dados[i][-1]+2))
        if (i <= 2):
            tx[i].set_text(f"{dados[i][-1]:.2f}\nm/s^2")
        else:
            tx[i].set_text(f"{dados[i][-1]:.2f}\nrad/s")"""
        ax.set_xdata(t)
        ax.set_ydata(dados[i])
    return ln


# GUI
root = ctk.CTk()
root.title("Gráficos MPU6050")
# root.iconbitmap("mpu6050.ico")
root.geometry("1270x660+20+45")
label = ctk.CTkLabel(root,
                     text="Gráficos Sensor MPU6050",
                     font=ctk.CTkFont(size=20,
                                      weight="bold")).grid(column=1, row=0)

label_nemu = ctk.CTkLabel(master=root, text="Menu",
                          width=110,
                          # image="./test_images/CustomTkinter_logo_single.png",
                          font=ctk.CTkFont(size=15, weight="bold"))
label_nemu.grid(row=0, column=0, padx=20, pady=10)
# label_nemu.place(rely=0.1)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=1, row=1)


def quit():
    root.quit()
    root.destroy()


button = ctk.CTkButton(master=root, height=30,
                       font=ctk.CTkFont(size=15, weight="bold"),
                       text="Quit", command=quit)
button.grid(row=1, column=0, padx=40, pady=10, sticky="s")
button.place(rely=0.2)


def aparencia_event(new_appearance_mode):
    ctk.set_appearance_mode(new_appearance_mode)


aparencia_menu = ctk.CTkOptionMenu(master=root,
                                   font=ctk.CTkFont(size=15,
                                                    weight="bold"),
                                   values=["Light", "Dark"],
                                   command=aparencia_event)

aparencia_menu.grid(row=1, column=0, padx=20, pady=5, sticky="s")
aparencia_menu.place(rely=0.3)


ani = FuncAnimation(fig, update, init_func=init,
                    cache_frame_data=False, interval=20, blit=True)

root.mainloop()
