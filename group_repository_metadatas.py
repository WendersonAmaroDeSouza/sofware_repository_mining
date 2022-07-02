import pandas as pd
from datetime import datetime

df_repository_metadatas = pd.read_csv('repositories.csv', sep=';')

df_repository_metadatas = df_repository_metadatas[['repository_category', 'project_name', 'author_name', 'author_date', 'dmm_unit_complexity', 'complexity']]
df_repository_metadatas = df_repository_metadatas[~df_repository_metadatas['dmm_unit_complexity'].isna()]
df_repository_metadatas['year'] = df_repository_metadatas['author_date'].apply(lambda x : datetime.fromisoformat(x).year )
df_repository_metadatas['month'] = df_repository_metadatas['author_date'].apply(lambda x : datetime.fromisoformat(x).month )
df_repository_metadatas = df_repository_metadatas.drop(columns='author_date')

df_repository_metadatas = df_repository_metadatas.groupby(by=['year', 'month', 'project_name', 'repository_category'], as_index=False).agg({
    'author_name': pd.Series.unique,
    'dmm_unit_complexity': ['sum'],
    'complexity': ['sum']
})

df_repository_metadatas = df_repository_metadatas.reset_index()

# df_repository_metadatas['contribuitors_number'] = df_repository_metadatas['author_name'].apply(lambda x : len(x))

print(df_repository_metadatas.columns)
