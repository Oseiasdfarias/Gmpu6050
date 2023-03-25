import serial
from time import sleep
import numpy as np
from threading import Thread


class ColetaDados:
    """Coleta os dados do sensor mpu6050 e salva em um buffer

    param: porta='/dev/ttyUSB0'
    param: baud_rate=115200

    """
    def __init__(self, porta="/dev/ttyUSB0", baud_rate=115200):
        self.porta = porta
        self.baud_rate = baud_rate
        self.fila = np.array([[], [], [], [], [], []]).astype(object)
        self.__init_thread()

    def get_dados(self):
        return self.fila

    def __init_thread(self):
        self.new_thread = Thread(target=self.__coleta_dados)
        self.new_thread.daemon = True
        self.new_thread.start()

    def __coleta_dados(self):
        self.disp = serial.Serial(self.porta, self.baud_rate)
        self.disp.reset_input_buffer()
        while self.disp.is_open:
            try:
                dado = self.disp.readline()
                dados1 = str(dado.decode('utf8')).rstrip("\n")
                dados1 = dados1.split(",")
                try:
                    dados_float = np.array([dados1], dtype="float64").T
                    if len(self.fila[0]) <= 50:
                        self.fila = np.append(self.fila, dados_float, axis=1)
                    else:
                        self.fila = np.delete(self.fila, np.s_[:1], 1)
                except Exception as erro:
                    print(f"Erro: {erro}")
                    sleep(0.03)
            except serial.SerialException:
                print("Erro de leitura ...")
                self.disp.reset_input_buffer()
                break


if __name__ == "__main__":
    coleta_dados = ColetaDados()
    while True:
        dados = coleta_dados.get_dados()
        print(dados)
