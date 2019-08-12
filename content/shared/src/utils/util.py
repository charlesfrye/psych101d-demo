import pandas as pd

def samples_to_dataframe(samples):
    return pd.DataFrame([sample for sample in samples])
