"""
This is a boilerplate pipeline 'data_aquisition'
generated using Kedro 0.18.7
"""

from typing import Any, Dict, Tuple

from prophet import Prophet
import numpy as np
import pandas as pd
from datetime import date
import gdown

import matplotlib.pyplot as plt
from kedro.extras.datasets.matplotlib import MatplotlibWriter

import lightgbm
from lightgbm import LGBMRegressor

'''def down_files() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    links = ['https://drive.google.com/file/d/1WFqpQXzzmDZO-Dyos2QSPoF1Lz54P-JJ/view?usp=share_link',
             'https://drive.google.com/file/d/16zvVSmAE3EheGFoUCqsq2hQYS_YQBQcB/view?usp=share_link',
             'https://drive.google.com/file/d/1_os7AbH5xJpHlWF4ekZ1zWG6C1knKkTX/view?usp=share_link',
             'https://drive.google.com/file/d/1p4bXfiBNV3YugAK5UnA__ZfO3oXWZXwU/view?usp=share_link']

    outputs = ['/home/ldonatti/teste/data/01_03_22.csv', '/home/ldonatti/teste/data/04_06_22.csv', 
               '/home/ldonatti/teste/data/07_12_22.csv', '/home/ldonatti/teste/data/temperatura.csv']
    
    for i in range(len(links)):
        link = links[i]
        output = outputs[i]
        gdown.download(link, output, quiet=True, fuzzy=True)

    df1 = pd.read_csv(outputs[0], sep=',')
    df2 = pd.read_csv(outputs[1], sep=',')
    df3 = pd.read_csv(outputs[2], sep=',')
    df4 = pd.read_csv(outputs[3], sep=',')

    return df1, df2, df3, df4'''


def downfiles(links:list, outputs:list) -> None:
    
    for i in range(len(links)):
        link = links[i]
        output = outputs[i]
        gdown.download(link, output, quiet=True, fuzzy=True)

    return None
