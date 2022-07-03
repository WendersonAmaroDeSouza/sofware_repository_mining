from pydriller import Repository
import pandas as pd
from repositories import list_all_repositories_by_category
from commits import get_commit_metadatas
from group_repository_metadatas import get_filtred_repository_metadatas

categories = ['100_a_500', '500_a_1000', '1000_a_5000'] # , '50000_a_100000', '100000_a_200000']

df_repositories_dataset = pd.DataFrame()

for category in categories:
    repositories = list_all_repositories_by_category(category)
    for repository in repositories:
        commits_metadatas = []
        commits = repository.traverse_commits()
        for commit in commits:
            commits_metadatas.append(get_commit_metadatas(commit))
        df_repository_metadatas = pd.DataFrame(commits_metadatas)
        df_repository_metadatas['repository_category'] = category
        df_repositories_dataset = pd.concat([df_repositories_dataset, get_filtred_repository_metadatas(df_repository_metadatas)])
        df_repositories_dataset.to_csv('repositories_dataset.csv', sep=';', index=False)
    print(category)
