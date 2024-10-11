import os

# Define the language extensions and their corresponding names and badges
LANGUAGES = {
    '.py': ('Python', '![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)'),
    '.java': ('Java', '![Java](https://img.shields.io/badge/-Java-007396?style=flat&logo=java&logoColor=white)')
}

# Function to count files by extension
def count_files_by_extension(root_dir):
    counts = {LANGUAGES[ext][0]: 0 for ext in LANGUAGES}
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in LANGUAGES:
                counts[LANGUAGES[ext][0]] += 1
    print(f"File counts: {counts}")  # Debug print
    return counts

# Function to update README.md
def update_readme(counts):
    with open('README.md', 'r') as file:
        readme = file.readlines()

    # Find the position of the language table in the README
    start_line = None
    end_line = None
    for i, line in enumerate(readme):
        if '| Language      | Solutions |' in line:
            start_line = i + 2  # Start after the header row
        elif start_line and line.strip() == '':
            end_line = i
            break

    print(f"Start line: {start_line}, End line: {end_line}")  # Debug print

    # Build the new table rows
    new_table = []
    for ext, (lang_name, badge) in LANGUAGES.items():
        count = counts[lang_name]
        new_table.append(f"| {badge} | {count} |\n")

    # Replace or insert the new table
    if start_line is not None and end_line is not None:
        readme[start_line:end_line] = new_table
    else:
        # If no table is found, add it at the end of the file
        readme.append('\n## 🧑‍💻 Languages & Stats\n')
        readme.append('| Language      | Solutions |\n')
        readme.append('| ------------- | ----------|\n')
        readme.extend(new_table)

    # Write the updated README
    with open('README.md', 'w') as file:
        file.writelines(readme)

    print("README updated")  # Debug print

# Main logic
if __name__ == "__main__":
    counts = count_files_by_extension('.')
    update_readme(counts)
