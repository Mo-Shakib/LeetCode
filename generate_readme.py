import json

# Load the problems.json file
with open("problems.json", "r") as file:
    problems = json.load(file)

# Generate the README.md file
readme_content = f"""# Shakib's LeetCode Solutions

Welcome to my LeetCode solutions repository! This project showcases my solutions to various LeetCode problems, along with their runtime, memory usage, and links to the original problems.

## Features

- **Search Functionality**: Easily search for specific problems by title.
- **Dark Mode**: Toggle between light and dark mode for better readability.
- **Responsive Design**: The site is fully responsive and works well on all devices.

## How to Use

1. Open [LeetCode Solution](https://mo-shakib.github.io/LeetCode/) in your browser.
2. Use the search bar to find specific problems.
3. Toggle dark mode using the moon icon in the top-right corner (if you prefer dark mode).

## Problems List

Below is a list of problems included in this repository:

| Title | Status | Runtime | Memory | Solution |
|-------|--------|---------|--------|----------|
"""

# Add the list of problems to the README content
for problem in problems:
    readme_content += f"| [{problem['title']}]({problem['url']}) | {problem['status']} | {problem['runtime']} | {problem['memory']} | [View Solution](https://mo-shakib.github.io/LeetCode/) |\n"

# Add a footer to the README content
readme_content += """

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
"""

# Write the README.md file
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)

print("README.md file generated successfully!")