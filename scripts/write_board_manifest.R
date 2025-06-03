library(pins)
library(here)

board <- board_folder(here("board"))
board |> write_board_manifest()