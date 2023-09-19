import polars as pl  
from lib import load_data, data_summary, data_visual


def main():

    data_path = "cars.csv"
    df = pl.read_csv(data_path)  

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
