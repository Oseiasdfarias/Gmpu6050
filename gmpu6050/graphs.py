import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use("ggplot")
matplotlib.use('TkAgg')


class Graphs(object):

    def __init__(self):

        self.fig, ((self.ax1, self.ax2, self.ax3),
                   (self.ax4, self.ax5, self.ax6)) =\
                    plt.subplots(2, 3, figsize=(11, 6))

        # fig.suptitle('Gráficos Sensor MPU6050', fontsize=19)
        self.fig.subplots_adjust(wspace=0.32, hspace=0.44, left=0.076,
                                 top=0.894, right=0.971, bottom=0.098)
        self.config_axes()

    def get_fig_axes_ln(self):
        return self.fig, self.ax, self.ln

    def config_axes(self):
        self.ax1 = self.fig.add_subplot(231)
        self.ax1.set_title("Aceleração eixo X($m/s^2$)", fontsize=11)
        self.ax1.set_xlabel("Tempo")
        self.ax1.set_ylabel("Amplitude")
        self.ln1, = self.ax1.plot([], [], lw=1.5, color="sienna")

        self.ax2 = self.fig.add_subplot(232)
        self.ax2.set_title("Aceleração eixo Y($m/s^2$)", fontsize=11)
        self.ax2.set_xlabel("Tempo")
        self.ax2.set_ylabel("Amplitude")
        self.ln2, = self.ax2.plot([], [], lw=1.5, color="green")

        self.ax3 = self.fig.add_subplot(233)
        self.ax3.set_title("Aceleração eixo Z($m/s^2$)", fontsize=11)
        self.ax3.set_xlabel("Tempo")
        self.ax3.set_ylabel("Amplitude")
        self.ln3, = self.ax3.plot([], [], lw=1.5, color="red")

        self.ax4 = self.fig.add_subplot(234)
        self.ax4.set_title("Rotação em X [Roll] ($rad/s$)", fontsize=11)
        self.ax4.set_xlabel("Tempo")
        self.ax4.set_ylabel("Amplitude")
        self.ln4, = self.ax4.plot([], [], lw=1.5, color="blue")

        self.ax5 = self.fig.add_subplot(235)
        self.ax5.set_title("Rotação em Y [Pitch] ($rad/s$)", fontsize=11)
        self.ax5.set_xlabel("Tempo")
        self.ax5.set_ylabel("Amplitude")
        self.ln5, = self.ax5.plot([], [], lw=1.5, color="purple")

        self.ax6 = self.fig.add_subplot(236)
        self.ax6.set_title("Rotação em Z [Yaw] ($rad/s$)", fontsize=11)
        self.ax6.set_xlabel("Tempo")
        self.ax6.set_ylabel("Amplitude")
        self.ln6, = self.ax6.plot([], [], lw=1.5, color="black")

        # Axis que para plotar os gráficos
        self.ln = [self.ln1, self.ln2, self.ln3, self.ln4, self.ln5, self.ln6]
        self.ax = [self.ax1, self.ax2, self.ax3, self.ax4, self.ax5, self.ax6]
