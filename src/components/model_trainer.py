import numpy as np
import pandas as pd
import os
import sys

from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBRegressor
from src.utils import save_object, evaluate_model
from src.logger import logging
from src.exception import CustomException

from dataclasses import dataclass

@dataclass
class ModelTrainerConfig():
    model_train_obj_file_path=os.path.join("artifact", "model.pkl")

class ModelTrainer():
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_train(self, train_array, test_array):
        try:
            logging.info("Initiate model train")

            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(), 
                "AdaBoost Regressor": AdaBoostRegressor()
                }
            
            model_evaluation:dict=evaluate_model(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,
                                           models=models)
            
            max_score=max(sorted(model_evaluation.values()))

            best_model=list(model_evaluation.keys())[
                list(model_evaluation.values()).index(max_score)
            ]

            model_name=models[best_model]

            if max_score<0.6:
                raise CustomException("no best model found")
            
            logging.info("Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.model_train_obj_file_path,
                obj=model_name
            )

            y_pred=model_name.predict(X_test)
            r2_square=r2_score(y_test, y_pred)

            return r2_square

        except Exception as e:
            raise CustomException(e, sys)
        


