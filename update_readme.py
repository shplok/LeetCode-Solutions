import os
import sys

# Map file extensions to a (display name, shields.io badge) pair.
# Several extensions can share a display name (e.g. C++ variants).
def badge(label, color, logo, logo_color="white"):
    return (f"![{label}](https://img.shields.io/badge/-{label.replace(' ', '%20')}-"
            f"{color}?style=flat&logo={logo}&logoColor={logo_color})")

LANGUAGES = {
    ".py":    ("Python",     badge("Python", "3776AB", "python")),
    ".java":  ("Java",       badge("Java", "007396", "java")),
    ".sql":   ("SQL",        badge("MySQL", "4479A1", "mysql")),
    ".cpp":   ("C++",        badge("C++", "00599C", "cplusplus")),
    ".cc":    ("C++",        badge("C++", "00599C", "cplusplus")),
    ".cxx":   ("C++",        badge("C++", "00599C", "cplusplus")),
    ".c":     ("C",          badge("C", "A8B9CC", "c", "black")),
    ".sh":    ("Bash",       badge("Bash", "4EAA25", "gnubash")),
    ".js":    ("JavaScript", badge("JavaScript", "F7DF1E", "javascript", "black")),
    ".ts":    ("TypeScript", badge("TypeScript", "3178C6", "typescript")),
    ".go":    ("Go",         badge("Go", "00ADD8", "go")),
    ".rb":    ("Ruby",       badge("Ruby", "CC342D", "ruby")),
    ".kt":    ("Kotlin",     badge("Kotlin", "7F52FF", "kotlin")),
    ".rs":    ("Rust",       badge("Rust", "000000", "rust")),
    ".swift": ("Swift",      badge("Swift", "F05138", "swift")),
    ".cs":    ("C#",         badge("C%23", "239120", "csharp")),
    ".scala": ("Scala",      badge("Scala", "DC322F", "scala")),
    ".php":   ("PHP",        badge("PHP", "777BB4", "php")),
}

# Files/dirs that are not solutions.
EXCLUDE_FILES = {"update_readme.py"}
EXCLUDE_DIRS = {".git", ".github", "node_modules"}

START_MARK = "<!-- STATS:START -->"
END_MARK = "<!-- STATS:END -->"


def count_solutions(root_dir):
    counts = {}         # display name -> count
    badges = {}         # display name -> badge (first seen)
    total = 0
    for subdir, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fname in files:
            if fname in EXCLUDE_FILES:
                continue
            ext = os.path.splitext(fname)[1].lower()
            if ext not in LANGUAGES:
                continue
            name, bdg = LANGUAGES[ext]
            counts[name] = counts.get(name, 0) + 1
            badges.setdefault(name, bdg)
            total += 1
    return counts, badges, total


def build_table(counts, badges, total):
    rows = ["| Language | Solutions |", "| --- | --- |"]
    # sort by count desc, then name asc
    for name in sorted(counts, key=lambda n: (-counts[n], n)):
        rows.append(f"| {badges[name]} | {counts[name]} |")
    rows.append(f"| **Total** | **{total}** |")
    return "\n".join(rows)


def update_readme(table, path="README.md"):
    header = "# This is a Collection of all the LeetCode Problems that I have Solved!\n"
    section = f"## 🧑‍💻 Languages & Stats\n\n{START_MARK}\n{table}\n{END_MARK}\n"

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = header + "\n"

    if START_MARK in content and END_MARK in content:
        pre = content[: content.index(START_MARK)]
        post = content[content.index(END_MARK) + len(END_MARK):]
        new_content = f"{pre}{START_MARK}\n{table}\n{END_MARK}{post}"
    else:
        # No markers yet (first migration): drop any existing stats section
        # (everything from the "Languages & Stats" heading onward) and append
        # a fresh, marker-delimited one so future runs are idempotent.
        stats_heading = "## 🧑‍💻 Languages & Stats"
        if stats_heading in content:
            content = content[: content.index(stats_heading)]
        if not content.startswith(header):
            content = header + "\n" + content
        new_content = content.rstrip() + "\n\n" + section

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            if f.read() == new_content:
                print("No changes needed in README.md")
                sys.exit(0)

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README.md updated")


if __name__ == "__main__":
    counts, badges, total = count_solutions(".")
    update_readme(build_table(counts, badges, total))
