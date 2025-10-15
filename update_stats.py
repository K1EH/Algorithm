import os
import re

TARGET_FOLDERS = {
    "백준": "BaekjoonHub (Auto)",
    "프로그래머스": "Programmers (Auto)",
    "이것이_취업을_위한_코딩테스트다": "Book Problems",
    "inflearn_2week_algorithm": "Inflearn Course",
    "baekjoon": "Local Workspace",
    "Algorithm_Note": "Personal Notes",
}

README_PATH = "README.md"
STATS_START = "<!-- stats:start -->"
STATS_END = "<!-- stats:end -->"


def count_files(folder):
    """폴더 내 .py/.ipynb/.sql 파일 수 세기"""
    if not os.path.exists(folder):
        return 0
    count = 0
    for root, _, files in os.walk(folder):
        for f in files:
            if f.endswith((".py", ".ipynb", ".sql")):
                count += 1
    return count


def count_problem_folders(folder):
    """백준, 프로그래머스 폴더 구조: 문제 1개당 하위폴더 1개"""
    if not os.path.exists(folder):
        return 0
    count = 0
    for root, dirs, _ in os.walk(folder):
        # 하위 디렉토리가 실제 문제 폴더인지 확인 (README.md 존재 시 문제 폴더로 간주)
        for d in dirs:
            problem_path = os.path.join(root, d)
            if any(
                fname.endswith((".py", ".sql")) for fname in os.listdir(problem_path)
            ):
                count += 1
    return count


def get_count(folder):
    if folder in ["백준", "프로그래머스"]:
        return count_problem_folders(folder)
    return count_files(folder)


def generate_stats_section():
    stats_lines = [
        "\n## 📊 Problem Statistics",
        "",
        "| Category | Folder | Count |",
        "|-----------|---------|--------|",
    ]
    for folder, label in TARGET_FOLDERS.items():
        n = get_count(folder)
        stats_lines.append(f"| {label} | `{folder}/` | {n} |")
    stats_lines.append("\n_Last updated automatically._\n")
    return "\n".join(stats_lines)


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

    print("✅ README.md updated with new problem statistics.")


if __name__ == "__main__":
    update_readme()
