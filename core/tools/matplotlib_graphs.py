import uuid
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot(df: pd.DataFrame, x: int, y: int, path_for_save: str) -> None:
    plt.figure(figsize=(10, 5), facecolor="#C9DDC4")
    ax = plt.gca()
    ax.set_facecolor("#f4f7d8")
    plt.scatter(df.iloc[:, x].tolist(), df.iloc[:, y].tolist(), color="b", marker="o", s=3)

    # Настройте оси и добавьте заголовок
    plt.xlabel(df.columns[x], loc="right", fontsize=12)
    plt.title(df.columns[y], loc="left")

    # Отобразите легенду
    plt.legend()

    unique_id = uuid.uuid4()
    # Сохранение графика
    plt.savefig(f"{path_for_save}/" + f"plot_{unique_id}.png")


def get_graphs(df: pd.DataFrame) -> str:
    # current_file_path = os.path.abspath(__file__)
    # current_dir_path = os.path.dirname(current_file_path)
    # path = os.path.join(current_dir_path, "products.csv")

    # Загрузка CSV в DataFrame
    # df = pd.read_csv(file)
    numeric_columns = df.select_dtypes(include=np.number)

    # если записей много, берем только случайных 1000
    records_limit = 1000
    if numeric_columns.shape[0] > records_limit:
        numeric_columns = numeric_columns.sample(n=records_limit)

    n = numeric_columns.shape[1] - 1
    # уникальные пары столбцов
    unique_pairs = [(i, j) for i in range(n + 1) for j in range(i, n + 1) if i != j]

    unique_id = uuid.uuid4()
    path = f"media/{unique_id}"
    Path(path).mkdir()
    limit = min(len(unique_pairs), 30)
    for i in range(limit):
        plot(numeric_columns, unique_pairs[i][0], unique_pairs[i][1], path)
    plt.close('all')
    return path
