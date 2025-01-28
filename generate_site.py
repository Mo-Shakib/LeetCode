import json

# Load the problems.json file
with open("problems.json", "r") as file:
    problems = json.load(file)

# Generate the HTML file
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <title>My LeetCode Solutions</title>
  <style>
  body {{
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
  }}
  body.dark-mode {{
    background-color: #121212;
    color: #f4f4f4;
  }}
  header {{
    background-color: #007acc;
    color: white;
    padding: 1rem 2rem;
    text-align: center;
  }}
  .container {{
    padding: 2rem;
    max-width: 950px;
    margin: 0 auto;

  }}
  .controls {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 2rem;
  }}
  .controls input {{
    padding: 0.5rem;
    font-size: 1rem;
    width: 70%;
  }}
  .controls button {{
    padding: 0.5rem 1rem;
    font-size: 1rem;
    background-color: #007acc;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }}
  .controls button:hover {{
    background-color: #005fa3;
  }}
  .solution-card {{
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
    padding: 1rem;
  }}
  .solution-card.dark-mode {{
    background: #18181A;
    color: #f4f4f4;
    border: 1px solid #333;
  }}
  .solution-card h2 {{
    margin: 0 0 1rem;
    font-size: 1.5rem;
  }}
  .solution-card pre {{
    background: #f8f8f8;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 1rem;
    overflow-x: auto;
  }}
  .solution-card.dark-mode pre {{
    background: #333;
    color: #f4f4f4;
  }}
  .solution-card a {{
    text-decoration: none;
    color: #007acc;
  }}
  .solution-card a:hover {{
    text-decoration: underline;
  }}
  footer {{
    text-align: center;
    padding: 0.5rem;
    background-color: #007acc;
    color: white;
    position: fixed;
    bottom: 0;
    width: 100%;
    font-size: 0.8rem;
  }}
  footer.dark-mode {{
    background-color: #333;
  }}
  </style>
</head>
<body>
  <header>
  <h1>Shakib's LeetCode Solutions</h1>
  </header>
  <div class="container">
  <div class="controls">
    <input type="text" id="search-input" placeholder="Search for a problem..." />
    <button id="dark-mode-toggle"><i class="fas fa-moon dark-mode-toggle"></i></button>
  </div>
  <div id="solutions-container"></div>
  </div>
  <footer>
  &copy; 2025 Shakib's LeetCode Solutions
  </footer>
  <script src="script.js"></script>
</body>
</html>
"""

# Generate the JavaScript file
js_content = f"""const problems = {json.dumps(problems, indent=2)};
const container = document.getElementById("solutions-container");
const searchInput = document.getElementById("search-input");
const darkModeToggle = document.getElementById("dark-mode-toggle");

// Function to render the problems
function renderProblems(filter = "") {{
  container.innerHTML = ""; // Clear the container
  const filteredProblems = problems.filter(problem =>
  problem.title.toLowerCase().includes(filter.toLowerCase())
  );

  filteredProblems.forEach(problem => {{
  const card = document.createElement("div");
  card.className = "solution-card";

  card.innerHTML = `
    <h2>${{problem.title}}</h2>
    <p><strong>Status:</strong> ${{problem.status}}</p>
    <p><strong>Runtime:</strong> ${{problem.runtime}}</p>
    <p><strong>Memory:</strong> ${{problem.memory}}</p>
    <a href="${{problem.url}}" target="_blank">View Problem</a>
    <h3>Solution:</h3>
    <pre>${{problem.code}}</pre>
  `;

  container.appendChild(card);
  }});
}}

// Event listener for the search input
searchInput.addEventListener("input", () => {{
  renderProblems(searchInput.value);
}});

// Dark mode toggle
let isDarkMode = false;

darkModeToggle.addEventListener("click", () => {{
  isDarkMode = !isDarkMode;
  document.body.classList.toggle("dark-mode", isDarkMode);
  document.querySelectorAll(".solution-card").forEach(card => {{
  card.classList.toggle("dark-mode", isDarkMode);
  }});
  document.querySelector("footer").classList.toggle("dark-mode", isDarkMode);
}});

// Initial render
renderProblems();
"""

# Write the HTML and JS files
with open("index.html", "w") as html_file:
    html_file.write(html_content)

with open("script.js", "w") as js_file:
    js_file.write(js_content)

print("Static site files with search and dark mode functionality generated successfully!")
