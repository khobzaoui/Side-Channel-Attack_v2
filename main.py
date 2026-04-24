from data_generator import DataGenerator
from cpa_analysis import CPAAnalyzer
from cnn_model import CNNModel
from database import Database
from visualization import Visualizer
from sklearn.model_selection import train_test_split

# Generate data
traces, labels = DataGenerator().generate()

# CPA
cpa_acc = CPAAnalyzer().compute(traces, labels)
print("CPA Accuracy:", cpa_acc)

# CNN
X = traces.reshape(traces.shape[0], traces.shape[1], 1)
Xtr, Xte, ytr, yte = train_test_split(X, labels, test_size=0.2)

cnn = CNNModel((traces.shape[1], 1))
hist = cnn.train(Xtr, ytr, Xte, yte)
cnn_acc = hist.history['val_accuracy'][-1]
print("CNN Accuracy:", cnn_acc)

# Database
db = Database()
db.insert("CPA", cpa_acc)
db.insert("CNN", cnn_acc)

print("DB:", db.fetch())

# Visualization
viz = Visualizer()
viz.plot()
