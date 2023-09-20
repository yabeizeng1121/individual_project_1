import pandas as pd
from lib 

def main():

    data_path = "cars.csv"
    df = pd.read_csv(data_path, sep=';')

    mean_values = compute_mean(df)
    median_values = compute_median(df)
    mode_values = compute_mode(df)
    std_dev_values = compute_std_dev(df)

    print("Mean Values:", mean_values)
    print("Median Values:", median_values)
    print("Mode Values:", mode_values)
    print("Standard Deviation Values:", std_dev_values)

if __name__ == "__main__":
    main()
