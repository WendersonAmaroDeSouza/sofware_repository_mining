from pydriller import Repository

def get_commit_complexity(commit):
    files = commit.modified_files
    complexity = 0
    for file in files:
        complexity += file.complexity if file.complexity != None else 0
    
    complexity = complexity / len(files)

    return complexity

def list_all_commits(repository_path):
    for commit in Repository(repository_path).traverse_commits():
        print('Hash {}, author {}, date {}'.format(commit.hash, commit.author.name, commit.author_date))
        print({ 
                    'author_date': commit.author_date, 
                    'committer_date': commit.committer_date, 
                    'dmm_unit_complexity': commit.dmm_unit_complexity, 
                    'complexity': get_commit_complexity(commit)
                })
        print(commit.files)

list_all_commits('./')
