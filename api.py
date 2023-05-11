from model import Model
from fastapi import FastAPI


model = Model.from_pretrained("params.pt")

# CREATE API
api = FastAPI()

# define data model


class Data:
    name: str
    age: int

# define API endpoints


@api.get("/predict")
def predict(data: Data):

    return {"prediction": model.predict(data)}
