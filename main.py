import pandas as pd
from src.preprocessing import orchestrator


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-07-01/weekly_gas_prices.csv')
    datasets = orchestrator(df)

    datasets['diesel'].to_csv(
        'data/processed/diesel.csv',
        index=False
    )
    datasets['gasoline'].to_csv(
        'data/processed/gasoline.csv',
        index=False
    )

    print('Datasets procesados correctamente')


if __name__ == "__main__":
    main()
