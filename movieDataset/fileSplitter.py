import csv
import pandas as pd
import math

IN_FILE = "movieDataset/ratings.csv"
OUT_FILE = "movieDataset/splitRatings/ratings"
NUM_SPLITS = 8

def write_to_csv(data):
    numRows = len(data)
    rowsPerFile = int(math.ceil(numRows/NUM_SPLITS))

    for i in range(0, NUM_SPLITS):
        newFileName = OUT_FILE + str(i) + ".csv"
        data.iloc[rowsPerFile*i:rowsPerFile*(i+1)].to_csv(newFileName, index=False)

if __name__ == "__main__":
    result = pd.read_csv(IN_FILE)
    write_to_csv(result)
