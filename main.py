import time
from generate_data import DriftingDataset
from drift_detection import DriftDetector

drift_detector = DriftDetector()
dataset = DriftingDataset()

for example in dataset:
    print(example)
    time.sleep(.1)
    drift_detector.monitor(example)
