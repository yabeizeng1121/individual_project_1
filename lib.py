# loading packages
import warnings
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def load_data(data_path):
    my_data = pd.read_csv(data_path, sep=';')
    return my_data


def data_summary(data):
    main_sum = data.describe()
    return main_sum

def data_visual(data):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sns.set_theme(style="ticks", palette="pastel")
        sns.boxplot(x='Origin', y='Weight', palette="Blues", data=data)
        plt.show()

def main():
    my_df = load_data("cars.csv")
    print(data_summary(my_df))
    data_visual(my_df)
    
if __name__ == "__main__":
    main()
