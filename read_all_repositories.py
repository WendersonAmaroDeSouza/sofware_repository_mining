from pydriller import Repository
import read_commits_from_repositories as commits
from resources import software_repositories

def list_all_repositories():
    repository = None
    for repository_resource in software_repositories:
        repository = Repository(repository_resource.get('path'))
        print(repository)
    return repository

repository = list_all_repositories()

print(dir(repository.__dict__.get('_conf')))