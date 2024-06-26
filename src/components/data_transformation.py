import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from src.logger import logging
from src.exception import CustomException
import os
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifact", "preprocessor.pkl")

class DataTransformation: 
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transform_object(self):

        """ This Function is responsible for data transformation and scaling"""

        try:
            numerical_columns=['writing_score', 'reading_score']
            categorical_columns= [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course',

            ]

            num_pipeline = Pipeline(

                steps=[
                    ("Imputer", SimpleImputer(strategy='median')),
                    ("Standard Scaler", StandardScaler())


                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                    ("Imputer", SimpleImputer(strategy='most_frequent')),
                    ("One HOt Encoding", OneHotEncoder()),
                    ("Standard Scaler", StandardScaler(with_mean=False))

                ])
            
            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns: {categorical_columns}")
            
            preprocessor = ColumnTransformer(

                [
                    ("Numerical Features", num_pipeline, numerical_columns),
                    ("Categorical Features", cat_pipeline, categorical_columns)


                ])
            
            return preprocessor
            
        except Exception as e:
           raise CustomException(e, sys)


    def initiate_data_trasformation(self, train_path, test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info('Reading of train and test data completed')
            
            logging.info("Creating pre-processor object")

            preprocessor_obj=self.get_data_transform_object()

            target_column='math_score'
            numerical_columns=['writing_score', 'reading_score']

            input_feature_train_df=train_df.drop(columns=[target_column], axis=1)
            target_feature_train_df=train_df[target_column]

            input_feature_test_df=test_df.drop(columns=[target_column], axis=1)
            target_feature_test_df=test_df[target_column]            

            logging.info("Completed Transformation of training and testing data")

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

            train_arr=np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ] 

            test_arr=np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]    

            logging.info("Saved preprocessor object after applying on training and testing dataframe")

            save_object(

                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj

            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)
            