from pydriller import Repository
import read_commits_from_repositories as commits
from resources import software_repositories

def list_all_repositories():
    for repository_resource in software_repositories:
        repository = Repository(repository_resource.get('path'))
        print(repository)

list_all_repositories()