import pins
from pyprojroot.here import here
import polars as pl
import pandas as pd

csv_file_path = "https://catalogue.data.gov.bc.ca/dataset/4cc207cc-ff03-44f8-8c5f-415af5224646/resource/9a9f14e1-03ea-4a11-936a-6e77b15eeb39/download/childcare_locations.csv"
data = pd.read_csv(csv_file_path)

# get the latest date
data_pl = pl.from_pandas(data)

data_pl = data_pl.with_columns(
    pl.col("VACANCY_LAST_UPDATE").str.to_date("%Y/%m/%d", strict=False)
)

latest_date = data_pl.select(pl.col("VACANCY_LAST_UPDATE")).to_series().max()

# write data to board
board = pins.board_folder(here("board"))
board.pin_write(data.head(), "bcchildcare", type="csv", metadata={"date": latest_date})

board.pin_meta("bcchildcare")
