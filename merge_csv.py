import pandas 
import os
import sys

def merge_csv(csv_dir, output_file):
    csv_list = os.listdir(csv_dir)
    csv_list = [e for e in csv_list if e.endswith(".csv")]
    csv_list = [os.path.join(csv_dir, csv) for csv in csv_list]
    df_list = []
    for csv in csv_list:
        df = pandas.read_csv(csv)
        df_list.append(df)
    df = pandas.concat(df_list)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    csv_dir = "./"
    output_file = "./output/all.csv"
    merge_csv(csv_dir, output_file)