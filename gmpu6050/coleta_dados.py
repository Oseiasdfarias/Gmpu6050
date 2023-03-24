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
        self.init_thread()

    def get_dados(self):
        return self.fila

    def init_thread(self):
        new_thread = Thread(target=self.coleta_dados)
        new_thread.daemon = True
        new_thread.start()

    def coleta_dados(self):
        disp = serial.Serial(self.porta, self.baud_rate)
        disp.reset_input_buffer()
        while disp.is_open:
            try:
                dado = disp.readline()
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
                break


if __name__ == "__main__":
    coleta_dados = ColetaDados()
    while True:
        dados = coleta_dados.get_dados()
        print(dados)
