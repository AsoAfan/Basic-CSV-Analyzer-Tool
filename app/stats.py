import numpy as np
import pandas as pd


def compute_statistics(data: pd.Series) -> str:
    mean = np.mean(data)
    median = np.median(data)
    mode = data.mode().values
    std_dev = np.std(data)

    stats_text = (
        f"Mean: {mean:.2f}\n"
        f"Median: {median:.2f}\n"
        f"Mode: {', '.join(map(str, mode)) if mode.shape[0] != data.shape[0] else "All data are common"}\n" 
        f"Standard Deviation: {std_dev:.2f}"
    )
    return stats_text
