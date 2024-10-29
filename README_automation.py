# GitHub README.md automation script by Mohammad Shakib
# This script can automatically update the readme file based on the files present in the repo.
# Last update: 29-11-2024
# Version - v3.5.0

import os, time, markdown, re
from datetime import datetime


def get_date(epoch_time):
    return datetime.fromtimestamp(epoch_time)
    
def create_problem_description_file(file_path, root_directory):
    filename = os.path.basename(file_path)
    description_filename = os.path.splitext(filename)[0] + ".md"  # Save description as .md
    description_path = os.path.join(root_directory, description_filename)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    title = ""
    url = ""
    description_lines = []
    code_lines = []
    start_description = False
    start_code = False

    for line in lines:
        if re.match(r"# \[\d+\]", line):  # Detects line containing "[ID] Title"
            title_info = line.split(" ", 2)
            problem_id = title_info[1].strip("[]")
            title = title_info[2].strip()
        elif "https://" in line:  # Detects URL line
            url = line.strip("# ").strip()
        elif line.strip().startswith("#") and start_description:  # Adds lines to the description
            description_lines.append(line.strip("# ").strip())
        elif line.strip().startswith("#") and "Given" in line:  # Start description collection at "Given"
            start_description = True
            description_lines.append(line.strip("# ").strip())
        
        # Extract code between # @lc code=start and # @lc code=end, excluding those markers
        if line.strip() == "# @lc code=start":
            start_code = True
        elif line.strip() == "# @lc code=end":
            start_code = False
        elif start_code:
            code_lines.append(line.rstrip())

    
    # Description
    description_content = f"# {title}\n\n**URL**: [{url}]({url})\n\n**Description**:\n" + "\n".join(description_lines[2:-2]) + "\n\n"
    code_content = "\n".join(code_lines)

    formatted_description_content = format_description(description_content)

    # Save to the root directory as a .md file (overwrite if exists)
    with open(description_path, 'w') as desc_file:        
        desc_file.write(formatted_description_content)
        desc_file.write("**Solution Code**:\n")
        desc_file.write("```python\n")
        desc_file.write(code_content)
        desc_file.write("\n```\n")
    
    print(f"[+] Problem description file created at {description_path}")
    return problem_id, title, url, description_filename

def format_description(content):
    lines = content.splitlines()
    formatted_lines = []
    
    in_code_block = False  # Track whether we're currently in a code block

    for line in lines:
        if line.startswith("Example") or line.startswith("Constraints"):
            # Close previous code block if applicable
            if in_code_block:
                formatted_lines.append("```")
                in_code_block = False
            
            formatted_lines.append('\n __'+line+'__')  # Add the example or constraint line

            formatted_lines.append("```")  # Open a new code block
            in_code_block = True  # We're in a code block now
        elif line.startswith("**Code**:") or line.startswith("Follow up:"):
            # Close the last code block when reaching "**Code**:"
            if in_code_block:
                formatted_lines.append("```")
                in_code_block = False
            formatted_lines.append(line)  # Add the "**Code**:" line
        elif line.startswith('**Description**'):
            formatted_lines.append("\n**Description**")
        
        else:
            # Add line normally if it's not empty
            if line:
                if in_code_block:
                    formatted_lines.append(line)
                else:
                    formatted_lines.append(line)

    # Close the last code block if we're still in one
    if in_code_block:
        formatted_lines.append("```")
    formatted_lines.append('\n')
    return "\n".join(formatted_lines)


def process_directory(root_directory):
    subdirectories = ["easy", "medium", "hard"]
    
    # Custom header for the README.md file
    readme_header = """# LeetCode Solutions

[![wakatime](https://wakatime.com/badge/github/Mo-Shakib/LeetCode.svg)](https://wakatime.com/badge/github/Mo-Shakib/LeetCode) ![example workflow](https://github.com/Mo-Shakib/LeetCode/actions/workflows/Readme-automation.yml/badge.svg)

<a href="https://leetcode.com/Mo-Shakib"><img src="https://leetcode.card.workers.dev/Mo-Shakib?theme=dark&font=baloo&extension=null&border=0.2"></a>

[LeetCode](https://leetcode.com/) is a website containing many algorithm questions. Most of them are real interview questions of Google, Facebook, LinkedIn, Apple, etc. and it always help to sharp our algorithm skills. This repo shows my solutions in Python. Hit the STAR to support this repo, thank you!

### Repository Structure
**The repository is organized into three main folders based on difficulty:**
```
LeetCode-Solutions/
├── easy/
│   ├── [Problem ID]-problem-name.py
│   ├── ...
│
├── medium/
│   ├── [Problem ID]-problem-name.py
│   ├── ...
│
├── hard/
│   ├── [Problem ID]-problem-name.py
│   ├── ...
|
└── README.md
```
"""

    readme_lines = [readme_header]

    for subdir in subdirectories:
        dir_path = os.path.join(root_directory, subdir)
        if os.path.exists(dir_path):
            # Start new section for each difficulty level
            readme_lines.append(f"\n\n## {subdir.capitalize()}\n")
            for filename in os.listdir(dir_path):
                if filename.endswith(".py"):
                    file_path = os.path.join(dir_path, filename)
                    problem_id, title, url, description_filename = create_problem_description_file(file_path, root_directory)
                    # Add entry to the section's list format
                    readme_lines.append(f"- [{title}]({url}) - [Solution]({description_filename})")
    
    
    readme_path = os.path.join(root_directory, "README.md")
    with open(readme_path, 'w') as readme_file:
        readme_file.write("\n".join(readme_lines))
    
    print(f"[+] README.md file created at {readme_path}")


root_directory = os.path.dirname(__file__)
process_directory(root_directory)

# print('[=] Task Successfull')

# current_time = datetime.now(pytz.timezone('Asia/Dhaka'))
# current_time = current_time.strftime("%d %B, %Y | %H:%M:%S")

# readme_edit.write('\n\n\n')
# readme_edit.write(f'__Last update:__ {current_time}')

print('[=] README.md updated.')
time.sleep(1)

# Writing website for the readme
print('Writing index.html file')
markdown.markdownFromFile(
    input='README.md',
    output='index.html',
    encoding='utf8',
)
print('Done writing index.html')

print("[+] Adding changes to GitHub")

print("[=] Successfull")
