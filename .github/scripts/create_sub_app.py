import os
import sys
from github import Github

def main():
    if len(sys.argv) < 3:
        raise SystemExit("Usage: create_sub_app.py <folder_name> <app_title>")

    folder_name = sys.argv[1].strip().rstrip("/")
    app_title = sys.argv[2].strip()

    token = os.environ["GITHUB_TOKEN"]
    repo_full = os.environ.get("REPO_NAME", "Ank576/FinStatAnalysis")

    g = Github(token)
    repo = g.get_repo(repo_full)

    base_path = folder_name
    branch = "main"

    # Basic templates
    readme_content = f"""# {app_title}

Streamlit-based **tool** inside the FinStatAnalysis repo.

## Overview

- Educational analysis app built with Streamlit.
- Part of the FinStatAnalysis toolkit for financial statement and market analysis.
- For learning and experimentation only (not investment advice).

## Installation

```bash
git clone https://github.com/{repo_full}.git
cd {repo_full}/{base_path}
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## Disclaimer

This app is for educational purposes only and does not constitute financial advice.
"""

    app_py_content = f"""import streamlit as st

st.set_page_config(page_title="{app_title}", layout="wide")

st.title("{app_title}")
st.write("This is a placeholder Streamlit app inside the FinStatAnalysis repository.")
st.info("Extend this app with your desired financial analysis logic.")
"""

    requirements_content = """streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
"""

    files_to_create = {
        f"{base_path}/README.md": readme_content,
        f"{base_path}/app.py": app_py_content,
        f"{base_path}/requirements.txt": requirements_content,
    }

    commit_message = f"Add sub-app folder: {folder_name}"

    # Create each file if it does not exist
    for path, content in files_to_create.items():
        try:
            repo.get_contents(path, ref=branch)
            print(f"Skipped existing file: {path}")
        except Exception:
            repo.create_file(
                path,
                commit_message,
                content,
                branch=branch,
            )
            print(f"Created file: {path}")

if __name__ == "__main__":
    main()
