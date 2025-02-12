import pandas as pd

def read_data():
    df = pd.read_csv('/home/alexandrejacqueline/code/alexandrejacqueline/pyton_101/101/result.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    return df

def aggregate_data(df):
    resample_df = df.groupby([pd.Grouper(freq='30S'), 'level']).size().unstack(fill_value=0)
    return resample_df

if __name__ == '__main__':
    df = read_data()
    resampled_df = aggregate_data(df)
    resampled_df.to_csv('/home/alexandrejacqueline/code/alexandrejacqueline/pyton_101/101/resampled.csv')
    print(resampled_df)
