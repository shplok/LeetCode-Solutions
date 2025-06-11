import os
import sys

# Define the language extensions and their corresponding names and badges
LANGUAGES = {
    '.py': ('Python', '![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)'),
    '.java': ('Java', '![Java](https://img.shields.io/badge/-Java-007396?style=flat&logo=java&logoColor=white)'),
    '.sql': ('SQL', '![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=fff)'),
    '.c': ('C', '![C](https://img.shields.io/badge/C-00599C?logo=c&logoColor=white)'),
}

def count_files_by_extension(root_dir):
    totalCount = 0
    counts = {LANGUAGES[ext][0]: 0 for ext in LANGUAGES}
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in LANGUAGES:
                counts[LANGUAGES[ext][0]] += 1
                totalCount += 1
    return counts, totalCount

def update_readme(counts, totalCount):
    with open('README.md', 'r') as file:
        readme = file.readlines()

    start_line = None
    end_line = None
    for i, line in enumerate(readme):
        if '| Language      | Solutions |' in line:
            start_line = i + 2  # Start after the header row
        elif start_line and line.strip() == '':
            end_line = i
            break

    new_table = []
    for ext, (lang_name, badge) in LANGUAGES.items():
        count = counts[lang_name]
        new_table.append(f"| {badge} | {count} |\n")
    new_table.append(f"| **Total!** | {totalCount} |\n")

    
    header = '# This is a Collection of all the LeetCode Problems that I have Solved!\n'
    if header not in readme:
        readme.insert(0, header + '\n')


    if start_line is not None and end_line is not None:
        if readme[start_line:end_line] == new_table:
            print("No changes needed in README.md")
            sys.exit(0)  # Exit with status 0 if no changes are needed
        readme[start_line:end_line] = new_table
    else:
        readme.append('\n## 🧑‍💻 Languages & Stats\n')
        readme.append('| Language      | Solutions |\n')
        readme.append('| ------------- | ----------|\n')
        readme.extend(new_table)

    with open('README.md', 'w') as file:
        file.writelines(readme)

    print("README.md updated")

if __name__ == "__main__":
    counts, totalCount = count_files_by_extension('.')
    update_readme(counts, totalCount)
