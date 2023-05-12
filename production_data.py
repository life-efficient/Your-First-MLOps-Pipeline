# %%
import pandas as pd
from time import sleep
from numpy.random import uniform


class RealWorldDataStream():
    def __init__(self, labels=False):
        self.df = pd.read_csv(
            "https://raw.githubusercontent.com/life-efficient/Your-First-MLOps-Pipeline/main/data/production_data.csv")
        # list of dict
        if not labels:
            self.df.drop("used_offer", axis=1, inplace=True)
        self.df = self.df.to_dict(orient="records")

    def __iter__(self):
        def _():
            while True:
                for row in self.df:
                    yield pd.DataFrame([row])
                    # sleep for a random amount of time
                    sleep(uniform(0, 0.1))

        return _()


if __name__ == "__main__":
    for datapoint in RealWorldDataStream():
        print(datapoint)
        print(type(datapoint))
        break
# %%
