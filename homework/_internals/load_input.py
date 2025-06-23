import pandas as pd


import os
import zipfile


def load_input(carpeta):
    dfs = []

    for archivo in os.listdir(carpeta):
        if archivo.endswith('.csv.zip'):
            with zipfile.ZipFile(os.path.join(carpeta, archivo)) as z:
                with z.open(z.namelist()[0]) as f:
                    dfs.append(pd.read_csv(f))

    return pd.concat(dfs, ignore_index=True)