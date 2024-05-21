import pandas as pd


def get_table(df: pd.DataFrame) -> pd.DataFrame:
    # Загрузка CSV в DataFrame
    # df = pd.read_csv(file)

    first_5 = df.head(5)

    # Получение последних 5 записей
    last_5 = df.tail(5)

    empty_row = pd.DataFrame("...", index=[0], columns=df.columns)
    star_row = pd.DataFrame("*", index=[0], columns=df.columns)

    # Объединение всех частей в новый DataFrame
    new_df = pd.concat([first_5, empty_row, last_5, star_row], ignore_index=True)
    new_df.insert(0, "", "")

    # среднее
    mean_values_list = [
        round(df[col].mean(), 2) if pd.api.types.is_numeric_dtype(df[col]) else "-" for col in df.columns
    ]
    mean_values_list.insert(0, "mean")
    mean_row = pd.DataFrame([mean_values_list], columns=new_df.columns)
    new_df = pd.concat([new_df, mean_row], ignore_index=True)

    # медиана
    median_values_list = [
        round(df[col].median(), 2) if pd.api.types.is_numeric_dtype(df[col]) else "-" for col in df.columns
    ]
    median_values_list.insert(0, "median")
    median_row = pd.DataFrame([median_values_list], columns=new_df.columns)
    new_df = pd.concat([new_df, median_row], ignore_index=True)

    # дисперсия
    var_values_list = [round(df[col].var(), 2) if pd.api.types.is_numeric_dtype(df[col]) else "-" for col in df.columns]
    var_values_list.insert(0, "var")
    var_row = pd.DataFrame([var_values_list], columns=new_df.columns)
    new_df = pd.concat([new_df, var_row], ignore_index=True)

    # стандартное отклонение
    std_values_list = [round(df[col].std(), 2) if pd.api.types.is_numeric_dtype(df[col]) else "-" for col in df.columns]
    std_values_list.insert(0, "std")
    std_row = pd.DataFrame([std_values_list], columns=new_df.columns)
    new_df = pd.concat([new_df, std_row], ignore_index=True)

    # минимум
    min_values_list = [df[col].min() if pd.api.types.is_numeric_dtype(df[col]) else "-" for col in df.columns]
    min_values_list.insert(0, "min")
    min_row = pd.DataFrame([min_values_list], columns=new_df.columns)
    new_df = pd.concat([new_df, min_row], ignore_index=True)

    # максимум
    max_values_list = [df[col].max() if pd.api.types.is_numeric_dtype(df[col]) else "-" for col in df.columns]
    max_values_list.insert(0, "max")
    max_row = pd.DataFrame([max_values_list], columns=new_df.columns)
    new_df = pd.concat([new_df, max_row], ignore_index=True)

    # сумма
    sum_values_list = [df[col].sum() if pd.api.types.is_numeric_dtype(df[col]) else "-" for col in df.columns]
    sum_values_list.insert(0, "sum")
    sum_row = pd.DataFrame([sum_values_list], columns=new_df.columns)
    new_df = pd.concat([new_df, sum_row], ignore_index=True)

    # количество
    count_values_list = [df[col].count() for col in df.columns]
    count_values_list.insert(0, "count")
    count_row = pd.DataFrame([count_values_list], columns=new_df.columns)
    return pd.concat([new_df, count_row], ignore_index=True)
