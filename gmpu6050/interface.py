import numpy as np
from matplotlib.animation import FuncAnimation

# import tkinter as Tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Modulos criados
from gmpu6050 import ColetaDados
from gmpu6050 import Graphs


class GraphMpu6959:
    def __init__(self):
        # Themes: blue (default), dark-blue, green
        ctk.set_default_color_theme("green")

        # Objeto para coletar dados do sensor
        self.usb_port = "/dev/ttyUSB0"
        self.baud_rate = 115200
        self.coleta_dados = ColetaDados(porta=self.usb_port,
                                        baud_rate=self.baud_rate)

        # Graficos
        self.executar = True
        graphs = Graphs()
        self.fig, self.ax, self.ln = graphs.get_fig_axes_ln()
        self.fila = self.coleta_dados.get_dados()

        # tx = []

    def init(self):
        for i in range(6):
            """tx.append(ax[i].text(40, int(fila[i][-1])+2, f"{fila[i][-1]}",
                                color=[0.3, 0.3, 0.5],
                                fontsize=9,
                                fontweight="bold"))"""
            self.ax[i].set_xlim(0, 50)
            self.ax[i].set_ylim(-15, 15)
            if i > 2:
                self.ax[i].set_xlim(0, 50)
                self.ax[i].set_ylim(-10, 10)
            self.ax[i].axhline(0, color="dimgray", lw=1.2)
            self.ax[i].axvline(0.5, color="dimgray", lw=1.2)
        return self.ln

    def update(self, frame):
        dados = self.coleta_dados.get_dados()
        t = np.arange(0, len(dados[0]))
        for i, ax in enumerate(self.ln):
            """tx[i].set_y(int(dados[i][-1]+2))
            if (i <= 2):
                tx[i].set_text(f"{dados[i][-1]:.2f}\nm/s^2")
            else:
                tx[i].set_text(f"{dados[i][-1]:.2f}\nrad/s")"""
            ax.set_xdata(t)
            ax.set_ydata(dados[i])
        return self.ln

    def quit(self):
        self.root.quit()
        self.root.destroy()
    
    def get_usb_port(self):
        port = self.textbox.get("0.0", "end")
        self.usb_port = port.strip(" ").replace("\n", "")
        # self.textbox.delete("0.0", "end")
        print(self.usb_port)

    @staticmethod
    def aparencia_event(new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def run_graph(self):
        if self.executar:
            self.ani = FuncAnimation(self.fig, self.update,
                                     init_func=self.init,
                                     cache_frame_data=False,
                                     interval=20, blit=True)
        self.executar = False

    def start_gui(self):
        # GUI
        self.root = ctk.CTk()
        self.root.title("Gráficos MPU6050")
        # root.iconbitmap("mpu6050.ico")
        self.root.geometry("1270x660+20+45")
        self.label = ctk.CTkLabel(
            self.root, text="Gráficos Sensor MPU6050",
            font=ctk.CTkFont(size=20,
                             weight="bold")).grid(column=1, row=0)

        self.label_nemu = ctk.CTkLabel(master=self.root, text="Menu",
                                       width=110,
                                       # image="./test_images/CustomTkinter_logo_single.png",
                                       font=ctk.CTkFont(size=15,
                                                        weight="bold"))
        self.label_nemu.grid(row=0, column=0, padx=20, pady=10)
        # label_nemu.place(rely=0.1)

        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.get_tk_widget().grid(column=1, row=1)

        button_run = ctk.CTkButton(master=self.root, height=30,
                                   font=ctk.CTkFont(size=15, weight="bold"),
                                   text="Executar", border_width=1,
                                   command=self.run_graph)
        button_run.grid(row=2, column=0,
                        padx=40, pady=10,
                        sticky="s")
        button_run.place(rely=0.2)

        button = ctk.CTkButton(master=self.root, height=30,
                               font=ctk.CTkFont(size=15, weight="bold"),
                               text="Quit", border_width=1,
                               command=self.quit)
        button.grid(row=3, column=0,
                    padx=40, pady=10,
                    sticky="s")
        button.place(rely=0.3)

        button_usb = ctk.CTkButton(master=self.root, height=30,
                                   font=ctk.CTkFont(size=15, weight="bold"),
                                   text="Get USB", border_width=1,
                                   command=self.get_usb_port)
        button_usb.grid(row=4, column=0,
                        padx=40, pady=10,
                        sticky="s")
        button_usb.place(rely=0.4)

        self.textbox = ctk.CTkTextbox(master=self.root, height=27, width=140,
                                      font=ctk.CTkFont(size=15,
                                                       weight="bold"),
                                      corner_radius=10,
                                      border_width=1)
        self.textbox.grid(row=5, padx=40, pady=10, column=0, sticky="s")
        self.textbox.insert("0.0", "ttyUSB0")
        self.textbox.place(rely=0.46)
        self.textbox.focus_set()

        self.aparencia_menu = ctk.CTkOptionMenu(master=self.root,
                                                font=ctk.CTkFont(
                                                     size=15,
                                                     weight="bold"),
                                                values=["Light", "Dark"],
                                                command=self.aparencia_event)

        self.aparencia_menu.grid(row=6, column=0, padx=20, pady=5, sticky="s")
        self.aparencia_menu.place(rely=0.55)

        self.root.mainloop()


if __name__ == "__main__":
    graph = GraphMpu6959()
    graph.start_gui()
