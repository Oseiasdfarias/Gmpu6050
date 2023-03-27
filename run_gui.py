from gmpu6050 import GraphMpu6959


def rungmpu():
    graph = GraphMpu6959()
    graph.start_gui()


if __name__ == "__main__":
    rungmpu()
