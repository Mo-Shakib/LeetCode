# GitHub README.md automation script by Mohammad Shakib
# This script can automatically update the readme file based on the files present in the repo.
# Last update: 29-11-2024
# Version - v4.0.0

import os, time, markdown2, re
from datetime import datetime

# Function to convert README.md to responsive HTML file

def markdown_table_to_html_list(markdown_content):
    """Converts markdown tables to HTML unordered list format."""
    # Regex pattern to match markdown tables
    table_pattern = re.compile(
        r"(\| ID \| Title \| Solution \|)(\n\|[-:]+\|[-:]+\|[-:]+\|)(\n(\|.*?\|)+)",
        re.DOTALL
    )

    # Find all matches of the markdown table
    matches = table_pattern.findall(markdown_content)

    for match in matches:
        # Extract the entire table string
        table_string = ''.join(match)  # Combine the matched groups

        # Initialize the unordered list
        list_content = "<ul>\n"

        # Split the table string into rows
        rows = table_string.strip().split("\n")[2:]  # Skip header and separator

        for row in rows:
            columns = [col.strip() for col in row.split("|") if col.strip()]
            if len(columns) == 3:
                list_content += f"""
                <li><strong>ID:</strong> {columns[0]} | <strong>Title:</strong> <a href="{columns[1]}">{columns[1]}</a> | <strong>Solution:</strong> <a href="{columns[2]}">{columns[2]}</a></li>\n
                """

        list_content += "</ul>\n"

        # Replace the markdown table with the generated HTML list
        markdown_content = markdown_content.replace(table_string, list_content)

    return markdown_content

def convert_markdown_to_html(input_file, output_file):
    # Read the markdown content
    with open(input_file, 'r') as md_file:
        markdown_content = md_file.read()

    # Convert markdown table to HTML list format
    markdown_content = markdown_table_to_html_list(markdown_content)

    # Convert markdown to HTML
    html_content = markdown2.markdown(markdown_content)

    # Responsive CSS style for general page
    css_style = """
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            max-width: 900px;
            margin: auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ddd;
            background-color: #f9f9f9;
            border-radius: 5px;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
    </style>
    """

    # Wrap HTML content with responsive HTML layout
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LeetCode Solutions</title>
        {css_style}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Write the full HTML to output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(full_html)

    print(f"[+] Converted {input_file} to responsive HTML at {output_file}")


    
def create_problem_description_file(file_path, src_directory):
    filename = os.path.basename(file_path)
    description_filename = os.path.splitext(filename)[0] + ".md"  # Save description as .md
    description_path = os.path.join(src_directory, description_filename)
    
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
        elif line.strip().startswith("#") and "Testcase Example" in line:  # Start description collection at "Given"
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
    description_content = f"# {title}\n\n**URL**: [{url}]({url})\n\n**Description**:\n" + "\n".join(description_lines[1:-2]) + "\n\n"
    code_content = "\n".join(code_lines)

    formatted_description_content = format_description(description_content)

    # Save to the /src directory as a .md file (overwrite if exists)
    with open(description_path, 'w') as desc_file:        
        desc_file.write(formatted_description_content)
        desc_file.write("**Solution Code**:\n")
        desc_file.write("```python\n")
        desc_file.write(code_content)
        desc_file.write("\n```\n")
    
    # print(f"[+] Problem description file created at {description_path}")
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
            formatted_lines.append("\n**Description:**\n")
        
        else:
            if line:
                if in_code_block:
                    formatted_lines.append(line)
                else:
                    formatted_lines.append(line)

    if in_code_block:
        formatted_lines.append("```")
    formatted_lines.append('\n')
    return "\n".join(formatted_lines)


def process_directory(root_directory):
    subdirectories = ["easy", "medium", "hard"]
    
    # Set the /src directory path
    src_directory = os.path.join(root_directory, "src")
    os.makedirs(src_directory, exist_ok=True)
    
    # Custom header for the README.md file
    readme_header = """# LeetCode Solutions

[![wakatime](https://wakatime.com/badge/github/Mo-Shakib/LeetCode.svg)](https://wakatime.com/badge/github/Mo-Shakib/LeetCode) ![Gihtub workflow](https://github.com/Mo-Shakib/LeetCode/actions/workflows/Readme-automation.yml/badge.svg)

<a href="https://leetcode.com/Mo-Shakib"><img src="https://leetcode.card.workers.dev/Mo-Shakib?theme=dark&font=baloo&extension=null&border=0.2"></a>

Welcome to my repository of LeetCode solutions! This collection includes my answers to various LeetCode problems, organized by difficulty. Each solution is written in Python. Hit the STAR to support this repo, thank you!

### Repository Structure
**The repository is organized into three main folders based on difficulty:**

```
LeetCode/
    ├── easy/
    ├── medium/
    |── hard/
    |── src/
    └-- README.md
```
"""

    readme_lines = [readme_header]

    for subdir in subdirectories:
        dir_path = os.path.join(root_directory, subdir)
        if os.path.exists(dir_path):
            # Start new section for each difficulty level
            readme_lines.append(f"\n\n## {subdir.capitalize()}\n")
            # Table headers
            readme_lines.append("| ID |              Title                 | Solution |")
            readme_lines.append("|----|------------------------------------|----------|")
            for filename in os.listdir(dir_path):
                if filename.endswith(".py"):
                    file_path = os.path.join(dir_path, filename)
                    problem_id, title, url, description_filename = create_problem_description_file(file_path, src_directory)
                    # Add entry to the table with links
                    readme_lines.append(f"| {problem_id} | [{title}]({url}) | [Python](src/{description_filename}) |")
    
    
    readme_path = os.path.join(root_directory, "README.md")
    with open(readme_path, 'w') as readme_file:
        readme_file.write("\n".join(readme_lines))
    
    print(f"[+] README.md file created at {readme_path}")

    # Convert README.md to responsive HTML
    output_html_path = os.path.join(root_directory, "index.html")
    convert_markdown_to_html(readme_path, output_html_path)

    print('[=] README.md and HTML conversion completed.')


# Run the main function on the root directory
root_directory = os.getcwd()
process_directory(root_directory)
