import pins
from pyprojroot.here import here
import polars as pl
import pandas as pd

csv_file_path = "https://catalogue.data.gov.bc.ca/dataset/4cc207cc-ff03-44f8-8c5f-415af5224646/resource/9a9f14e1-03ea-4a11-936a-6e77b15eeb39/download/childcare_locations.csv"

data = pd.read_csv(csv_file_path)
board = pins.board_folder("board")

board.pin_write(data.head(), "bcchildcare", type="csv")
print("bcchildcare Data pinned successfully to the board.")
