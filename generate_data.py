import os
import json
from pathlib import Path


def parse_submissions():
    submissions_dir = Path('submissions')
    problems = []

    # Iterate through all problem directories
    for problem_dir in submissions_dir.iterdir():
        if not problem_dir.is_dir():
            continue

        # Look for Accepted solutions
        accepted_dir = problem_dir / 'Accepted'
        if not accepted_dir.exists():
            continue

        # Get the most recent accepted submission
        submission_dirs = sorted(
            accepted_dir.iterdir(), key=lambda x: x.name, reverse=True)
        if not submission_dirs:
            continue

        latest_submission = submission_dirs[0]
        info_file = latest_submission / 'info.txt'
        solution_file = latest_submission / 'Solution.py'

        if not info_file.exists() or not solution_file.exists():
            continue

        # Parse submission info
        try:
            with open(info_file, 'r') as f:
                info = json.load(f)

            with open(solution_file, 'r') as f:
                code = f.read()

            problem_data = {
                'title': info['title'],
                'status': info['status_display'],
                'runtime': info['runtime'],
                'memory': info['memory'],
                'code': code,
                'url': f"https://leetcode.com/problems/{info['title_slug']}"
            }
            problems.append(problem_data)

        except (json.JSONDecodeError, KeyError, IOError) as e:
            print(f"Error processing {problem_dir.name}: {str(e)}")
            continue

    # Sort problems by title
    problems.sort(key=lambda x: x['title'])

    # Write to problems.json
    with open('problems.json', 'w') as f:
        json.dump(problems, f, indent=2)


if __name__ == '__main__':
    parse_submissions()
