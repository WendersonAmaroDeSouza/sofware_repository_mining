from pydriller import Repository

def get_commit_complexity(commit):
    files = commit.modified_files
    complexity = 0
    for file in files:
        complexity += file.complexity if file.complexity != None else 0
    
    complexity = complexity / len(files)

    return complexity

def get_commit_metadatas(commit):
    commit_metadatas = { 
                'author_date': commit.author_date, 
                'committer_date': commit.committer_date, 
                'dmm_unit_complexity': commit.dmm_unit_complexity, 
                'complexity': get_commit_complexity(commit)
            }
    
    return commit_metadatas
