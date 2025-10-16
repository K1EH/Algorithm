import os
import re
from datetime import datetime

README_PATH = "README.md"
STATS_START = "<!-- stats:start -->"
STATS_END = "<!-- stats:end -->"


def count_problem_folders(folder):
    """문제 단위 폴더 개수 세기 (.py나 .sql이 들어있는 폴더만 카운트)"""
    if not os.path.exists(folder):
        return 0
    count = 0
    for root, dirs, files in os.walk(folder):
        if any(f.endswith((".py", ".sql")) for f in files):
            count += 1
    return count


def generate_stats_section():
    baekjoon_count = count_problem_folders("백준")
    programmers_count = count_problem_folders("프로그래머스")

    today = datetime.now().strftime("%Y-%m-%d")

    lines = [
        "\n## 📊 Problem Statistics",
        "",
        "| Platform | Folder | Problem Count |",
        "|-----------|---------|----------------|",
        f"| BaekjoonHub (Auto) | `백준/` | {baekjoon_count} |",
        f"| Programmers (Auto) | `프로그래머스/` | {programmers_count} |",
        "",
        f"_Last updated: {today}_",
    ]
    return "\n".join(lines)


def update_readme():
    if not os.path.exists(README_PATH):
        print("❌ README.md not found.")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_stats = f"{STATS_START}\n{generate_stats_section()}\n{STATS_END}"

    if STATS_START in content and STATS_END in content:
        content = re.sub(f"{STATS_START}.*?{STATS_END}", new_stats, content, flags=re.S)
    else:
        content += f"\n\n{new_stats}\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ README.md updated with date and problem statistics.")


if __name__ == "__main__":
    update_readme()
