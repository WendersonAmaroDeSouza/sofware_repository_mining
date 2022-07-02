from pydriller import Repository
import pandas as pd
from repositories import list_all_repositories_by_category
from commits import get_commit_metadatas

categories = ['100_a_500', '500_a_1000', '1000_a_5000', '50000_a_100000', '100000_a_200000']

for category in categories:
    df_repositories_metadatas = pd.DataFrame()
    repositories = list_all_repositories_by_category(category)
    for repository in repositories:
        commits_metadatas = []
        commits = repository.traverse_commits()
        for commit in commits:
            commits_metadatas.append(get_commit_metadatas(commit))
        df_repository_metadatas = pd.DataFrame(commits_metadatas)
        df_repository_metadatas['repository_category'] = category
        df_repositories_metadatas = pd.concat([df_repositories_metadatas, df_repository_metadatas])
    df_repositories_metadatas.to_csv('repositories.csv', sep=';', index=False)
    exit()
