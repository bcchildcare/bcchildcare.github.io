import pins
from pyprojroot.here import here
import polars as pl
import pandas as pd

csv_file_path = "https://catalogue.data.gov.bc.ca/dataset/4cc207cc-ff03-44f8-8c5f-415af5224646/resource/9a9f14e1-03ea-4a11-936a-6e77b15eeb39/download/childcare_locations.csv"
data = pd.read_csv(csv_file_path)
print("Data downloaded and loaded")

# get the latest date
data_pl = pl.from_pandas(data)
data_pl = data_pl.with_columns(
    pl.col("VACANCY_LAST_UPDATE").str.to_date("%Y/%m/%d", strict=False)
)

latest_date = data_pl.select(pl.col("VACANCY_LAST_UPDATE")).to_series().max()
print(f"Latest date: {latest_date}")

# create popup text
def createPopup(row: dict):
    """
    Uses multiple columns to create text for the popup
    """

    tab = "&nbsp;&nbsp;&nbsp;&nbsp;"
    text = f'{row["NAME"]}<br>{row["NAME"]}<br>{row["PHONE"]}<br><br>'
    text += "Vacancy:"
    text += f"{tab}<36 months: {row['VACANCY_SRVC_UNDER36']}<br>"
    text += f"{tab}30 months -- 5 years: {row['VACANCY_SRVC_30MOS_5YRS']}<br>"
    text += f"{tab}Preschool: {row['VACANCY_SRVC_LICPRE']}<br>"
    text += f"{tab}Grade 1 - Age 12: {row['VACANCY_SRVC_OOS_GR1_AGE12']}<br>"
    
    # do some work
    return text

data_pl = data_pl.with_columns(
    pl.struct(pl.all()).map_elements(createPopup, return_dtype = pl.String).alias("popup")
)
print("Created popup text")


# write data to board
board = pins.board_folder(here("board"))
board.pin_write(data_pl, "bcchildcare", type="csv", metadata={"date": latest_date})
board.pin_meta("bcchildcare")