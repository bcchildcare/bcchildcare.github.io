import pandas as pd


def ingest_data(file_path):
    """
    Ingests data from a CSV file into a Pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from the CSV file,
                          or None if an error occurs.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty")
        return None
    except pd.errors.ParserError:
        print(f"Error: Failed to parse CSV file '{file_path}'. Check the file format.")
        return None


if __name__ == "__main__":
    from pyprojroot.here import here

    csv_file_path = here("data/2025-05-24 childcare_locations.csv")
    data = ingest_data(csv_file_path)

    if data is not None:
        print("Data ingested successfully:")
        print(data)
