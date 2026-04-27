import os
import requests
import subprocess
from datetime import datetime

TOKEN = os.environ["GH_TOKEN"]
ORG = os.environ["ORG_NAME"]

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_repos():
    repos = []
    page = 1

    while True:
        url = f"https://api.github.com/orgs/{ORG}/repos?per_page=100&page={page}"
        resp = requests.get(url, headers=HEADERS)
        data = resp.json()

        if not data:
            break

        repos.extend([r["name"] for r in data])
        page += 1

    return repos

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def main():
    repos = get_repos()

    print(f"Total repos: {len(repos)}")

    for repo in repos:
        print("=" * 50)
        print(f"Processing: {repo}")

        try:
            clone_url = f"https://{TOKEN}@github.com/{ORG}/{repo}.git"

            run(f"git clone --depth 1 {clone_url}")
            os.chdir(repo)

            os.makedirs(".github", exist_ok=True)

            timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            with open(".github/trigger.txt", "a") as f:
                f.write(f"trigger: {timestamp}\n")

            run("git config user.name 'github-actions'")
            run("git config user.email 'github-actions@github.com'")

            run("git add .github/trigger.txt")
            run(f"git commit -m 'chore: trigger pipeline ({timestamp})' || true")
            run("git push")

            os.chdir("..")

            print("OK")

        except Exception as e:
            print(f"ERROR: {repo} -> {e}")
            os.chdir("..")

if __name__ == "__main__":
    main()