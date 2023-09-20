import pandas as pd
from lib import data_load, data_summary, data_visual

def main():

    data_path = "cars.csv"
    df = pd.read_csv(data_path, sep=';')
    sum_data = data_summary(df)

    print(sum_data)


if __name__ == "__main__":
    main()
