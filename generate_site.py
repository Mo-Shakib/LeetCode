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
  <!-- Prism.js CSS for syntax highlighting -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
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
    background-color: #ffffff;
    color: #3b3b3b;
    padding: 1rem 2rem;
    text-align: center;
    border-bottom: 1px solid orange;
  }}
  header.dark-mode {{
    background-color: #1e1e1e;
    color: #f4f4f4;
    border-bottom: 1px solid #ffa51d;
  }}
  header p {{
    max-width: 850px;
    margin: auto;
  }}
  .container {{
    padding: 2rem;
    max-width: 900px;
    margin: 0 auto;
  }}
  .controls {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 2rem;
  }}
  .controls input {{
    padding: 0.6rem;
    font-size: 1rem;
    width: 70%;
    border-radius: 10px;
    border: none;
  }}
  .controls button {{
    padding: 0.5rem 1rem;
    font-size: 1rem;
    background-color: #ffa51d;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
  }}
  .controls button:hover {{
    background-color: black;
  }}
  .solution-card {{
    background: white;
    border-radius: 15px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
    padding: 1rem;
  }}
  .solution-card.dark-mode {{
    background: #343434;
    color: #f4f4f4;
    border: 1px solid #333;
  }}
  .solution-card h2 {{
    margin: 0 0 1rem;
    font-size: 1.5rem;
  }}
  .solution-card pre {{
    position: relative;
    background: #2d2d2d;
    border-radius: 10px;
    padding: 1rem;
    overflow-x: auto;
    border: none;
    color: #f8f8f8;
  }}
  .solution-card.dark-mode pre {{
    background: #1e1e1e;
  }}
  .solution-card a {{
    text-decoration: none;
    color: #ffa51d;
  }}
  .solution-card a:hover {{
    text-decoration: underline;
  }}
  footer {{
    text-align: center;
    padding: 0.2rem;
    background-color: #3b3b3b;
    color: white;
    position: fixed;
    bottom: 0;
    width: 100%;
    font-size: 0.8rem;
  }}
  footer.dark-mode {{
    background-color: #333;
  }}
  #move-to-top {{
    display: none; /* Hidden by default */
    position: fixed;
    bottom: 30px;
    right: 20px;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    background-color: #ffa51d;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    z-index: 1000;
  }}
  #move-to-top:hover {{
    background-color: black;
  }}
  #move-to-top.dark-mode {{
    background-color: #ffa51d;
    color: white;
  }}
  #move-to-top.dark-mode:hover {{
    background-color: black;
  }}
  .copy-button {{
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: #ffa51d;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 0.5rem;
    cursor: pointer;
  }}
  .copy-button:hover {{
    background-color: black;
  }}
  </style>
</head>
<body>
  <header>
  <h1>Shakib's LeetCode Solutions</h1>
  <p>Explore my solutions to various LeetCode problems with details on runtime, memory usage, and links to the original problems. Use the search bar to quickly find a specific problem.</p>
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
  <!-- Add the "Move to Top" button -->
  <button id="move-to-top" title="Go to top">
    <i class="fas fa-arrow-up"></i>
  </button>
  <!-- Prism.js for syntax highlighting -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-javascript.min.js"></script>
  <script src="script.js"></script>
</body>
</html>
"""

# Generate the JavaScript file
js_content = f"""const problems = {json.dumps(problems, indent=2)};
const container = document.getElementById("solutions-container");
const searchInput = document.getElementById("search-input");
const darkModeToggle = document.getElementById("dark-mode-toggle");
const moveToTopButton = document.getElementById("move-to-top");

// Function to render the problems
function renderProblems(filter = "") {{
  container.innerHTML = ""; // Clear the container
  const filteredProblems = problems.filter(problem =>
    problem.title.toLowerCase().includes(filter.toLowerCase())
  );

  filteredProblems.forEach(problem => {{
    const card = document.createElement("div");
    card.className = "solution-card";

    // Add a copy button for the code block
    const copyButton = document.createElement("button");
    copyButton.className = "copy-button";
    copyButton.innerHTML = '<i class="fas fa-copy"></i>';
    copyButton.addEventListener("click", () => {{
      navigator.clipboard.writeText(problem.code).then(() => {{
        copyButton.innerHTML = '<i class="fas fa-check"></i>';
        setTimeout(() => {{
          copyButton.innerHTML = '<i class="fas fa-copy"></i>';
        }}, 2000);
      }});
    }});

    card.innerHTML = `
      <h2>${{problem.title}}</h2>
      <p><strong>Status:</strong> ${{problem.status}}</p>
      <p><strong>Runtime:</strong> ${{problem.runtime}}</p>
      <p><strong>Memory:</strong> ${{problem.memory}}</p>
      <a href="${{problem.url}}" target="_blank">View Problem</a>
      <h3>Solution:</h3>
      <pre><code class="language-javascript">${{problem.code}}</code></pre>
    `;

    // Append the copy button to the code block
    const preElement = card.querySelector("pre");
    preElement.appendChild(copyButton);

    // Apply dark mode class if enabled
    if (isDarkMode) {{
      card.classList.add("dark-mode");
    }}

    container.appendChild(card);
  }});

  // Highlight syntax using Prism.js
  Prism.highlightAll();
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
  document.querySelector("header").classList.toggle("dark-mode", isDarkMode);
  document.querySelectorAll(".solution-card").forEach(card => {{
    card.classList.toggle("dark-mode", isDarkMode);
  }});
  document.querySelector("footer").classList.toggle("dark-mode", isDarkMode);
  moveToTopButton.classList.toggle("dark-mode", isDarkMode);
}});

// "Move to Top" button functionality
window.addEventListener("scroll", () => {{
  if (window.scrollY > 300) {{
    moveToTopButton.style.display = "block";
  }} else {{
    moveToTopButton.style.display = "none";
  }}
}});

moveToTopButton.addEventListener("click", () => {{
  window.scrollTo({{
    top: 0,
    behavior: "smooth"
  }});
}});

// Initial render
renderProblems();
"""

# Write the HTML and JS files
with open("index.html", "w") as html_file:
    html_file.write(html_content)

with open("script.js", "w") as js_file:
    js_file.write(js_content)

print("[=] Static site generated successfully!")