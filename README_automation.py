# GitHub README.md automation script by Mohammad Shakib
# This script can automatically update the readme file based on the files in the repo.
# Last update: 06-01-2022

import os
import git

readme = open("README.md", "r")
question = open("all-leetcode-questions.txt", "r")

all_files = []
valid_ids = [str(x) for x in range(1, 100000)]
all_files_id = []
old_files = []
file_data = {}
skip_files = ['test.py', 'main.py']
problem_details = {}

for line in question:
    line = line.strip()
    x = line.split(',')
    problem_details[int(x[0])] = x[1:]
question.close()

for files in os.listdir("Python"):
    if files.endswith(".py"):
        if files not in skip_files:
            all_files.append(files)
            file_id = files.split(".")[0]
            all_files_id.append(file_id)
            file_data[file_id] = files

for i in readme.readlines():
    try:
        x = i.split("|")
        if x[1] in valid_ids:
            old_files.append(x[1])
    except IndexError:
        pass

newfiles = list(set(all_files_id) - set(old_files))

if len(newfiles) == 0:
    print("[!] No new file found")
else:
    n = 0
    for i in newfiles:
        print('[+] Adding:',file_data[i])
        n += 1
    print(f'[=] Total {n} files indexed.')


leetcode_url = "https://leetcode.com/problems/"

readme_edit = open("README.md", "a")
for x in newfiles:
    problem_id = file_data[x].split(".")[0]
    url = leetcode_url + file_data[x].split(".")[1]
    problem_name = file_data[x].split(".")[1].strip()
    problem_name = problem_name.replace("-", " ")
    try:
        problem_info = problem_details[int(problem_id)]
    except KeyError:
        problem_info = ['-','-','-'] 
    readme_edit.write(f"|{problem_id}|[{problem_name.capitalize()}]({url})|[Python](Python/{file_data[x]})|{problem_info[2]}|{problem_info[1]}|\n")

readme_edit.close()

print("[+] Adding files to git")

commit_message = "Updated"

repo = git.Repo("/home/runner/work/LeetCode/LeetCode/")

repo.git.add('--all')
repo.git.commit('-m', commit_message, author='Shakib')
origin = repo.remote(name='origin')
origin.push()

print("[=] Successfull")