import pandas as pd
from typing import List, TypeVar
from pydantic import ValidationError

# Generic type variable for model
T = TypeVar("T")  

def validate_data(data: List[T], model_class: T) -> bool:

    """

    Validate a list of data objects against a given Pydantic model class.
    Returns True if all are valid, otherwise raises ValidationError.

    """

    for item in data:
        try:
            # If item is already an instance of the model, skip re-validation
            if not isinstance(item, model_class):
                model_class(**item)
        except ValidationError as e:
            print("Validation error:", e)
            return False
    return True

def to_dataframe(data: List[T]):

    """

    Convert a list of Pydantic model instances to a pandas DataFrame.

    """

    # Convert each model instance to dict, then create DataFrame
    data_dicts = [item.dict() for item in data]
    return pd.DataFrame(data_dicts)

def export_data(data: List[T], output_path: str, file_format: str = "csv"):
    
    """

    Export data to CSV
    
    """

    df = to_dataframe(data)
    
    if file_format.lower() == "csv":
        df.to_csv(output_path, index=False)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")

    print(f"Data exported to {output_path}")