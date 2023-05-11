# %%

class DriftDetector:
    """A class used to monitor a single value of a datapoint for drift"""

    def __init__(self, detector_name):
        self.name = detector_name
        self.mean = None
        self.examples_seen = 0
        self.alpha = 0.9
        self.threshold = 1

    def compute_running_mean(self, data):
        """Computes the running mean of the input data for each element provided in the array"""
        if self.examples_seen == 0:
            self.mean = data
        else:
            self.mean = (self.mean * self.examples_seen +
                         data) / (self.examples_seen + 1)
            self.exponential_rolling_mean = self.mean * \
                self.alpha + data * (1 - self.alpha)
        self.examples_seen += 1

    def monitor(self, data):
        """Monitors the input data for drift"""

        # print("Monitoring data")
        # print(self.mean)
        self.compute_running_mean(data)
        # print("New mean", self.mean)

        if self.examples_seen == 1:  # if the first example is seen
            self.mean_upper_threshold = self.mean + self.threshold
            self.mean_lower_threshold = self.mean - self.threshold

        if self.drift_detected():
            pass
            # print("Retraining model")

    def drift_detected(self):
        """Detects drift in the monitored data"""
        drift_detected = False
        if self.mean > self.mean_upper_threshold or self.mean < self.mean_lower_threshold:
            print(
                f"Drift detected in {self.name} (rolling average ({self.mean}) exceeded threshold range ({self.mean_lower_threshold}, {self.mean_upper_threshold}))")
            drift_detected = True
        return drift_detected


if __name__ == "__main__":
    from generate_data import DriftingDataset
    import time
    dataset = DriftingDataset()
    feature_1_drift_detector = DriftDetector("feature 1")
    feature_2_drift_detector = DriftDetector("feature 2")
    label_drift_detector = DriftDetector("label")
    for example in dataset:
        print(example)
        time.sleep(.1)
        feature_1_drift_detector.monitor(example[0][0])
        feature_2_drift_detector.monitor(example[0][1])
        label_drift_detector.monitor(example[1])


# %%
