import sqlite3
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, db_path="db/results.db"):
        self.conn = sqlite3.connect(db_path)

    def plot(self):
        data = self.conn.execute("SELECT model, acc FROM results").fetchall()
        models = [d[0] for d in data]
        acc = [d[1] for d in data]

        plt.figure()
        plt.bar(models, acc)
        plt.xlabel("Models")
        plt.ylabel("Accuracy")
        plt.title("Model Performance")
        plt.savefig("results.png")
        plt.show()
