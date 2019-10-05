import pandas as pd
from utils.file_utils import FileUtil


class MakeStats:
    def __init__(self):
        pass

    def read_data(self, input_csv_file_path: str):
        # Read csv file into dataframe
        dataframe = FileUtil.csv2dataframe(input_csv_file_path)

        # Clean data

        return dataframe


def main():
    # Init class
    MST = MakeStats()

    # Keyword
    keyword = "陶磁器"

    # Read csv file into dataframe
    dataframe = MST.read_data(f"data/{keyword}.csv")


if __name__ == "__main__":
    main()