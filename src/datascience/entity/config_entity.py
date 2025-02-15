from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    

@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE: str
    unzip_data_dir:Path
    all_schema:dict


@dataclass
class DataTransformationConfig:
    root_dir:Path
    data_path:Path


@dataclass
class ModelTrainerConfig:
    root_dir:Path
    train_data_path: Path
    test_data_path: Path
    model_name:str
    target_column:str
    alpha: float
    l1_ratio: float


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_path: Path
    all_params: dict
    target_column: str
    mlflow_uri: str

from pathlib import Path
from dataclasses import dataclass

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_path: Path
    all_params: dict
    target_column: str
    mlflow_uri: str
    


