import os

# Define the language extensions and their corresponding names and icons
LANGUAGES = {
    '.py': ('Python', '![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)', '🐍'),
    '.js': ('JavaScript', '![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)', '🌐'),
    '.cpp': ('C++', '![C++](https://img.shields.io/badge/-C++-00599C?style=flat&logo=c%2B%2B&logoColor=white)', '💻'),
    '.java': ('Java', '![Java](https://img.shields.io/badge/-Java-007396?style=flat&logo=java&logoColor=white)', '☕'),
    '.rkt': ('Racket', '![Racket](https://img.shields.io/badge/-Racket-9F1D20?style=flat&logo=racket&logoColor=white)', '🎨')
}

# Function to count files by extension
def count_files_by_extension(root_dir):
    counts = {lang: 0 for lang in LANGUAGES}
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in LANGUAGES:
                counts[LANGUAGES[ext][0]] += 1
    return counts

# Function to update README.md
def update_readme(counts):
    with open('README.md', 'r') as file:
        readme = file.readlines()

    # Find the line where the table starts and rewrite it
    table_start = readme.index('| Language      | Solutions |\n') + 2
    table_end = table_start + len(LANGUAGES)

    # Build the new table rows
    new_table = []
    for ext, (lang_name, badge, icon) in LANGUAGES.items():
        count = counts[lang_name]
        new_table.append(f"| {badge} | {count} | {icon} |\n")

    # Replace the old table with the new one
    readme[table_start:table_end] = new_table

    # Write the updated README
    with open('README.md', 'w') as file:
        file.writelines(readme)

# Main logic
if __name__ == "__main__":
    counts = count_files_by_extension('.')
    update_readme(counts)
