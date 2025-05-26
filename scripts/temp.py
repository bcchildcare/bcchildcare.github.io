from pyprojroot.here import here
import pandas as pd
import polars as pl
import datetime as dt


def get_data_vacancy(file_path):
    """
    Ingests data from a CSV file into a Pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from the CSV file,
                          or None if an error occurs.
    """
    data = pl.read_csv(file_path)

    # extract vacancy data
    data_pl = data.select(pl.col("NAME"), pl.col("VACANCY_SRVC_30MOS_5YRS")).unpivot(
        index=["NAME"], on="VACANCY_SRVC_30MOS_5YRS"
    )
    return data_pl


if __name__ == "__main__":
    csv_file_path = "https://catalogue.data.gov.bc.ca/dataset/4cc207cc-ff03-44f8-8c5f-415af5224646/resource/9a9f14e1-03ea-4a11-936a-6e77b15eeb39/download/childcare_locations.csv"
    data_pl = pl.read_csv(csv_file_path)
    data

    csv_file_path = here("data/2025-05-24 childcare_locations.csv")
    data = get_data_vacancy(csv_file_path)

# get the latest date
    data_pl = data_pl.with_columns(
        pl.col("VACANCY_LAST_UPDATE")
        .str.to_date("%Y/%m/%d", strict=False)
        .alias('VACANCY_LAST_UPDATE_date')
    )
    
    latest_date = (
        data_pl.select(pl.col("VACANCY_LAST_UPDATE_date"))
        .to_series()
        .max()
    )
    
    data_pl.glimpse()
    
    data_pl.filter(
        pl.col("VACANCY_LAST_UPDATE_date") > (latest_date - dt.timedelta(days=7))
    )

    dataset_last_update = max(data$VACANCY_LAST_UPDATE, na.rm = TRUE)
    pl.from_pandas(data).filter(pl.col("VACANCY_LAST_UPDATE") ))

    if data is not None:
        print("Vacancy data ingested successfully:")
        print(data)