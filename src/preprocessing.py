import pandas as pd


def prepare_dates(df):
    if 'date' not in df.columns:
        raise ValueError('La columna date no está en el dataframe')

    df_copy = df.copy()
    df_copy['date'] = pd.to_datetime(
        df_copy['date'],
        format='%Y-%m-%d',
        errors='coerce'
    )
    df_copy = df_copy[df_copy['date'].notna()]
    return df_copy


def split_by_fuel(df):
    if 'fuel' not in df.columns:
        raise ValueError('No está fuel entre las columnas del dataframe')

    datasets_fuel = {}
    for fu in df['fuel'].unique():
        datasets_fuel[fu] = df[df['fuel'] == fu].copy()

    return datasets_fuel


def clean_diesel(df_diesel):
    if 'grade' not in df_diesel.columns:
        raise ValueError("La columna 'grade' no existe en diésel")

    df_copy = df_diesel.copy()
    return df_copy[df_copy['grade'] != 'all']


def clean_gasoline(df_gasoline, keep_all: bool = True):
    if 'grade' not in df_gasoline.columns:
        raise ValueError('No se encuentra la columna grade')

    df_copy = df_gasoline.copy()
    if not keep_all:
        df_copy = df_copy[df_copy['grade'] != 'all']

    return df_copy


def orchestrator(df):
    if df.empty:
        raise ValueError('El dataframe vino vacío')

    df_date_prep = prepare_dates(df)
    datasets_fuel = split_by_fuel(df_date_prep)

    df_diesel = datasets_fuel['diesel']
    df_gasoline = datasets_fuel['gasoline']

    return {
        'diesel': clean_diesel(df_diesel),
        'gasoline': clean_gasoline(df_gasoline)
    }
