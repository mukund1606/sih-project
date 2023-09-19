from typing import Annotated

from fastapi import FastAPI, Form
from model import Model

app = FastAPI()

model = Model()
iteration = 0


def loadModel(inputData):
    global iteration, model  # Training Again After Saving New Data
    iteration += 1
    model.saveParameters(
        inputData["weather"], inputData["moisture"], inputData["cropType"]
    )
    prediction = model.makePrediction()
    model.saveData()

    if iteration > 5:
        model.modelName = "New Model"
        iteration = 0
    return {"data": prediction, "model": model.modelName}


@app.post("/predict")
def read_item(
    weather: Annotated[str, Form()],
    moisture: Annotated[str, Form()],
    cropType: Annotated[str, Form()],
):
    prediction = loadModel(
        {"weather": weather, "moisture": moisture, "cropType": cropType}
    )
    return {"message": prediction}
