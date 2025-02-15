from pathlib import Path
import pandas as pd
import numpy as np
import joblib


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts\model_trainer\model.joblib'))

    def prediction(self, data):
        prediction = self.model.predict(data)

        return prediction