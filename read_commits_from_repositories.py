from pydriller import Repository

def list_all_commits(repository_path):
    for commit in Repository(repository_path).traverse_commits():
        print('Hash {}, author {}'.format(commit.hash, commit.author.name))

list_all_commits('./')
