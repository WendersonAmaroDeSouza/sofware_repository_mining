#Repos 100 a 500 stars
software_repositories_paths = [
    'https://github.com/taki0112/Densenet-Tensorflow', 'https://github.com/longcw/MOTDT', 'https://github.com/xiaoshun007/12306Python', 'https://github.com/OrkoHunter/keep'
]

#Repos 500 a 1000 stars
software_repositories_paths2 = [
    'https://github.com/clovaai/CutMix-PyTorch', 'https://github.com/CacheBrowser/cachebrowser', 'https://github.com/kumar-shridhar/PyTorch-BayesianCNN', 'https://github.com/mushorg/conpot' 
]

from pydriller import Repository

#Repos 1000 a 5000 stars
software_repositories_paths3 = [
    'https://github.com/psf/requests', 'https://github.com/tiangolo/fastapi', 'https://github.com/python/cpython', 'https://github.com/3b1b/manim'
]

#Repos 50000 a 100000 stars
software_repositories_paths4 = [
    'https://github.com/tensorflow/models', 'https://github.com/nvbn/thefuck', 'https://github.com/huggingface/transformers', 'https://github.com/django/django'
]

#Repos 100000 a 200000 stars
software_repositories_paths5 = [
    'https://github.com/public-apis/public-apis.git', 'https://github.com/donnemartin/system-design-primer', 'https://github.com/TheAlgorithms/Python', 'https://github.com/vinta/awesome-python'
]

repositorie_paths_by_category = { 
    '100_a_500': software_repositories_paths,
    '500_a_1000': software_repositories_paths2, 
    '1000_a_5000': software_repositories_paths3, 
    '50000_a_100000': software_repositories_paths4, 
    '100000_a_200000': software_repositories_paths5
}

def list_all_repositories_by_category(category):
    repositories = []
    for repository_path in repositorie_paths_by_category.get(category):
        repositories.append(Repository(repository_path))
    return repositories

