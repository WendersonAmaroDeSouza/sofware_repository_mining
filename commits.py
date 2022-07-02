from pydriller import Repository

def get_commit_complexity(commit):
    files = commit.modified_files
    complexity = 0
    for file in files:
        complexity += float(file.complexity) if file.complexity != None else 0.0
    
    complexity = (complexity / len(files)) if len(files) > 0 else 0

    print(complexity)

    return complexity

def get_commit_metadatas(commit):
    commit_metadatas = {
                'project_name': commit.project_name,
                'author_date': commit.author_date,
                'author_name': commit.author.name,
                'committer_date': commit.committer_date,
                'committer_name': commit.committer.name,
                'dmm_unit_complexity': commit.dmm_unit_complexity,
                'complexity': get_commit_complexity(commit),
                'num_files': len(commit.modified_files)
            }
    
    return commit_metadatas
