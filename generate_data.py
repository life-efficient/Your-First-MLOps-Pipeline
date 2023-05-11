# %%
# generate some fake data following some parameterised distribution

import numpy as np
import pandas as pd
import time


class DriftingDataset:
    def __init__(
        self,
        n_samples=100,
        n_features=2,
        mean=0,
        std=1,
        data_drift="linear",
        concept_drift="linear",
    ):
        self.n_samples = n_samples
        self.mean = mean
        self.std = std
        self.n_features = n_features
        self.mapping_weights = np.random.rand(n_features)
        self.mapping_bias = np.random.rand(1)
        self.drift_pattern = "linear"
        self.drift_idx = 0

    def mapping(self, x):
        return np.dot(x, self.mapping_weights) + self.mapping_bias

    def generate_datapoint(self):
        x = np.random.normal(self.mean, self.std, self.n_features)
        return x, self.mapping(x)

    def increase_data_drift(self):
        self.mean += np.random.normal(self.mean, self.std, self.n_features)
        self.std += 0.1
        self.drift_idx += 1

    # def increase_concept_drift(self):
    #     self.mapping_weights += 1
    #     self.mapping_bias += 1
    #     self.concept_drift_idx += 1

    def __iter__(self):
        def _():
            while True:
                yield self.generate_datapoint()
                self.increase_data_drift()
        return _()


if __name__ == "__main__":

    dataset = DriftingDataset()

    for example in dataset:
        print(example)
        time.sleep(1)

for idx, example in enumerate(dataset):
    print(example)
    time.sleep(1)