import git
import os
import datetime  

def get_date(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time)

submissionDate_fileName = {}

from git.objects.commit import Commit 
dir_path = os.path.dirname(os.path.realpath(__file__))

repo = git.Repo(dir_path)
tree = repo.tree()

for blob in tree.trees[1]:
    # print(blob.name)
    # print(blob.path)
    commit = next(repo.iter_commits(paths=blob.path, max_count=1))
    date = str(get_date(commit.committed_date))[:10]
    submissionDate_fileName[blob.name] = date
    
    
print(submissionDate_fileName['1.two-sum.py'])