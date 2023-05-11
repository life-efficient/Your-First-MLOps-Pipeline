import sklearn
import numpy as np

n_samples = 100
n_features = 2
mean = 0
std = 1

X, y = generate_dataset(n_samples, n_features, mean, std)

model = sklearn.linear_model.LogisticRegression()
model.fit(X, y)

# evaluate model


def evaluate_model(model, X, y):
    return model.score(X, y)

# save model


def save_model(model, path):
    np.save(path, model)
