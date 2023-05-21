import os
import pandas as pd


path2df = 'data/records.csv'

df = pd.DataFrame(columns=[
    'date',
    'user_name',
    'user_id',
    'general_grade',
    'emoji',
    'description'
]) if not os.path.isfile(path2df) else pd.read_csv(path2df)


def df_append(date: int, user_name: str, user_id: int, general_grade, emoji, description):
    df.loc[df.shape[0]] = [date, user_name, user_id, general_grade, emoji, description]
    df.to_csv(path2df, index=False, encoding='utf-8')


def df_delete(user_id: int):
    clear_df = df
    if df[df['user_id'] == user_id].shape[0] != 0:
        clear_df = df.drop([df.index[df['user_id'] == user_id].tolist()[-1]])
    clear_df.to_csv(path2df, index=False, encoding='utf-8')


def df_show(user_id: int):
    slice_df = df[df['user_id'] == user_id]
    path2slice = f'data/slices/{user_id}.csv'
    slice_df.to_csv(path2slice, index=False)
    return path2slice
