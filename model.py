class Model:
    modelName = "Model"

    def saveParameters(self, weather, moisture, cropType) -> None:
        self.weather = weather
        self.moisture = moisture
        self.cropType = cropType
        print("Loading Model")

    def makePrediction(self) -> dict:
        return {
            "weather": self.weather,
            "moisture": self.moisture,
            "cropType": self.cropType,
        }

    def saveData(self) -> None:
        with open("data.txt", "a") as f:
            f.write(f"{self.weather}, {self.moisture}, {self.cropType}\n")
        print("Saving Data")
