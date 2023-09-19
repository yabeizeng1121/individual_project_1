from lib import load_data, data_summary

def df_loading(data_path):
    return load_data(data_path)

def data_describe(data):
    return data_summary(data)

