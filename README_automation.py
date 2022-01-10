# GitHub README.md automation script by Mohammad Shakib
# This script can automatically update the readme file based on the files present in the repo.
# Last update: 10-01-2022
# Version - v2.0.0

import os, time, pytz, git
from LeetCode_problem_info import problem_info
from datetime import datetime
from git.objects.commit import Commit 

# - - - - - - - - - - - - - - - - - - - - - - - - 
def get_date(epoch_time):
    return datetime.fromtimestamp(epoch_time)

submissionDate_fileName = {}


dir_path = os.path.dirname(os.path.realpath(__file__))

repo = git.Repo(dir_path)
tree = repo.tree()

for blob in tree.trees[1]:
    commit = next(repo.iter_commits(paths=blob.path, max_count=1))
    date = str(get_date(commit.committed_date))[:10]
    submissionDate_fileName[blob.name] = date

# - - - - - - - - - - - - - - - - - - - - - - - - - 

all_files = []
all_files_id = []
file_data = {}
submissionTime = {}
skip_files = ['test.py', 'main.py']
driver = problem_info.Get_Info()
problem_details = driver.all_data()
readme_edit = open("README.md", "w")

for files in os.listdir("Python"):
    if files.endswith(".py"):
        if files not in skip_files:
            all_files.append(files)
            file_id = files.split(".")[0]
            all_files_id.append(file_id)
            file_data[file_id] = files + "." + submissionDate_fileName[files]
            print(submissionDate_fileName[files])

newfiles = all_files_id
newfiles_data = {}
for i in newfiles:
    newfiles_data[i] = file_data[i]

print('[*] Updating README.md...')

readme_edit.write('# LeetCode Solutions\n\n')
readme_edit.write('[![wakatime](https://wakatime.com/badge/github/Mo-Shakib/LeetCode.svg)](https://wakatime.com/badge/github/Mo-Shakib/LeetCode)')
readme_edit.write('![example workflow](https://github.com/Mo-Shakib/LeetCode/actions/workflows/Readme-automation.yml/badge.svg)\n\n')
readme_edit.write('<a href="https://leetcode.com/Mo-Shakib"><img src="https://leetcode.card.workers.dev/Mo-Shakib?theme=dark&font=baloo&extension=null&border=0.2"></a>\n')
readme_edit.write('\n\n[LeetCode](https://leetcode.com/) is a website containing many algorithm questions. Most of them are real interview questions of Google, Facebook, LinkedIn, Apple, etc. and it always help to sharp our algorithm skills. This repo shows my solutions in Python. Please feel free to reference and STAR to support this repo, thank you!\n\n\n')

readme_edit.write('|   #   |  Title | Solution | Difficulty | Submission |\n')
readme_edit.write('| ----- |  ----- | -------- | ---------- | ---------- |\n')

newfiles_data = {k: v for k, v in sorted(newfiles_data.items(), key = lambda item: item[1][-10:])}

for key, file_data in newfiles_data.items():
    print(f'[+] Adding: {file_data[:-11]}')
    problem_id = newfiles_data[key].split(".")[0]
    url = "https://leetcode.com/problems/" + newfiles_data[key].split(".")[1]
    problem_name = newfiles_data[key].split(".")[1].strip()
    problem_name = problem_name.replace("-", " ")
    date = newfiles_data[key].split(".")[3]
    filePath = "Python/" + newfiles_data[key][:-11]
    try:
        problem_info = problem_details[int(problem_id)]
    except KeyError:
        problem_info = ['-','-','-'] 
    readme_edit.write(f"| **{problem_id}** | [{problem_name.capitalize()}]({url}) | [Python]({filePath}) | {problem_info[2]}| {date} |\n")

current_time = datetime.now(pytz.timezone('Asia/Dhaka'))
current_time = current_time.strftime("%d %B, %Y | %H:%M:%S")

readme_edit.write('\n\n\n')
readme_edit.write(f'__Last update:__ {current_time}')

print('[=] README.md updated.')
readme_edit.close()
time.sleep(10)
print("[+] Adding changes to GitHub")

commit_message = "Updated by automated commit"
repo.git.add('--all')
repo.git.commit('-m', commit_message, author='Shakib')
origin = repo.remote(name='origin')
origin.push()

print("[=] Successfull")
