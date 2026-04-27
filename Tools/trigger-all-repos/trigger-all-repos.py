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


def run(cmd, cwd=None, check=True):
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if check and result.returncode != 0:
        raise Exception(f"Command failed: {cmd}")
    return result.returncode


def get_repos():
    repos = []
    page = 1

    while True:
        url = f"https://api.github.com/orgs/{ORG}/repos?per_page=100&page={page}"
        resp = requests.get(url, headers=HEADERS)
        data = resp.json()

        if not data:
            break

        repos.extend(data)
        page += 1

    return repos


def main():
    repos = get_repos()

    print(f"Total repos: {len(repos)}")

    success = 0
    fail = 0
    skipped = 0

    for repo in repos:
        name = repo["name"]

        print("=" * 50)
        print(f"Processing: {name}")

        # 🔒 Skip se não tem permissão de push
        if not repo.get("permissions", {}).get("push", False):
            print("SKIP -> no write access")
            skipped += 1
            continue

        try:
            clone_url = f"https://{TOKEN}@github.com/{ORG}/{name}.git"

            run(f"git clone --depth 1 {clone_url}")

            os.chdir(name)

            os.makedirs(".github", exist_ok=True)

            file_path = ".github/trigger.txt"
            timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

            with open(file_path, "a") as f:
                f.write(f"trigger: {timestamp}\n")

            run("git config user.name 'github-actions'")
            run("git config user.email 'github-actions@github.com'")

            run("git add .github/trigger.txt")

            # evita commit vazio
            commit_result = subprocess.run(
                "git commit -m \"chore: trigger pipeline\"",
                shell=True
            )

            if commit_result.returncode != 0:
                print("SKIP -> nothing to commit")
                os.chdir("..")
                skipped += 1
                continue

            # 🔥 aqui não pode falhar silencioso
            run("git push")

            os.chdir("..")

            print("OK")
            success += 1

        except Exception as e:
            print(f"FAIL -> {e}")
            fail += 1
            os.chdir("..")

    print("\n" + "=" * 50)
    print(f"SUCCESS: {success}")
    print(f"FAIL: {fail}")
    print(f"SKIPPED: {skipped}")

    # ❌ falha o pipeline se tiver erro
    if fail > 0:
        exit(1)


if __name__ == "__main__":
    main()